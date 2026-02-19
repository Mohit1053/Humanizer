"""
Generate humanized samples for AI detection testing
"""
import pandas as pd
import ollama

df = pd.read_csv("final_pledges_merged.csv")

# Best prompt after research - focuses on pledge-like emotional content
BEST_PROMPT = """You are rewriting a personal pledge/confession from a working professional.

CRITICAL RULES:
1. Keep the EXACT same emotional meaning about work struggles/doubts
2. Sound like a real exhausted person talking naturally
3. Use contractions (I'm, can't, it's, don't)
4. Add filler words naturally: "honestly", "I mean", "like", "you know"
5. Mix short sentences with longer rambling ones
6. Include human hesitations and self-corrections
7. OUTPUT ONLY THE REWRITTEN TEXT - no explanations

Original pledge: {text}

Rewritten pledge:"""

def humanize(text):
    response = ollama.generate(
        model='llama3:8b',
        prompt=BEST_PROMPT.format(text=text),
        options={'temperature': 0.9, 'top_p': 0.92, 'num_predict': 400}
    )
    result = response['response'].strip()
    
    # Aggressive cleanup
    result = result.replace('Rewritten pledge:', '').strip()
    if '(Note' in result: result = result.split('(Note')[0].strip()
    if '(I ' in result and result.count('(') == 1: result = result.split('(I ')[0].strip()
    if '\n\n' in result: result = result.split('\n\n')[0].strip()
    for marker in ['Here is', 'Here\'s', 'I aimed', 'I tried', 'I used', 'I kept', 'Note:']:
        if marker in result:
            result = result.split(marker)[0].strip()
    result = result.strip('"\'')
    
    return result

# Test on 5 diverse samples
samples = [0, 50, 100, 500, 1000]
results = []

print("Generating humanized samples...")
print("=" * 70)

for idx in samples:
    original = df.at[idx, 'pledge']
    print(f"\n--- Sample from row {idx} ---")
    print(f"ORIGINAL:\n{original}\n")
    
    humanized = humanize(original)
    print(f"HUMANIZED:\n{humanized}\n")
    print("-" * 70)
    
    results.append({
        'row': idx,
        'original': original,
        'humanized': humanized
    })

# Save for easy copy-paste testing
pd.DataFrame(results).to_csv("samples_to_test.csv", index=False)

print("\n" + "=" * 70)
print("SAMPLES SAVED TO: samples_to_test.csv")
print("=" * 70)
print("\nCopy each 'humanized' text and test at:")
print("  - https://gptzero.me/")
print("  - https://zerogpt.com/")
print("  - https://www.zerogpt.com/")
