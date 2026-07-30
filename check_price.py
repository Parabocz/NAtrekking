import json
import re

with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\scratch\scraped_data.json', 'r', encoding='utf-8') as f:
    text_data = json.load(f)

for k, text in text_data.items():
    print(f'\nURL: {k}')
    for line in text.split('\n'):
        # Match R$1000, US$ 500, R$ 1.500, etc.
        if re.search(r'(R\$|US\$|USD)\s*[\d\.,]+', line, re.IGNORECASE):
            print(f'PRICE FOUND: {line.strip()}')
