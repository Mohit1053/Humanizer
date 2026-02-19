"""
OPTIMIZED AI Humanizer - Version 2.0
Based on research on what bypasses AI detectors in 2025:
1. Perplexity variation - unpredictable word choices
2. Burstiness - mixing short and long sentences dramatically
3. Human quirks - typos, filler words, incomplete thoughts
4. Emotional authenticity - personal voice
"""
import pandas as pd
import ollama
import time
import random
from tqdm import tqdm
from datetime import datetime

# ==================== CONFIGURATION ====================
INPUT_CSV = "final_pledges_merged.csv"
OUTPUT_CSV = "final_pledges_humanized.csv"

PLEDGE_COLUMN = 'pledge'
NEW_COLUMN = 'humanized_pledge'

MODEL = 'llama3:8b'
BATCH_SIZE = 50
START_ROW = 0
DELAY_MIN = 0.5
DELAY_MAX = 1.0

# ==================== OPTIMIZED PROMPT ====================
# v5_best - Tested and produces natural human-like output
HUMANIZE_PROMPT = """Transform this work pledge into authentic human speech. 

Rules:
- Preserve EXACT emotional meaning about work doubts/struggles
- Use natural speech patterns: "honestly", "like", "you know", "I mean", "right?"
- Heavy contractions: I'm, can't, won't, it's, that's, don't, you're
- Mix sentence lengths: some very short (3-5 words), some long rambling ones
- Sound like a tired professional venting to a close friend
- Include slight self-doubt phrasing
- NO explanations, NO markdown, NO quotes - ONLY output the rewritten pledge

Original pledge:
{text}

Human version:"""

# ==================== FUNCTIONS ====================

def load_or_resume():
    """Load existing output or start fresh"""
    try:
        df = pd.read_csv(OUTPUT_CSV)
        done = df[NEW_COLUMN].notna().sum()
        print(f"✓ Resuming: {done}/{len(df)} already done")
    except FileNotFoundError:
        df = pd.read_csv(INPUT_CSV)
        df[NEW_COLUMN] = pd.NA
        print(f"✓ Starting fresh: {len(df)} rows")
    return df


def humanize(text):
    """Humanize single text with optimized settings"""
    if pd.isna(text) or not str(text).strip():
        return text
    
    try:
        response = ollama.generate(
            model=MODEL,
            prompt=HUMANIZE_PROMPT.format(text=text),
            options={
                'temperature': 0.95,      # Higher = more creative/unpredictable
                'top_p': 0.92,            # Nucleus sampling
                'top_k': 50,              # Limit vocabulary for each token
                'repeat_penalty': 1.15,   # Avoid repetitive patterns
                'num_predict': 450,       # Allow longer responses
            }
        )
        result = response['response'].strip()
        
        # Aggressive cleanup of any meta-text
        cleanup_markers = [
            'Your natural rewrite:', 'Rewrite:', 'Here is', "Here's", 
            '(Note', '(I aimed', '(I tried', '(I used', 'I hope this',
            'Let me know', 'Feel free', 'This version', 'The rewritten',
            '\n\n(', '\n\nNote:', '\n\nI '
        ]
        for marker in cleanup_markers:
            if marker in result:
                result = result.split(marker)[0].strip()
        
        # Remove surrounding quotes
        result = result.strip('"\'""''')
        
        # Remove any trailing incomplete sentences from cleanup
        if result.endswith('('):
            result = result[:-1].strip()
            
        return result
        
    except Exception as e:
        print(f"\n⚠ Error: {e}")
        return text


def check_ollama():
    """Verify Ollama is running"""
    try:
        models = ollama.list()
        if hasattr(models, 'models'):
            names = [m.model for m in models.models]
        else:
            names = [m.get('model', m.get('name', '')) for m in models.get('models', [])]
        
        if not any('llama3' in str(n) for n in names):
            print(f"❌ Model '{MODEL}' not found. Run: ollama pull {MODEL}")
            return False
        print(f"✓ Ollama ready with {MODEL}")
        return True
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return False


def main():
    print("=" * 60)
    print("AI HUMANIZER v2.0 - Optimized for Undetectability")
    print("=" * 60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if not check_ollama():
        return
    
    df = load_or_resume()
    total = len(df)
    done = df[NEW_COLUMN].notna().sum()
    remaining = total - done
    
    print(f"✓ Rows remaining: {remaining}")
    print(f"✓ Est. time: {remaining * 1.5 / 60:.1f} min")
    print(f"\nProcessing... (Ctrl+C to stop safely)\n")
    
    processed = 0
    start_time = time.time()
    
    try:
        for batch_start in range(START_ROW, total, BATCH_SIZE):
            batch_end = min(batch_start + BATCH_SIZE, total)
            
            pbar = tqdm(range(batch_start, batch_end), 
                       desc=f"Batch {batch_start//BATCH_SIZE + 1}",
                       unit="row")
            
            for i in pbar:
                # Skip if already done
                if pd.notna(df.at[i, NEW_COLUMN]) and str(df.at[i, NEW_COLUMN]).strip():
                    continue
                
                original = df.at[i, PLEDGE_COLUMN]
                humanized = humanize(original)
                df.at[i, NEW_COLUMN] = humanized
                processed += 1
                
                # Show preview
                if humanized:
                    preview = str(humanized)[:35] + "..." if len(str(humanized)) > 35 else humanized
                    pbar.set_postfix_str(preview)
                
                time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            
            # Save after each batch
            df.to_csv(OUTPUT_CSV, index=False)
            
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0
            print(f"✓ Saved! {batch_end}/{total} done | {rate:.1f} rows/sec\n")
    
    except KeyboardInterrupt:
        print("\n\n⚠ Stopping... Saving progress...")
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"✓ Saved to {OUTPUT_CSV}")
        print(f"✓ Resume anytime - it will continue from where it stopped")
        return
    
    df.to_csv(OUTPUT_CSV, index=False)
    elapsed = time.time() - start_time
    
    print("=" * 60)
    print("✓ COMPLETE!")
    print(f"✓ Processed: {processed} rows in {elapsed/60:.1f} min")
    print(f"✓ Output: {OUTPUT_CSV}")
    print("=" * 60)


if __name__ == "__main__":
    main()
