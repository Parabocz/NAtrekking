import json
from bs4 import BeautifulSoup
import re

def clean_text(lines):
    res = []
    for l in lines:
        l = l.strip()
        if not l: continue
        if len(res) > 0 and res[-1] == l: continue
        res.append(l)
    return res

def parse_local(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    texts = []
    for p in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']):
        t = p.get_text(strip=True)
        texts.append(t)
        
    lines = clean_text(texts)
    
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
    
    state = 'intro'
    current_day = None
    
    for line in lines:
        line_lower = line.lower()
        
        # Exact match transitions
        if line_lower == 'incluso no investimento' or line_lower == 'o que está incluso' or line_lower == 'incluso':
            state = 'incluso'
            continue
        elif line_lower == 'não incluso no investimento' or line_lower == 'não incluso no pacote' or line_lower == 'não incluso':
            state = 'nao_incluso'
            continue
        elif line_lower == 'investimento':
            state = 'investimento'
            continue
        elif 'politica de cancelamento' in line_lower or 'política de cancelamento' in line_lower:
            state = 'politica'
            continue
        elif line_lower in ['perguntas frequentes', 'dúvidas frequentes', 'dúvidas', 'quais documentos preciso?']:
            state = 'faq'
            if 'quais documentos' in line_lower:
                buckets['faq'].append(line)
            continue
        
        if line_lower in ['cronograma', 'roteiro', 'dia', 'como vai rolar a trip', 'como vai rolar essa trip', 'dados da expedição']:
            continue
            
        # Timeline
        if state in ['intro', 'cronograma'] and re.match(r'^(dia \d+|dia \d+ de|primeiro dia|segundo dia)', line_lower):
            state = 'cronograma'
            current_day = {"titulo": line, "descricao": []}
            buckets['cronograma'].append(current_day)
            continue
            
        if state == 'intro':
            if 'data:' in line_lower or 'duração:' in line_lower or 'ponto de encontro:' in line_lower or 'dificuldade' in line_lower or 'elevação' in line_lower or 'distância:' in line_lower:
                buckets['specs'].append(line)
            elif 'atenção' in line_lower or 'condições do tempo' in line_lower or 'esse é um roteiro que necessita' in line_lower or 'não podemos garantir tempo' in line_lower:
                buckets['atencao'].append(line)
            elif len(line) > 60:
                buckets['vibe'].append(line)
                
        elif state == 'cronograma':
            if current_day:
                current_day['descricao'].append(line)
        elif state == 'incluso':
            if 'investimento' not in line_lower:
                buckets['incluso'].append(line)
        elif state == 'nao_incluso':
            if 'investimento' not in line_lower:
                buckets['nao_incluso'].append(line)
        elif state == 'investimento':
            buckets['investimento'].append(line)
        elif state == 'politica':
            buckets['politica'].append(line)
        elif state == 'faq':
            buckets['faq'].append(line)
            
    for step in buckets['cronograma']:
        step['descricao'] = '\n'.join(step['descricao'])
        
    faq_list = []
    q = None
    for f in buckets['faq']:
        if '?' in f or 'quais' in f.lower() or 'como' in f.lower() or 'documentos' in f.lower():
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

url = "https://natrekking.com.br/rinoceronte"
parsed = parse_local(r'D:\rinoceronte.html')

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured = json.load(f)

structured[url] = parsed

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(structured, f, ensure_ascii=False, indent=4)

print("Parsed rinoceronte.html successfully!")
