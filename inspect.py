with open('generate_unified.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'with open' in l and 'w' in l:
        print(f'{i:03d}: {l.strip()}')
