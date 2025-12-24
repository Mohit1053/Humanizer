"""Quick 3-sample test with optimized prompt"""
import pandas as pd
import ollama

df = pd.read_csv(r"C:\Users\mohit1\Desktop\Humanizer\final_pledges_merged.csv")

PROMPT = """Rewrite this work pledge to sound like a tired professional venting to a friend late at night.

Rules:
- Keep same emotional meaning about work doubts
- Use contractions: I'm, can't, it's, don't
- Add fillers: "honestly", "like", "you know", "I mean"
- Mix very short sentences with long rambling ones
- Sound genuine and tired
- ONLY output the rewrite, nothing else

Original: {text}

Rewrite:"""

def humanize(text):
    r = ollama.generate(model='llama3:8b', prompt=PROMPT.format(text=text),
                        options={'temperature': 0.95, 'num_predict': 400})
    result = r['response'].strip()
    for m in ['Rewrite:', '(Note', 'Here is', '\n\n']:
        if m in result: result = result.split(m)[0].strip()
    return result.strip('"\'')

samples = [df.at[0, 'pledge'], df.at[100, 'pledge'], df.at[500, 'pledge']]
results = []

print("Generating 3 quick samples...\n")
for i, s in enumerate(samples):
    print(f"--- SAMPLE {i+1} ---")
    print(f"ORIGINAL: {s[:100]}...")
    h = humanize(s)
    print(f"HUMANIZED: {h}\n")
    results.append({'original': s, 'humanized': h})

pd.DataFrame(results).to_csv(r"C:\Users\mohit1\Desktop\Humanizer\quick_samples.csv", index=False)
print("Saved to quick_samples.csv")
