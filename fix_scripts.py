import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

correct_scripts = '''    <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.29/bundled/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script type="module" src="/script.js"></script>
'''

text = text.replace('<script type="module" src="/main.js"></script>', correct_scripts)

with open('template_expedicao.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Template scripts fixed!")
