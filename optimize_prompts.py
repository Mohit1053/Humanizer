"""
AI Humanizer Testing & Optimization Script
Runs multiple prompts, tests outputs, and finds the best approach
"""
import pandas as pd
import ollama
import time

# Load sample data
df = pd.read_csv("final_pledges_merged.csv")

# Test samples (different occupations/styles)
test_samples = [
    df.at[0, 'pledge'],   # Doctor 1
    df.at[5, 'pledge'],   # Doctor 2
    df.at[100, 'pledge'], # Different context
]

# Different prompt strategies to test
PROMPTS = {
    "v1_basic": """Rewrite this text naturally. Keep meaning, add contractions and varied sentences.
Original: {text}
Rewritten:""",

    "v2_casual": """You are a real person sharing your feelings casually. Rewrite this in your own words.
Be natural - use "like", "you know", "I mean", contractions. Vary sentence length. Keep the emotion.
Text: {text}
Your version:""",

    "v3_imperfect": """Rewrite as if you're texting a close friend about your work struggles. 
Be genuine, slightly messy, use filler words, incomplete thoughts sometimes. Keep the core message.
Original: {text}
Your natural rewrite:""",

    "v4_storytelling": """Rewrite this as a genuine personal reflection. 
- Use first person naturally
- Mix short punchy sentences with longer ones
- Add human hesitations like "honestly", "I guess", "kind of"
- Keep the emotional core intact
- NO explanations, just the rewrite

Text: {text}
Rewrite:""",

    "v5_best": """Transform this into authentic human speech. Rules:
1. Preserve the EXACT emotional message
2. Use natural speech patterns: contractions, filler words ("honestly", "like", "you know")
3. Vary rhythm: mix 5-word sentences with 20-word ones
4. Add subtle imperfections humans make
5. Sound like a tired professional venting to a friend
6. Output ONLY the rewritten text, nothing else

Original: {text}

Human version:"""
}

def humanize(text, prompt_template, model='llama3:8b'):
    """Humanize text with given prompt"""
    prompt = prompt_template.format(text=text)
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={'temperature': 0.85, 'top_p': 0.9, 'num_predict': 350}
    )
    result = response['response'].strip()
    
    # Clean up
    for prefix in ['Rewritten:', 'Your version:', 'Your natural rewrite:', 'Rewrite:', 'Human version:']:
        result = result.replace(prefix, '').strip()
    if '(Note:' in result:
        result = result.split('(Note:')[0].strip()
    if '\n\n' in result:
        result = result.split('\n\n')[0].strip()
    result = result.strip('"').strip("'")
    
    return result

def main():
    print("=" * 70)
    print("AI HUMANIZER - PROMPT TESTING & OPTIMIZATION")
    print("=" * 70)
    print(f"\nTesting {len(PROMPTS)} different prompts on {len(test_samples)} samples")
    print("This will generate outputs for you to test on AI detectors\n")
    
    results = []
    
    for sample_idx, sample in enumerate(test_samples):
        print(f"\n{'='*70}")
        print(f"SAMPLE {sample_idx + 1}")
        print(f"{'='*70}")
        print(f"ORIGINAL ({len(sample)} chars):")
        print(f"{sample[:200]}...")
        print()
        
        for prompt_name, prompt_template in PROMPTS.items():
            print(f"\n--- {prompt_name} ---")
            humanized = humanize(sample, prompt_template)
            print(f"OUTPUT: {humanized[:200]}...")
            print(f"Length: {len(humanized)} chars")
            
            results.append({
                'sample_idx': sample_idx + 1,
                'prompt_version': prompt_name,
                'original': sample,
                'humanized': humanized
            })
            time.sleep(1)
    
    # Save all results for testing
    results_df = pd.DataFrame(results)
    results_df.to_csv("test_results.csv", index=False)
    
    print("\n" + "=" * 70)
    print("RESULTS SAVED!")
    print("=" * 70)
    print(f"\nAll outputs saved to: test_results.csv")
    print("\nNEXT STEPS:")
    print("1. Open test_results.csv")
    print("2. Copy 'humanized' texts to https://gptzero.me/ or https://zerogpt.com/")
    print("3. Note which prompt_version gets lowest AI scores")
    print("4. We'll use the winning prompt for bulk processing")

if __name__ == "__main__":
    main()
