import os
import shutil
import re

# Paths
brain_dir = r"C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b"
public_dir = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\public"

# 1. Copy images
for file in os.listdir(brain_dir):
    if 'hero' in file and file.endswith('.jpg'):
        src = os.path.join(brain_dir, file)
        dst = os.path.join(public_dir, file)
        shutil.copy2(src, dst)
        print(f"Copied {file} to public/")

# 2. Add accordion and timeline logic to script.js
with open('script.js', 'r', encoding='utf-8') as f:
    script_js = f.read()

additional_js = """
// --- Accordion Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', function() {
            this.classList.toggle('active');
            const content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                content.style.paddingTop = '0';
                content.style.paddingBottom = '0';
                content.style.opacity = '0';
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                content.style.paddingTop = '1rem';
                content.style.paddingBottom = '1rem';
                content.style.opacity = '1';
            }
        });
    });

    // --- Timeline Intersection Observer ---
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.timeline-item').forEach(item => {
        observer.observe(item);
    });
});
"""

if 'Accordion Logic' not in script_js:
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write(additional_js)
    print("Added logic to script.js")

# 3. Fix style.css (Remove opacity: 0 and configure accordion)
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix timeline opacity (all instances)
css = re.sub(r'opacity:\s*0;', 'opacity: 1;', css)
css = re.sub(r'transform:\s*translateY\(20px\);', 'transform: translateY(0);', css)
css = re.sub(r'transform:\s*translateX\(-20px\);', 'transform: translateX(0);', css)

# Add accordion CSS if not present
if '.accordion-content {' not in css:
    accordion_css = """
.accordion-header {
    width: 100%;
    text-align: left;
    padding: 1rem 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: none;
    outline: none;
    color: white;
    font-size: 1.1rem;
    cursor: pointer;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
    transition: background 0.3s;
}
.accordion-header:hover {
    background: rgba(255, 255, 255, 0.1);
}
.accordion-header i {
    transition: transform 0.3s;
}
.accordion-header.active i {
    transform: rotate(180deg);
}
.accordion-content {
    max-height: 0;
    overflow: hidden;
    padding: 0 1.5rem;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 8px;
    opacity: 0;
    transition: max-height 0.4s ease, padding 0.4s ease, opacity 0.4s ease;
    margin-bottom: 1rem;
}
.accordion-content p {
    margin-bottom: 1rem;
}
"""
    css += accordion_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css fixed!")

# 4. Update generate_unified.py data to use new AI images
with open('generate_unified.py', 'r', encoding='utf-8') as f:
    gen = f.read()

# Equador
gen = gen.replace('"img": "public/agenda_internacional_1.jpg", "link": None', '"img": "public/equador_hero_1785360532710.jpg", "link": None')
# Kilimanjaro 2026
gen = gen.replace('"img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/kilimanjaro2026"', '"img": "public/kilimanjaro_hero_1785360543579.jpg", "link": "https://natrekking.com.br/kilimanjaro2026"')
# Kili Safari
gen = gen.replace('"img": "public/agenda_internacional_3.jpg", "link": "https://natrekking.com.br/kilimanjarosafari2026"', '"img": "public/kilimanjaro_safari_hero_1785360555337.jpg", "link": "https://natrekking.com.br/kilimanjarosafari2026"')
# Roraima
gen = gen.replace('"img": "public/agenda_internacional_4.jpg", "link": "https://natrekking.com.br/roraimanov2026"', '"img": "public/roraima_hero_1785360565465.jpg", "link": "https://natrekking.com.br/roraimanov2026"')
# Patagonia Especial
gen = gen.replace('"img": "public/agenda_internacional_5.jpg", "link": "https://natrekking.com.br/patagonia-especial"', '"img": "public/patagonia_reveillon_hero_1785360574602.jpg", "link": "https://natrekking.com.br/patagonia-especial"')
# Ushuaia
gen = gen.replace('"img": "public/agenda_internacional_6.jpg", "link": "https://natrekking.com.br/ushuaia-dez26-jan27"', '"img": "public/ushuaia_hero_1785360593447.jpg", "link": "https://natrekking.com.br/ushuaia-dez26-jan27"')
# Patagonia Chilena
gen = gen.replace('"img": "public/agenda_internacional_7.jpg", "link": "https://natrekking.com.br/patagoniachilenaespecial"', '"img": "public/patagonia_chilena_hero_1785360603284.jpg", "link": "https://natrekking.com.br/patagoniachilenaespecial"')
# Patagonia Argentina
gen = gen.replace('"img": "public/agenda_internacional_8.jpg", "link": "https://natrekking.com.br/calafate-chalten-especial"', '"img": "public/patagonia_argentina_hero_1785360613356.jpg", "link": "https://natrekking.com.br/calafate-chalten-especial"')
# Atacama
gen = gen.replace('"img": "public/agenda_internacional_9.jpg", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27"', '"img": "public/atacama_hero_1785360644849.jpg", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27"')
# Torres del Paine
gen = gen.replace('"img": "public/agenda_internacional_10.jpg", "link": "https://natrekking.com.br/torresdelpaineo2027"', '"img": "public/torres_paine_hero_1785360623634.jpg", "link": "https://natrekking.com.br/torresdelpaineo2027"')
# Cruce de Los Andes
gen = gen.replace('"img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/crucedelosandes2027"', '"img": "public/andes_hero_1785360668799.jpg", "link": "https://natrekking.com.br/crucedelosandes2027"')

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(gen)
print("generate_unified.py updated with AI Images!")
