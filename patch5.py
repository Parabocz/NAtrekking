with open('generate_unified.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_line = -1
end_line = -1

for i, l in enumerate(lines):
    if 'def clean_lines(text):' in l and start_line == -1:
        start_line = i - 1 
    if '# 3. Conditional Elevation' in l:
        end_line = i
        break

print(f"start: {start_line}, end: {end_line}")

if start_line != -1 and end_line != -1:
    with open('new_parser.py', 'r', encoding='utf-8') as f:
        new_parser = f.read()

    new_content = "".join(lines[:start_line]) + new_parser + "\n        " + "".join(lines[end_line:])
    
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patched!")
