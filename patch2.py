import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('        # ── Semantic Parser ────────────────────────────────────────────────')
end_idx = text.find('        # ── Escrever o HTML Final ──────────────────────────────────────────')

if start_idx == -1:
    print("Start marker not found.")
if end_idx == -1:
    print("End marker not found. Trying fallback.")
    # Look for the last `page_html = template_html.replace`
    end_idx = text.rfind('        with open(output_path, \'w\', encoding=\'utf-8\') as f:')

print(f"Indices: start={start_idx}, end={end_idx}")

if start_idx != -1 and end_idx != -1:
    with open('new_parser.py', 'r', encoding='utf-8') as f:
        new_parser = f.read()
    
    new_text = text[:start_idx] + new_parser + '\n\n' + text[end_idx:]
    
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Patched successfully.")
else:
    print("Failed to patch.")
