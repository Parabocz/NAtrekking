import json

# Manual overrides for the missing ones to ensure perfection without regex pain
overrides = {
    "https://natrekking.com.br/kilimanjaro-safari-2027": "https://natrekking.com.br/kilimanjarosafari2026",
    "https://natrekking.com.br/lencoismaranhensesagosto2026": "https://natrekking.com.br/lencois-maranhenses-jul-27",
    "https://natrekking.com.br/curso-de-trekking-agosto": "https://natrekking.com.br/curso-de-trekking-setembro"
}

with open("structured_copy.json", "r", encoding="utf-8") as f:
    sc = json.load(f)

for target, source in overrides.items():
    if target in sc and source in sc:
        # Copy everything
        sc[target] = json.loads(json.dumps(sc[source]))

# For the small ones with missing history (1-day trips)
# 12) TRAVESSIA DOS PICOS DE JARAGUÁ
sc["https://natrekking.com.br/travpicosdejaragua"]["historia"] = ["Travessia do Pico Boa Vista para o Pico do Jaraguá."]
# 13) FENDA CRUZ DE PEDRA
sc["https://natrekking.com.br/fendacruzdepedra"]["historia"] = ["Conhecer a Fenda Cruz de Pedra."]
# 17) TORRE DA PRATA
sc["https://natrekking.com.br/torredaprata"]["historia"] = ["Conhecer a Torre da Prata."]
# 18) PEDRA DO CANTAGALO
sc["https://natrekking.com.br/cantagalo"]["historia"] = ["Conhecer a Pedra do Cantagalo."]

with open("structured_copy.json", "w", encoding="utf-8") as f:
    json.dump(sc, f, ensure_ascii=False, indent=2)

print("Fixed missing data in structured_copy.json")
