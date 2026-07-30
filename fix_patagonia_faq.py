import json

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

url = 'https://natrekking.com.br/patagonia-especial'

data[url]["faq"] = [
    {
        "pergunta": "Quais documentos preciso?",
        "resposta": "Para a viagem vc vai precisar de passaporte ou rg. Passaporte com no mínimo 6 meses de validade na data da viagem e com no mínimo 3 paginas em branco. RG dentro da validade (valido por 10 anos) e em bom estado."
    },
    {
        "pergunta": "Quais vacinas são necessárias?",
        "resposta": "Você vai precisar da vacina da febre amarela e retirar o certificado internacional."
    }
]

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("FAQ fixed in Patagonia Especial.")
