"""
Generate 10 test samples with optimized humanization
These will be saved for you to test on AI detectors
"""
import pandas as pd
import ollama

INPUT_CSV = "final_pledges_merged.csv"
df = pd.read_csv(INPUT_CSV)

# Optimized prompt - engineered to bypass AI detectors
PROMPT = """<|system|>
You are helping rewrite a personal work pledge to sound more natural and human.
<|user|>
Rewrite this pledge to sound like a real exhausted professional venting to a close friend late at night.

CRITICAL REQUIREMENTS:
- PRESERVE the exact emotional meaning about work doubts/struggles
- Use heavy contractions: I'm, can't, won't, shouldn't, it's, that's, what's
- Add natural filler words: "honestly", "like", "you know", "I mean", "kind of", "basically"
- VARY sentence length dramatically: some 3-4 words, others 25+ words
- Include self-interruptions: "wait, no", "actually", "I don't know"
- Add slight rambling/tangents that circle back
- Use informal punctuation: ... and - for pauses
- Sound tired, genuine, vulnerable
- NO markdown, NO quotes around output, NO explanations
- ONLY output the rewritten pledge, nothing else

Original pledge:
{text}

Your natural rewrite:"""


def humanize(text):
    response = ollama.generate(
        model='llama3:8b',
        prompt=PROMPT.format(text=text),
        options={
            'temperature': 0.95,
            'top_p': 0.92,
            'top_k': 50,
            'repeat_penalty': 1.15,
            'num_predict': 450,
        }
    )
    result = response['response'].strip()
    
    # Cleanup
    for marker in ['Your natural rewrite:', 'Rewrite:', 'Here is', "Here's", 
                   '(Note', '(I aimed', '(I tried', '\n\n(', '\n\nNote:']:
        if marker in result:
            result = result.split(marker)[0].strip()
    result = result.strip('"\'""''')
    
    return result


# Test on 10 diverse samples
test_indices = [0, 25, 50, 100, 200, 500, 1000, 2000, 3000, 4000]
results = []

print("=" * 70)
print("GENERATING 10 OPTIMIZED HUMANIZED SAMPLES")
print("=" * 70)

for idx in test_indices:
    if idx >= len(df):
        continue
        
    original = df.at[idx, 'pledge']
    print(f"\n{'='*70}")
    print(f"SAMPLE {idx} - {df.at[idx, 'occupation']}")
    print(f"{'='*70}")
    print(f"ORIGINAL:\n{original}\n")
    
    humanized = humanize(original)
    print(f"HUMANIZED:\n{humanized}")
    
    results.append({
        'row_index': idx,
        'occupation': df.at[idx, 'occupation'],
        'original': original,
        'humanized': humanized,
        'orig_len': len(original),
        'new_len': len(humanized)
    })

# Save results
results_df = pd.DataFrame(results)
output_file = "TEST_SAMPLES.csv"
results_df.to_csv(output_file, index=False)

print("\n" + "=" * 70)
print("SAMPLES SAVED!")
print("=" * 70)
print(f"\nFile: {output_file}")
print(f"Total samples: {len(results)}")
print("\n" + "-" * 70)
print("NEXT STEPS:")
print("-" * 70)
print("1. Open TEST_SAMPLES.csv")
print("2. Copy each 'humanized' text")
print("3. Test at: https://gptzero.me/")
print("4. Test at: https://www.zerogpt.com/")
print("5. Check if AI detection is < 10%")
print("-" * 70)
