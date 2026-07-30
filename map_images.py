import os
import shutil
import re

brain_dir = r"C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b"
public_dir = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\public"

# The mapping of generator filename keys to the actual image names in public/
# The user wants exact correct images mapped.
# We have existing images and newly created ones.
mappings = {
    "kilimanjaro-safari-2026.html": "kilimanjaro_safari_hero_1785360555337.jpg",
    "kilimanjaro-safari-2027.html": "kilimanjaro_safari_27_hero.jpg",
    "monte-roraima.html": "roraima_hero_1785360565465.jpg",
    "patagonia-especial-reveillon.html": "patagonia_reveillon_hero_1785360574602.jpg",
    "ushuaia.html": "ushuaia_hero_1785360593447.jpg",
    "patagonia-chilena.html": "patagonia_chilena_hero_1785360603284.jpg",
    "patagonia-argentina.html": "patagonia_argentina_hero_1785360613356.jpg",
    "vulcoes-do-atacama.html": "atacama_hero_1785360644849.jpg",
    "torres-del-paine.html": "torres_paine_hero_1785360623634.jpg",
    "cruce-de-los-andes.html": "andes_hero_1785360668799.jpg",
    
    "trekking-rinoceronte.html": "rinoceronte_hero_1785360679293.jpg",
    "hiking-torre-da-prata.html": "torre_prata_hero_1785360688320.jpg",
    
    "lencois-maranhenses-ago-2026.html": "lencois_maranhenses_ago_hero.jpg",
    "pedra-do-cantagalo.html": "pedra_cantagalo_hero.jpg",
    "curso-trekking-agosto.html": "curso_trekking_ago_hero.jpg",
    "espraiado-x-soldados.html": "espraiado_soldados_hero.jpg",
    "travessia-araca-x-crista.html": "araca_crista_hero.jpg",
    "travessia-picos-de-jaragua.html": "picos_jaragua_hero.jpg",
    "fenda-cruz-de-pedra.html": "cruz_pedra_hero.jpg",
    "curso-trekking-setembro.html": "curso_trekking_set_hero.jpg",
    "lencois-maranhenses-jul-2027.html": "lencois_maranhenses_jul_hero.jpg"
}

# The images that were just generated in the brain directory
generated_files = [f for f in os.listdir(brain_dir) if f.endswith('.jpg') and not f.startswith('hero_ mountain')]
for f in generated_files:
    # the format is something_hero_123456.jpg -> we want something_hero.jpg
    match = re.match(r'(.+?)_\d+\.jpg$', f)
    if match:
        clean_name = match.group(1) + '.jpg'
        src = os.path.join(brain_dir, f)
        dst = os.path.join(public_dir, clean_name)
        shutil.copy2(src, dst)
        print(f"Copied {f} to {clean_name}")

# Now update generate_unified.py
gen_file = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\generate_unified.py"
with open(gen_file, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the "img": "public/..." for each of these
for html_file, img_name in mappings.items():
    # Find the line that has this filename
    # e.g. "filename": "monte-roraima.html"
    # we want to replace its "img": "public/..." with "img": "public/{img_name}"
    
    # We can use regex to target the exact block
    # Match the block up to the filename
    # It looks like: "img": "public/something.jpg", "link": ..., "filename": "html_file"
    # We can just do a multi-line substitution or just parse and dump if it wasn't a raw string.
    # But generate_unified.py has it as a raw string!
    # Let's find the exact line
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if f'"filename": "{html_file}"' in line:
            # replace "img": "public/...",
            new_line = re.sub(r'"img": "public/[^"]+"', f'"img": "public/{img_name}"', line)
            lines[i] = new_line

content = '\n'.join(lines)
with open(gen_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated generate_unified.py")
