with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()
    
# Fix double indent
text = text.replace("                with open", "        with open")

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(text)
