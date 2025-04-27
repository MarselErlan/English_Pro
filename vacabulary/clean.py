import re

# Adjust the path if needed
INPUT_FILE = '/Users/macbookpro/PycharmProjects/English_Pro/vacabulary/t5'
OUTPUT_FILE = 'unique_words5.txt'

# Read the transcript
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract words (including contractions and hyphens)
words = re.findall(r"[A-Za-z0-9'-]+", text)

# Deduplicate in order of first appearance
seen = set()
unique_words = []
for w in words:
    lw = w.lower()  # Normalize case
    if lw not in seen:
        seen.add(lw)
        unique_words.append(w)

# Write out the unique words
with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    for w in unique_words:
        out.write(w + '\n')

print(f"Wrote {len(unique_words)} unique words to {OUTPUT_FILE}")
