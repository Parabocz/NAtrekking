import re

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove onclick from structured_copy.json
text = re.sub(r' onclick="[^"]+"', '', text)

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    f.write(text)

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove onclick from generate_unified.py
text = re.sub(r' onclick="[^"]+"', '', text)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(text)
