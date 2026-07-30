with open('new_parser.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("intro_html += \"</ul></div>\"", "intro_html += \"</ul></div>\"\n            intro_content = intro_html")
text = text.replace("intro_html = \"<p>Uma aventura", "intro_content = \"<p>Uma aventura")
text = text.replace("page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content)", 
                    "page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content if 'intro_content' in locals() else intro_html)")

with open('new_parser.py', 'w', encoding='utf-8') as f:
    f.write(text)
