import sys

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the previous regex with a more robust one
broken_regex = "re.sub(r'--alpha\\\\s+-', '--alpha-', wix_html)"
fixed_regex = "re.sub(r'--alpha\\\\s*-\\\\s*', '--alpha-', wix_html)"

code = code.replace(broken_regex, fixed_regex)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed CSS regex to handle spaces around hyphens")
