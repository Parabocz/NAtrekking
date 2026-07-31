import re
import json

with open("expedicoes_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Load existing structured copy
with open("structured_copy.json", "r", encoding="utf-8") as f:
    structured = json.load(f)

blocks = re.split(r'#{60,}', text)
expeditions = []

for i in range(len(blocks) - 1):
    header_block = blocks[i].strip()
    content_block = blocks[i+1].strip()
    
    url_match = re.search(r'URL:\s*natrekking\.com\.br/([^\n\s]+)', header_block)
    if not url_match:
        continue
        
    url = "https://natrekking.com.br/" + url_match.group(1).strip()
    
    data = {
        "historia": [],
        "vibe": [],
        "specs": [],
        "cronograma": [],
        "atencao": [],
        "incluso": [],
        "nao_incluso": [],
        "investimento": [],
        "politica": [],
        "faq": []
    }
    
    sections = re.split(r'\n(?=O QUE ESPERAR DESSA VIAGEM|HISTÓRIA|COMO VAI ROLAR|PARA QUEM É / O QUE VAMOS APRENDER|DADOS DA EXPEDIÇÃO|CRONOGRAMA|ATENÇÃO|INCLUSO NO INVESTIMENTO|INCLUSO/NÃO INCLUSO|NÃO INCLUSO|INVESTIMENTO|POLÍTICA DE CANCELAMENTO|FAQ)', content_block)
    
    for sec in sections:
        sec = sec.strip()
        if not sec: continue
        
        lines = [line.strip() for line in sec.split('\n') if line.strip()]
        if not lines: continue
        
        header = lines[0]
        content = "\n".join(lines[1:])
        
        if header.startswith("O QUE ESPERAR DESSA VIAGEM") or header.startswith("HISTÓRIA"):
            data["historia"] = [p for p in content.split('\n\n') if p.strip()]
        elif header.startswith("COMO VAI ROLAR") or header.startswith("PARA QUEM É / O QUE VAMOS APRENDER"):
            data["vibe"] = [p for p in content.split('\n\n') if p.strip()]
            if not data["historia"]:
                data["historia"] = data["vibe"]
                data["vibe"] = []
        elif header.startswith("CRONOGRAMA"):
            crono_items = re.split(r'\n(?=Dia|Sábado|Domingo|04:30|04:00|07:00|23:00)', content)
            for item in crono_items:
                item = item.strip()
                if not item: continue
                parts = item.split('—', 1)
                if len(parts) > 1:
                    titulo = parts[0].strip()
                    desc = parts[1].strip()
                else:
                    titulo = "Dia"
                    desc = item
                data["cronograma"].append({
                    "titulo": titulo,
                    "descricao": desc,
                    "icon": "fa-map-marker-alt"
                })
        elif header.startswith("ATENÇÃO"):
            data["atencao"] = [line.replace('- ', '').strip() for line in content.split('\n') if line.strip()]
        elif header.startswith("INCLUSO NO INVESTIMENTO"):
            items = [i.strip() for i in content.replace(';', '\n').split('\n') if i.strip()]
            data["incluso"] = items
        elif header.startswith("NÃO INCLUSO"):
            items = [i.strip() for i in content.replace(';', '\n').split('\n') if i.strip()]
            data["nao_incluso"] = items
        elif header.startswith("INCLUSO/NÃO INCLUSO"):
            data["incluso"] = [content]
            data["nao_incluso"] = [content]
        elif header.startswith("INVESTIMENTO"):
            if "Não há valores" not in content and "não exibido" not in content.lower():
                data["investimento"] = [p for p in content.split('\n') if p.strip()]
        elif header.startswith("POLÍTICA DE CANCELAMENTO"):
            data["politica"] = [line.strip() for line in content.split('\n') if line.strip()]
        elif header.startswith("FAQ"):
            faq_items = re.split(r'\n(?=-)', content)
            for item in faq_items:
                if not item.strip(): continue
                item = item.strip().lstrip('-').strip()
                parts = item.split(':', 1)
                if len(parts) == 2:
                    data["faq"].append({"pergunta": parts[0].strip(), "resposta": [parts[1].strip()]})
                else:
                    data["faq"].append({"pergunta": "Informação", "resposta": [item]})

    structured[url] = data

with open("structured_copy.json", "w", encoding="utf-8") as f:
    json.dump(structured, f, ensure_ascii=False, indent=2)

print("Parsed and updated structured_copy.json")
