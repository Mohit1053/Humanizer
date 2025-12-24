"""
Bulk AI Content Humanizer - Local Offline Solution
Uses Ollama with local LLM to humanize text and bypass AI detectors.
Processes your CSV file in batches, saves progress, and can resume if interrupted.
"""

import pandas as pd
import ollama
import time
import random
from tqdm import tqdm
from datetime import datetime

# ==================== CONFIGURATION ====================
# File paths
INPUT_CSV = r"C:\Users\mohit1\Desktop\Humanizer\final_pledges_merged.csv"
OUTPUT_CSV = r"C:\Users\mohit1\Desktop\Humanizer\final_pledges_humanized.csv"

# Column settings
PLEDGE_COLUMN = 'pledge'              # Column to humanize
NEW_COLUMN = 'humanized_pledge'       # New column for humanized text

# Model settings (use one of these - llama3:8b is recommended)
MODEL = 'llama3:8b'                   # Good balance of speed and quality
# MODEL = 'dolphin-mistral:7b'        # Alternative - more creative
# MODEL = 'phi3:mini'                 # Lighter, faster, less RAM needed

# Processing settings
BATCH_SIZE = 100                      # Save progress every N rows
START_ROW = 0                         # Resume from this row if interrupted
DELAY_MIN = 0.5                       # Min seconds between calls
DELAY_MAX = 1.5                       # Max seconds between calls

# ==================== HUMANIZATION PROMPT ====================
# This prompt is optimized for bypassing AI detectors
PROMPT_TEMPLATE = """Rewrite this text to sound completely natural and human-written. 

Rules:
- Keep the EXACT same meaning and emotions
- Add natural imperfections: contractions, varied sentence lengths, casual phrasing
- Use idioms, filler words, or slight rambling where appropriate
- Make it sound like a real person speaking naturally
- DON'T add any introduction or explanation - just give the rewritten text
- Keep similar length to the original

Original: {text}

Rewritten:"""

# ==================== MAIN SCRIPT ====================

def load_or_create_output():
    """Load existing output or create new dataframe"""
    try:
        # Try to load existing output (for resuming)
        df = pd.read_csv(OUTPUT_CSV)
        print(f"✓ Resuming from existing output file ({len(df)} rows)")
    except FileNotFoundError:
        # Load fresh input
        df = pd.read_csv(INPUT_CSV)
        df[NEW_COLUMN] = pd.NA
        print(f"✓ Starting fresh with input file ({len(df)} rows)")
    return df


def humanize_text(text, model):
    """Humanize a single text using Ollama"""
    if pd.isna(text) or not text or str(text).strip() == '':
        return text
    
    prompt = PROMPT_TEMPLATE.format(text=text)
    
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={
                'temperature': 0.8,      # Adds creativity/variation
                'top_p': 0.9,
                'num_predict': 300,      # Max tokens for response
            }
        )
        result = response['response'].strip()
        
        # Clean up common LLM quirks
        result = result.replace('Rewritten:', '').strip()
        result = result.replace('Here is the rewritten text:', '').strip()
        result = result.strip('"').strip("'")
        
        # Remove any notes/explanations the model might add
        if '(Note:' in result:
            result = result.split('(Note:')[0].strip()
        if '\n\n' in result:
            result = result.split('\n\n')[0].strip()
        if 'I aimed' in result:
            result = result.split('I aimed')[0].strip()
        
        return result
    except Exception as e:
        print(f"\n⚠ Error: {e}")
        return text  # Return original on error


def check_ollama_running():
    """Check if Ollama is running and model is available"""
    try:
        models = ollama.list()
        # Handle both old and new API formats
        if hasattr(models, 'models'):
            model_list = models.models
            model_names = [m.model for m in model_list]
        else:
            model_list = models.get('models', [])
            model_names = [m.get('name', m.get('model', '')) for m in model_list]
        
        # Check if our model is available
        model_base = MODEL.split(':')[0]
        if not any(model_base in str(name) for name in model_names):
            print(f"\n⚠ Model '{MODEL}' not found!")
            print(f"Available models: {model_names}")
            print(f"\nTo download, run: ollama pull {MODEL}")
            return False
        
        print(f"✓ Ollama running with model: {MODEL}")
        return True
    except Exception as e:
        print(f"\n❌ Cannot connect to Ollama!")
        print(f"Error: {e}")
        print("\nMake sure Ollama is installed and running:")
        print("1. Download from: https://ollama.com/download")
        print("2. Install and run Ollama")
        print(f"3. Pull model: ollama pull {MODEL}")
        return False


def main():
    print("=" * 60)
    print("AI Content Humanizer - Local Offline Solution")
    print("=" * 60)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check Ollama
    if not check_ollama_running():
        return
    
    # Load data
    df = load_or_create_output()
    total_rows = len(df)
    
    # Count already processed
    already_done = df[NEW_COLUMN].notna().sum()
    remaining = total_rows - already_done
    
    print(f"✓ Total rows: {total_rows}")
    print(f"✓ Already processed: {already_done}")
    print(f"✓ Remaining: {remaining}")
    print(f"✓ Estimated time: {remaining * 2 / 60:.1f} - {remaining * 3 / 60:.1f} minutes")
    print()
    print("Processing... (Press Ctrl+C to stop safely)")
    print("-" * 60)
    
    # Process in batches
    processed = 0
    start_time = time.time()
    
    try:
        for start in range(START_ROW, total_rows, BATCH_SIZE):
            end = min(start + BATCH_SIZE, total_rows)
            batch_processed = 0
            
            # Progress bar for this batch
            pbar = tqdm(range(start, end), desc=f"Batch {start//BATCH_SIZE + 1}", unit="row")
            
            for i in pbar:
                # Skip if already processed
                if pd.notna(df.at[i, NEW_COLUMN]) and str(df.at[i, NEW_COLUMN]).strip():
                    continue
                
                original = df.at[i, PLEDGE_COLUMN]
                humanized = humanize_text(original, MODEL)
                df.at[i, NEW_COLUMN] = humanized
                
                batch_processed += 1
                processed += 1
                
                # Update progress bar with sample
                if humanized:
                    preview = humanized[:40] + "..." if len(str(humanized)) > 40 else humanized
                    pbar.set_postfix_str(f"'{preview}'")
                
                # Random delay
                time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            
            # Save after each batch
            df.to_csv(OUTPUT_CSV, index=False)
            
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0
            print(f"\n✓ Batch saved! Progress: {end}/{total_rows} | Rate: {rate:.1f} rows/sec")
    
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted! Saving progress...")
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"✓ Progress saved to {OUTPUT_CSV}")
        print(f"✓ Resume by running the script again")
        return
    
    # Final save
    df.to_csv(OUTPUT_CSV, index=False)
    
    elapsed = time.time() - start_time
    print()
    print("=" * 60)
    print("✓ COMPLETE!")
    print(f"✓ Total processed: {processed} rows")
    print(f"✓ Time taken: {elapsed/60:.1f} minutes")
    print(f"✓ Output saved to: {OUTPUT_CSV}")
    print("=" * 60)


if __name__ == "__main__":
    main()
