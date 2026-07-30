import json
import re

with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\scratch\scraped_data.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

# Atacama URL might have encoding issue in key
atacama_key = next((k for k in scraped.keys() if 'atacama' in k), None)
if atacama_key:
    scraped['https://natrekking.com.br/vulcões-do-atacama-jan-27'] = scraped.pop(atacama_key)

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured = json.load(f)

def clean_text(lines):
    # remove empty lines and duplicates sequentially
    res = []
    for l in lines:
        l = l.strip()
        if not l: continue
        if len(res) > 0 and res[-1] == l: continue
        res.append(l)
    return res

def parse_page(url, text):
    lines = clean_text(text.split('\n'))
    
    buckets = {
        'historia': [],
        'vibe': [],
        'specs': [],
        'cronograma': [],
        'atencao': [],
        'incluso': [],
        'nao_incluso': [],
        'investimento': [],
        'politica': [],
        'faq': []
    }
    
    current_section = 'intro'
    current_day = None
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Section transitions
        if 'incluso no investimento' in line_lower or line_lower == 'incluso':
            current_section = 'incluso'
            continue
        elif 'não incluso' in line_lower or 'nao incluso' in line_lower:
            current_section = 'nao_incluso'
            continue
        elif 'investimento' in line_lower and 'incluso' not in line_lower:
            current_section = 'investimento'
            continue
        elif 'politica de cancelamento' in line_lower or 'política de cancelamento' in line_lower:
            current_section = 'politica'
            continue
        elif 'perguntas frequentes' in line_lower or 'dúvidas' in line_lower or 'quais documentos' in line_lower:
            current_section = 'faq'
            # don't continue, keep the question
            
        if current_section == 'intro':
            # Detect days for timeline
            if re.match(r'^(dia \d+|dia \d+ de)', line_lower):
                current_section = 'cronograma'
            else:
                if 'data:' in line_lower or 'duração:' in line_lower or 'ponto de encontro:' in line_lower or 'dificuldade' in line_lower:
                    buckets['specs'].append(line)
                elif 'atenção' in line_lower or 'condições do tempo' in line_lower:
                    buckets['atencao'].append(line)
                elif len(line) > 50:
                    buckets['vibe'].append(line)
                
        if current_section == 'cronograma':
            if re.match(r'^(dia \d+|dia \d+ de)', line_lower) or (len(line) < 20 and 'dia' in line_lower and not 'bom dia' in line_lower):
                current_day = {"titulo": line, "descricao": []}
                buckets['cronograma'].append(current_day)
            elif current_day:
                current_day['descricao'].append(line)
                
        elif current_section == 'incluso':
            if not 'investimento' in line_lower:
                buckets['incluso'].append(line)
        elif current_section == 'nao_incluso':
            if not 'investimento' in line_lower:
                buckets['nao_incluso'].append(line)
        elif current_section == 'investimento':
            buckets['investimento'].append(line)
        elif current_section == 'politica':
            buckets['politica'].append(line)
        elif current_section == 'faq':
            buckets['faq'].append(line)

    # Post-process cronograma
    for step in buckets['cronograma']:
        step['descricao'] = '\n'.join(step['descricao'])
        
    # Post-process FAQ (naive: even index = q, odd index = a)
    # Actually just dump strings and generate_unified.py will handle it since we fixed it!
    # Wait, we fixed it to handle string for `resposta`, but it expects `dict` with `pergunta` and `resposta`.
    faq_list = []
    q = None
    for f in buckets['faq']:
        if '?' in f or 'quais' in f.lower() or 'como' in f.lower():
            if q:
                faq_list.append({"pergunta": q, "resposta": ""})
            q = f
        else:
            if q:
                faq_list.append({"pergunta": q, "resposta": f})
                q = None
            else:
                if faq_list:
                    faq_list[-1]["resposta"] += "\n" + f
    if q:
        faq_list.append({"pergunta": q, "resposta": ""})
    buckets['faq'] = faq_list
    
    return buckets

urls_to_process = [
    "https://natrekking.com.br/kilimanjaro2026",
    "https://natrekking.com.br/kilimanjarosafari2026",
    "https://natrekking.com.br/kilimanjaro-safari-2027",
    "https://natrekking.com.br/roraimanov2026",
    "https://natrekking.com.br/ushuaia-dez26-jan27",
    "https://natrekking.com.br/patagoniachilenaespecial",
    "https://natrekking.com.br/calafate-chalten-especial",
    "https://natrekking.com.br/vulcões-do-atacama-jan-27",
    "https://natrekking.com.br/torresdelpaineo2027",
    "https://natrekking.com.br/crucedelosandes2027",
    "https://natrekking.com.br/travpicosdejaragua",
    "https://natrekking.com.br/fendacruzdepedra",
    "https://natrekking.com.br/curso-de-trekking-setembro",
    "https://natrekking.com.br/lencois-maranhenses-jul-27",
    "https://natrekking.com.br/rinoceronte",
    "https://natrekking.com.br/torredaprata",
    "https://natrekking.com.br/cantagalo",
    "https://natrekking.com.br/lencoismaranhensesagosto2026",
    "https://natrekking.com.br/curso-de-trekking-agosto",
    "https://natrekking.com.br/espraiadoxsoldados",
    "https://natrekking.com.br/travessiaaracaxcrista"
]

for url in urls_to_process:
    if url in scraped:
        print(f"Processing {url}...")
        parsed = parse_page(url, scraped[url])
        # Preserve Patagonia Especial since we already did it perfectly manually
        if url != 'https://natrekking.com.br/patagonia-especial':
            if url not in structured:
                structured[url] = {}
            for k in parsed:
                structured[url][k] = parsed[k]

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(structured, f, ensure_ascii=False, indent=4)
print("Finished cloning data!")
