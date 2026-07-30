import json

# 1. Read scraped data
with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\scratch\scraped_data.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

# 2. Read structured copy
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured = json.load(f)

for url in ['https://natrekking.com.br/patagonia-especial', 'https://natrekking.com.br/roraimanov2026']:
    text = scraped.get(url, '')
    lines = text.split('\n')
    
    incluso = []
    nao_incluso = []
    
    start_incluso = False
    start_nao = False
    
    for line in lines:
        line = line.strip()
        if 'Incluso no Investimento' in line or 'Incluso no investimento' in line:
            start_incluso = True
            continue
        if start_incluso:
            if 'Não incluso no investimento' in line or 'Não incluso' in line:
                start_incluso = False
                start_nao = True
                continue
            if line:
                incluso.append(line)
        if start_nao:
            # Stop conditions for Nao Incluso
            if 'Investimento' in line or 'Formas de Pagamento' in line or 'Política de Cancelamento' in line or 'Dúvidas' in line or 'Perguntas Frequentes' in line:
                break
            if line:
                nao_incluso.append(line)
                
    # Deduplicate lists but keep order
    def dedupe(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]
        
    incluso = dedupe(incluso)
    nao_incluso = dedupe(nao_incluso)
    
    if url in structured:
        structured[url]['incluso'] = incluso
        structured[url]['nao_incluso'] = nao_incluso
        print(f"Updated exhaustive lists for {url}")

# Write back
with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(structured, f, ensure_ascii=False, indent=4)
print("structured_copy.json updated.")
