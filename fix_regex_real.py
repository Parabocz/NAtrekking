import re
import sys

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the specific line no matter what the old regex was
old_regex = r"wix_html = re.sub(r'--alpha\\s+-', '--alpha-', wix_html)"
# We will just sanitize all spaces around hyphens in CSS variables.
# A CSS variable looks like --varName. If there are spaces around the hyphen, it breaks.
# We'll use a very robust regex: re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)
new_regex = r"wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)"
new_regex += "\n                    wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)"

if old_regex in code:
    code = code.replace(old_regex, new_regex)
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Regex fixed successfully!")
else:
    print("Old regex not found.")
