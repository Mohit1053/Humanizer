"""
Quick Test Script - Tests humanization on 5 sample rows
Run this first to verify Ollama is working correctly!
"""

import pandas as pd
import ollama
from datetime import datetime

# Configuration
INPUT_CSV = "final_pledges_merged.csv"
MODEL = 'llama3:8b'
TEST_ROWS = 5

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


def check_ollama():
    """Check Ollama setup"""
    print("Checking Ollama connection...")
    try:
        models = ollama.list()
        # Handle both old and new API formats
        if hasattr(models, 'models'):
            model_list = models.models
            model_names = [m.model for m in model_list]
        else:
            model_list = models.get('models', [])
            model_names = [m.get('name', m.get('model', '')) for m in model_list]
        
        print(f"✓ Ollama is running")
        print(f"✓ Available models: {model_names}")
        
        model_base = MODEL.split(':')[0]
        if not any(model_base in str(name) for name in model_names):
            print(f"\n❌ Model '{MODEL}' not installed!")
            print(f"Run this command to install: ollama pull {MODEL}")
            return False
        
        print(f"✓ Model '{MODEL}' is available")
        return True
    except Exception as e:
        print(f"\n❌ Cannot connect to Ollama: {e}")
        print("\nPlease ensure:")
        print("1. Ollama is installed: https://ollama.com/download")
        print("2. Ollama is running (check system tray on Windows)")
        print(f"3. Model is downloaded: ollama pull {MODEL}")
        return False


def humanize_text(text):
    """Humanize single text"""
    prompt = PROMPT_TEMPLATE.format(text=text)
    response = ollama.generate(
        model=MODEL,
        prompt=prompt,
        options={'temperature': 0.8, 'top_p': 0.9, 'num_predict': 300}
    )
    result = response['response'].strip()
    result = result.replace('Rewritten:', '').strip()
    result = result.strip('"').strip("'")
    return result


def main():
    print("=" * 70)
    print("AI Humanizer - Quick Test (5 samples)")
    print("=" * 70)
    print()
    
    # Check Ollama first
    if not check_ollama():
        return
    
    print()
    print("-" * 70)
    print()
    
    # Load sample data
    df = pd.read_csv(INPUT_CSV)
    print(f"✓ Loaded {len(df)} rows from CSV")
    print(f"✓ Testing first {TEST_ROWS} rows...\n")
    
    for i in range(TEST_ROWS):
        original = df.at[i, 'pledge']
        print(f"--- Row {i+1} ---")
        print(f"ORIGINAL ({len(original)} chars):")
        print(f"  {original[:150]}...")
        print()
        
        print("Humanizing...")
        humanized = humanize_text(original)
        
        print(f"HUMANIZED ({len(humanized)} chars):")
        print(f"  {humanized[:150]}...")
        print()
        print("=" * 70)
        print()
    
    print("✓ Test complete!")
    print("✓ If outputs look natural, run: python humanize_csv.py")
    print()
    print("TIP: Copy some humanized text and test at https://gptzero.me/")


if __name__ == "__main__":
    main()
