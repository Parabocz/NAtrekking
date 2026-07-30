import sys

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

broken_regex = "re.sub(r'--alpha\\\\s*-\\\\s*', '--alpha-', wix_html)"
fixed_regex = "re.sub(r'--([a-zA-Z0-9_]+)\\\\s*-\\\\s*([a-zA-Z0-9_]+)', r'--\\1-\\2', wix_html)"

# We do it twice to catch multiple hyphens like --alpha - bg - drop
code = code.replace(broken_regex, fixed_regex + "\\n                    wix_html = " + fixed_regex)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed CSS regex completely")
