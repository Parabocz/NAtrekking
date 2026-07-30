import re

gen_file = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\generate_unified.py"
with open(gen_file, 'r', encoding='utf-8') as f:
    content = f.read()

mappings = {
    "kilimanjaro-safari-2026.html": "kilimanjaro_safari_hero.jpg",
    "kilimanjaro-safari-2027.html": "kilimanjaro_safari_27_hero.jpg",
    "monte-roraima.html": "roraima_hero.jpg",
    "patagonia-especial-reveillon.html": "patagonia_reveillon_hero.jpg",
    "ushuaia.html": "ushuaia_hero.jpg",
    "patagonia-chilena.html": "patagonia_chilena_hero.jpg",
    "patagonia-argentina.html": "patagonia_argentina_hero.jpg",
    "vulcoes-do-atacama.html": "atacama_hero.jpg",
    "torres-del-paine.html": "torres_paine_hero.jpg",
    "cruce-de-los-andes.html": "andes_hero.jpg",
    
    "trekking-rinoceronte.html": "rinoceronte_hero.jpg",
    "hiking-torre-da-prata.html": "torre_prata_hero.jpg",
    
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

lines = content.split('\n')
for html_file, img_name in mappings.items():
    for i, line in enumerate(lines):
        if f'"filename": "{html_file}"' in line:
            lines[i] = re.sub(r'"img": "public/[^"]+"', f'"img": "public/{img_name}"', line)

content = '\n'.join(lines)
with open(gen_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated ALL mappings in generate_unified.py")
