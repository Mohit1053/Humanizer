"""Single sample humanizer - generates one sample at a time for testing"""
import ollama

# Sample pledge to humanize
SAMPLE = """I gotta be sure every single time 'cause lives are on the line here. But sometimes, man, I just wonder if I'm good enough, you know? Like, did I miss something obvious or did I overthink it again? It's crazy how much pressure there is and how little sleep I get. Maybe I should've stayed a barista."""

PROMPT = """You are rewriting a personal pledge from a working professional sharing their work struggles.

RULES:
1. Keep EXACT same emotional meaning about doubts and work pressure  
2. Sound like a real tired person venting naturally
3. Use contractions: I'm, can't, it's, don't, wouldn't
4. Add fillers: "honestly", "I mean", "like", "you know", "kind of"
5. Mix sentence lengths - some short, some long and rambling
6. Include slight hesitations and self-corrections
7. NO explanations - ONLY output the rewritten text

Original: {text}

Rewrite:"""

print("Generating humanized version...")
response = ollama.generate(
    model='llama3:8b',
    prompt=PROMPT.format(text=SAMPLE),
    options={'temperature': 0.9, 'top_p': 0.92, 'num_predict': 400}
)

result = response['response'].strip()

# Clean
for marker in ['Rewrite:', 'Here is', 'Here\'s', '(Note', '(I aimed', '(I used', 'I tried']:
    if marker in result:
        result = result.split(marker)[0].strip() if marker != 'Rewrite:' else result.replace(marker, '').strip()
if '\n\n' in result:
    result = result.split('\n\n')[0].strip()
result = result.strip('"\'')

print("\n" + "=" * 70)
print("ORIGINAL:")
print(SAMPLE)
print("\n" + "=" * 70)
print("HUMANIZED:")
print(result)
print("\n" + "=" * 70)
print("\nCopy the HUMANIZED text above and test at:")
print("https://gptzero.me/")
