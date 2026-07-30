with open('generate_unified.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_line = -1
end_line = -1

for i, l in enumerate(lines):
    if 'def clean_lines(text):' in l and start_line == -1:
        # Go up one line to include the Semantic Parser comment
        start_line = i - 1 
    if "with open(page_path, 'w', encoding='utf-8') as pf:" in l:
        end_line = i
        break

print(f"start: {start_line}, end: {end_line}")

if start_line != -1 and end_line != -1:
    with open('new_parser.py', 'r', encoding='utf-8') as f:
        new_parser = f.read()

    # Create the new file content
    new_content = "".join(lines[:start_line]) + new_parser + "\n        " + "".join(lines[end_line:])
    
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("generate_unified.py patched successfully using exact line indices!")
else:
    print("Could not find start/end bounds.")
