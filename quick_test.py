"""Quick single-text test for Ollama humanization"""
import ollama

text = "I gotta be sure every single time 'cause lives are on the line here. But sometimes, man, I just wonder if I'm good enough."

prompt = f"""Rewrite this text to sound completely natural and human-written. 
Keep the same meaning. Add natural imperfections like contractions, varied sentences.
DON'T add any introduction - just give the rewritten text.

Original: {text}

Rewritten:"""

print("Testing Ollama with a single text...")
print(f"\nORIGINAL: {text}")
print("\nProcessing...")

response = ollama.generate(
    model='llama3:8b',
    prompt=prompt,
    options={'temperature': 0.8, 'num_predict': 200}
)

result = response['response'].strip()
print(f"\nHUMANIZED: {result}")
print("\n✓ Success! Ollama is working correctly.")
print("Now you can run: python humanize_csv.py")
