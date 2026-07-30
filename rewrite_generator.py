import re
import os

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    old_script = f.read()

# Extract data list
data_match = re.search(r'data\s*=\s*\[.*?\]', old_script, flags=re.DOTALL)
if not data_match:
    print("Failed to find data array!")
    exit(1)

data_code = data_match.group(0)

new_script = f'''import os
import json

# ==========================================
# 1. EXPEDITION DATA
# ==========================================
{data_code}

# ==========================================
# 2. LOAD STRUCTURED COPY JSON
# ==========================================
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured_copy = json.load(f)

# ==========================================
# 3. LOAD TEMPLATES
# ==========================================
with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    template = f.read()

os.makedirs('expedicoes', exist_ok=True)

# ==========================================
# 4. GENERATOR LOOP
# ==========================================
for exp in data:
    if not exp.get("filename"):
        continue

    url = exp.get('url')
    buckets = structured_copy.get(url, {{
        'historia': [], 'vibe': [], 'specs': [], 'cronograma': [],
        'atencao': [], 'incluso': [], 'nao_incluso': [],
        'investimento': [], 'politica': [], 'faq': []
    }})

    # Format HTML Blocks
    historia_content = "".join(f"<p style='margin-bottom: 1rem;'>{{p}}</p>" for p in buckets['historia']) if buckets['historia'] else "<p>Detalhes completos em breve.</p>"
    vibe_content = "".join(f"<p style='margin-bottom: 1rem;'>{{p}}</p>" for p in buckets['vibe']) if buckets['vibe'] else ""
    
    if buckets['atencao']:
        atencao_content = f"""<div style='background: rgba(244,67,54,0.1); border-left: 4px solid #F44336; padding: 1.5rem; margin-bottom: 3rem; border-radius: 4px;'>
            <h3 style='color: #F44336; margin-bottom: 1rem;'><i class='fas fa-exclamation-triangle'></i> Atenção</h3>
            {{"".join(f"<p style='margin-bottom:0.5rem; color:#ddd;'>{{p}}</p>" for p in buckets['atencao'])}}
        </div>"""
    else:
        atencao_content = ""

    timeline_html = ""
    for step in buckets['cronograma']:
        step_title = step.get('titulo', 'Passo')
        step_details = step.get('detalhes', [])
        details_html = "".join(f"<li>{{d}}</li>" for d in step_details)
        timeline_html += f"""
        <div class="timeline-item">
            <div class="timeline-content">
                <h3 class="timeline-title">{{step_title}}</h3>
                <ul class="timeline-details">
                    {{details_html}}
                </ul>
            </div>
        </div>
        """
    if not timeline_html:
        timeline_html = "<p>Roteiro detalhado em breve.</p>"

    included_html = "".join(f"<li><i class='fas fa-check'></i> {{item}}</li>" for item in buckets['incluso']) if buckets['incluso'] else "<li>Consultar</li>"
    excluded_html = "".join(f"<li><i class='fas fa-times'></i> {{item}}</li>" for item in buckets['nao_incluso']) if buckets['nao_incluso'] else "<li>Consultar</li>"

    if buckets['investimento']:
        price_content = "".join(f"<p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>{{p}}</p>" for p in buckets['investimento'])
        price_content += "<br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Garantir minha vaga</a>"
    else:
        price_content = "<p style='font-size: 1.1rem;'>Consulte nossa equipe para obter os valores e formas de pagamento atualizados.</p><br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Consultar Valores</a>"

    faq_html = ""
    for faq in buckets['faq']:
        q = faq.get('pergunta', '')
        a_list = faq.get('resposta', [])
        a_html = "".join(f"<p>{{ans}}</p>" for ans in a_list)
        faq_html += f"""
        <div class="accordion-item">
            <button class="accordion-header">
                {{q}}
                <i class="fas fa-chevron-down"></i>
            </button>
            <div class="accordion-content">
                {{a_html}}
            </div>
        </div>
        """

    politica_html = ""
    if buckets['politica']:
        p_html = "".join(f"<p style='margin-bottom: 0.5rem;'>{{p}}</p>" for p in buckets['politica'])
        politica_html = f"""
        <div class="accordion-item">
            <button class="accordion-header" style="color: #F44336;">
                Política de Cancelamento
                <i class="fas fa-chevron-down"></i>
            </button>
            <div class="accordion-content">
                {{p_html}}
            </div>
        </div>
        """

    # Inject into template
    page_html = template.replace('{{ TITLE }}', exp.get('title', 'Expedição'))
    page_html = page_html.replace('{{ HERO_IMAGE }}', "../" + exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg'))
    page_html = page_html.replace('{{ DATES }}', exp.get('dates', ''))
    page_html = page_html.replace('{{ DURATION }}', exp.get('dur', ''))
    page_html = page_html.replace('{{ LOCATION }}', exp.get('loc', ''))
    page_html = page_html.replace('{{ DIFFICULTY }}', exp.get('difficulty', ''))
    page_html = page_html.replace('{{ ELEVATION }}', exp.get('elevation', ''))
    
    page_html = page_html.replace('{{ HISTORIA_CONTENT }}', historia_content)
    page_html = page_html.replace('{{ VIBE_CONTENT }}', vibe_content)
    page_html = page_html.replace('{{ ATENCAO_CONTENT }}', atencao_content)
    page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_html)
    page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_html)
    page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_html)
    page_html = page_html.replace('{{ PRICE_CONTENT }}', price_content)
    page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_html)
    page_html = page_html.replace('{{ POLITICA_CONTENT }}', politica_html)

    out_path = os.path.join('expedicoes', exp['filename'])
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(page_html)

print("Geradas todas as páginas usando o modelo de 10 blocos!")
'''

with open('generate_unified_new.py', 'w', encoding='utf-8') as f:
    f.write(new_script)

print("Created generate_unified_new.py")
