import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Define boundaries to replace the entire semantic parser and formatting section
start_pattern = r'(        if not hero_image:\s*hero_image = "public/fallback_hero\.jpg"\s*if filename not in generated:\s*generated\.add\(filename\)\s*raw_text = scraped_data\.get\(url, ""\) if url else "")'
end_pattern = r'(        with open\(output_path, \'w\', encoding=\'utf-8\'\) as f:\s*f\.write\(page_html\))'

with open('new_parser.py', 'r', encoding='utf-8') as f:
    new_parser = f.read()

def replacer(match):
    return match.group(1) + '\n\n' + new_parser + '\n\n' + match.group(2)

# Build a regex that matches from start_pattern to end_pattern
combined_pattern = start_pattern + r'.*?' + end_pattern

new_text = re.sub(combined_pattern, replacer, text, flags=re.DOTALL)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("generate_unified.py foi atualizado com sucesso!")
