import re

with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\.system_generated\steps\1096\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

import re
with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\.system_generated\steps\1096\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'.{0,50}Salk.{0,50}', content, re.IGNORECASE)
with open('output.txt', 'w', encoding='utf-8') as out:
    for m in matches: out.write(m.group(0) + '\n')
    out.write("--- EXPEDI ---\n")
    matches = re.finditer(r'.{0,50}Expedi.{0,50}', content, re.IGNORECASE)
    for m in matches: out.write(m.group(0) + '\n')
    out.write("--- JSON keys ---\n")
    matches = re.finditer(r'"[^"]*Salk[^"]*"', content, re.IGNORECASE)
    for m in matches: out.write(m.group(0) + '\n')
