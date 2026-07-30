import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

# First, restore the footer and script tag at the end.
footer_code = '''
    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <div class="footer-logo">
                    <img src="../public/logo.png" alt="N.A Trekking">
                </div>
                <p>Especialistas em expedições de alta montanha e trekkings inesquecíveis.</p>
                <div class="social-links">
                    <a href="https://instagram.com/n.atrekking" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://wa.me/5541999999999" target="_blank"><i class="fab fa-whatsapp"></i></a>
                    <a href="https://youtube.com" target="_blank"><i class="fab fa-youtube"></i></a>
                </div>
            </div>
            
            <div class="footer-links">
                <h3>Expedições</h3>
                <ul>
                    <li><a href="/#internacional">Internacional</a></li>
                    <li><a href="/#nacional">Nacional</a></li>
                    <li><a href="/#cursos">Cursos</a></li>
                </ul>
            </div>
            
            <div class="footer-contact">
                <h3>Contato</h3>
                <ul>
                    <li><i class="fas fa-envelope"></i> contato@natrekking.com.br</li>
                    <li><i class="fas fa-phone"></i> (41) 99999-9999</li>
                    <li><i class="fas fa-map-marker-alt"></i> Curitiba, PR - Brasil</li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 N.A Trekking. Todos os direitos reservados.</p>
        </div>
    </footer>

    <script type="module" src="/main.js"></script>
</body>
</html>
'''

# Replace everything after </main> with the new footer code
main_end_idx = text.find('</main>')
if main_end_idx != -1:
    new_text = text[:main_end_idx+7] + "\n" + footer_code
    with open('template_expedicao.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Footer restored!")
else:
    print("Could not find </main>")

# Fix generate_unified.py background path logic
with open('generate_unified.py', 'r', encoding='utf-8') as f:
    gen_text = f.read()

# We need to change:
# page_html = page_html.replace('{{ HERO_IMAGE }}', "../" + exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg'))
# to:
# img_path = exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg').replace('public/', '/')
# page_html = page_html.replace('{{ HERO_IMAGE }}', img_path)

old_img_line = "page_html = page_html.replace('{{ HERO_IMAGE }}', \"../\" + exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg'))"
new_img_line = """img_path = exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg').replace('public/', '/')
    page_html = page_html.replace('{{ HERO_IMAGE }}', img_path)"""

gen_text = gen_text.replace(old_img_line, new_img_line)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(gen_text)
print("generate_unified.py fixed!")
