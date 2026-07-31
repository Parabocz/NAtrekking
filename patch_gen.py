import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = r"""    dist_val = buckets.get\('distancia', ''\)
    if dist_val:
        dist_html = f'''<div class="meta-item">
            <span class="meta-label">Distância</span>
            <span class="meta-value">\{dist_val\}</span>
        </div>'''
    else:
        dist_html = ''
    page_html = page_html.replace\('\{\{ DISTANCE_BLOCK \}\}', dist_html\)

    dif_fis = buckets.get\('dif_fisica'\) or exp.get\('difficulty', ''\)
    if dif_fis:
        dif_fis_html = f'''<div class="meta-item">
            <span class="meta-label">Dif. Física</span>
            <span class="meta-value">\{dif_fis\}</span>
        </div>'''
    else:
        dif_fis_html = ''
    page_html = page_html.replace\('\{\{ DIFFICULTY_FISICA_BLOCK \}\}', dif_fis_html\)

    dif_tec = buckets.get\('dif_tecnica', ''\)
    if dif_tec:
        dif_tec_html = f'''<div class="meta-item">
            <span class="meta-label">Dif. Técnica</span>
            <span class="meta-value">\{dif_tec\}</span>
        </div>'''
    else:
        dif_tec_html = ''
    page_html = page_html.replace\('\{\{ DIFFICULTY_TECNICA_BLOCK \}\}', dif_tec_html\)"""

new_block = """    dist_val = buckets.get('distancia') or 'N/A'
    dist_html = f'''<div class="meta-item">
        <span class="meta-label">Distância</span>
        <span class="meta-value">{dist_val}</span>
    </div>'''
    page_html = page_html.replace('{{ DISTANCE_BLOCK }}', dist_html)

    dif_fis = buckets.get('dif_fisica') or exp.get('difficulty') or 'N/A'
    dif_fis_html = f'''<div class="meta-item">
        <span class="meta-label">Dif. Física</span>
        <span class="meta-value">{dif_fis}</span>
    </div>'''
    page_html = page_html.replace('{{ DIFFICULTY_FISICA_BLOCK }}', dif_fis_html)

    dif_tec = buckets.get('dif_tecnica') or 'N/A'
    dif_tec_html = f'''<div class="meta-item">
        <span class="meta-label">Dif. Técnica</span>
        <span class="meta-value">{dif_tec}</span>
    </div>'''
    page_html = page_html.replace('{{ DIFFICULTY_TECNICA_BLOCK }}', dif_tec_html)"""

new_text = re.sub(old_block, new_block, text)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("generate_unified.py patched.")
