import json
import re

with open("expedicoes_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("structured_copy.json", "r", encoding="utf-8") as f:
    sc = json.load(f)

blocks = re.split(r'#{60,}', text)

padrao_atencao = [
    "Exige bom preparo físico; guia avalia condições diariamente.",
    "Horários podem variar (trânsito, clima, ritmo do grupo, decisão dos guias).",
    "Atrativos podem ser reordenados para segurança/melhor experiência.",
    "Sempre há guia na frente e atrás do grupo.",
    "Sem garantia de bom tempo; cancelamento só por risco de segurança."
]

for i in range(len(blocks) - 1):
    header_block = blocks[i].strip()
    content_block = blocks[i+1].strip()
    
    url_match = re.search(r'URL:\s*natrekking\.com\.br/([^\n\s]+)', header_block)
    if not url_match:
        continue
        
    url = "https://natrekking.com.br/" + url_match.group(1).strip()
    
    if url not in sc:
        continue
        
    data = sc[url]
    
    # 1. Update Atenção
    atencao_text = "\n".join(data.get("atencao", []))
    if not atencao_text or "padrão" in atencao_text.lower():
        # prepend or replace with standard
        # the previous parser just put "padrão." or similar. Let's merge them.
        data["atencao"] = padrao_atencao + [a for a in data.get("atencao", []) if "padrão" not in a.lower()]

    # 2. Extract Meta info
    dados_match = re.search(r'(?m)^DADOS DA EXPEDIÇÃO\n(.*?)(?=\n[A-Z]{3,}|$)', content_block, re.DOTALL)
    if dados_match:
        dados_text = dados_match.group(1)
        
        # Distancia
        dist = re.search(r'Distância:\s*([^\|\n]+)', dados_text)
        if dist:
            data["distancia"] = dist.group(1).strip()
            
        # Elevacao (Ganho/Perda or Elevacao)
        elev = re.search(r'Ganho(?:/perda)?\s*de elevação:\s*([^\|\n]+)', dados_text, re.IGNORECASE)
        if elev:
            data["elevacao_ganho"] = elev.group(1).strip()
        
        # Dificuldade Física
        dif_fisica = re.search(r'Dificuldade\s*física(?:\/técnica| trekking)?:\s*([^\|\n]+)', dados_text, re.IGNORECASE)
        if dif_fisica:
            data["dif_fisica"] = dif_fisica.group(1).strip()
        else:
            # Maybe just Dificuldade:
            dif = re.search(r'Dificuldade:\s*([^\|\n]+)', dados_text, re.IGNORECASE)
            if dif:
                data["dif_fisica"] = dif.group(1).strip()
            
        # Dificuldade Técnica
        dif_tecnica = re.search(r'Técnica:\s*([^\|\n]+)', dados_text, re.IGNORECASE)
        if dif_tecnica:
            data["dif_tecnica"] = dif_tecnica.group(1).strip()
        elif re.search(r'física/técnica:\s*([^\|\n]+)', dados_text, re.IGNORECASE):
            data["dif_tecnica"] = dif_fisica.group(1).strip()

with open("structured_copy.json", "w", encoding="utf-8") as f:
    json.dump(sc, f, ensure_ascii=False, indent=2)

print("Updated structured_copy.json with Meta and Atenção.")
