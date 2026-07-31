import json
import re

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)
sc_keys = set(sc.keys())

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    gen = f.read()

matches = re.findall(r'"url": "([^"]+)"', gen)
gen_urls = set(matches)

print('In generate_unified but NOT in structured_copy:', gen_urls - sc_keys)
print('In structured_copy but NOT in generate_unified:', sc_keys - gen_urls)
