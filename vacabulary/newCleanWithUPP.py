import re

# Adjust the path if needed
INPUT_FILE = '/Users/macbookpro/PycharmProjects/English_Pro/vacabulary/f_uw2.txt'
OUTPUT_FILE = 'f_uw3'

# Read the transcript
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

# Grab candidate tokens (letters, digits, apostrophes, hyphens)
raw_tokens = re.findall(r"[A-Za-z0-9'-]+", text)

seen = set()
unique_words = []

for token in raw_tokens:
    # 1) strip any leading non-letters
    token = re.sub(r'^[^A-Za-z]+', '', token)
    # 2) drop empty strings
    if not token:
        continue
    # 3) drop pure numbers
    if token.isdigit():
        continue
    # normalize for dedup
    lw = token.lower()
    if lw not in seen:
        seen.add(lw)
        unique_words.append(token)

# Capitalize first letter of each word
unique_words = [w[0].upper() + w[1:] for w in unique_words]

# Write out the unique words
with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    for w in unique_words:
        out.write(w + '\n')

print(f"Wrote {len(unique_words)} unique words to {OUTPUT_FILE}")
