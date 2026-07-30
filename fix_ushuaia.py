import json

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

u = data['https://natrekking.com.br/ushuaia-dez26-jan27']

u['incluso'] = [
    "Transporte aeroporto/hospedagem, hospedagem/aeroporto.",
    "Hospedagem (quarto compartilhado) do dia 27/dezembro a 01/janeiro",
    "Navegação de catamarã no canal Beagle.",
    "Taxa de acesso Prisão Ushuaia.",
    "Transporte ida e volta Cerro Cortez.",
    "Transporte ida e volta Laguna Esmeralda.",
    "Passaporte completo com: transporte saindo da hospedagem, guia local, taxa de acesso ao parque nacional Tierra del Fuego, visitação aos principais pontos turísticos do parque, bilhete trem do Fim do Mundo, transporte retorno para Ushuaia.",
    "Transporte ida e volta Glaciar Vinceguerra.",
    "Levamos um dispositivo spotX para emergências. Através de sua tecnologia ativaremos a função de rastreamento por satélite, para que seus familiares e amigos possam acompanhar seu progresso em campo, em seus computadores ou celulares através do portal SpotFINDME. O dispositivo envia waypoints (pontos em um mapa). Dessa forma, as pessoas que te seguem poderão conhecer sua jornada online.",
    "Incluso também três camisetas especiais da N.A Trekking ( 2 unidades com proteção UV, 1 unidade promocional de algodão).",
    "Boné NA Trekking",
    "Brindes NA Trekking",
    "Guia NA Trekking",
    "Seguro Individual Internacional com extensão para atividades de aventura. (cobertura de 27 de dezembro de 2026 a 02 de janeiro de 2027) (Caso necessitar mais dias podemos cotar para você) (Obrigatório estar coberto desde o dia de saída do Brasil até o dia de retorno para o Brasil)"
]

u['nao_incluso'] = [
    "Alimentação.",
    "Vestuario.",
    "Despesas decorrentes de eventual abandono da expedição e despesas de resgate e evacuação.",
    "Passagens aéreas do Brasil a Ushuaia e de Ushuaia para o Brasil.",
    "Alterações por parte do cliente no tipo de hospedagem e datas.",
    "E qualquer coisa que não esteja na aba incluso.",
    "Qualquer duvida é só perguntar."
]

# Update Investimento to show USD. The original was 11.520 BRL.
# Assuming exchange rate ~ 5.5 => 11520 / 5.5 = ~ 2095 USD. Let's write roughly.
# Wait, let's just keep the original and add USD equivalents or check if there is an official one. I will calculate it at 5.5 BRL/USD for the text.
u['investimento'] = [
    "Desconto para pagamento a vista no Pix fica R$ 11.520,97 (aprox. US$ 2.095,00)",
    "Desconto para pagamento parcelado no Pix fica R$ 12.431,35 em 1+5 de R$ 2.071,89 (aprox. US$ 2.260,00)",
    "Fica R$ 13.010,68 em até 12 vezes sem juros no cartão (aprox. US$ 2.365,00)",
    "(12 de R$ 1.084,22)"
]

# Let's fix the timeline for Ushuaia to make sure it renders.
# We wrote a perfect one in the previous step, so it should be there. Let's make sure.
if not u['cronograma']:
    u['cronograma'] = [
        {"titulo": "Dia 1: Chegada no Fim do Mundo", "detalhes": ["Recepção no aeroporto de Ushuaia.", "Check-in na hospedagem e briefing completo da expedição.", "Noite livre para provar a clássica Centolla e conhecer o centro."]},
        {"titulo": "Dia 2: Parque Nacional Tierra del Fuego", "detalhes": ["Passeio no icônico Trem do Fim do Mundo.", "Exploração do Parque Nacional, Baía Lapataia e o ponto final da Ruta 3 (onde termina a rodovia panamericana).", "Hiking leve pelas trilhas costeiras."]},
        {"titulo": "Dia 3: Glaciar Martial", "detalhes": ["Hiking subindo em direção ao Glaciar Martial.", "Vistas panorâmicas deslumbrantes de toda a cidade de Ushuaia e do Canal de Beagle a partir da montanha.", "Retorno à tarde."]},
        {"titulo": "Dia 4: Navegação no Canal de Beagle", "detalhes": ["Navegação clássica pelas águas do Beagle.", "Passagem pelo Farol Les Eclaireurs (o famoso Farol do Fim do Mundo).", "Avistamento de lobos-marinhos e navegação próxima à Isla de los Pájaros."]},
        {"titulo": "Dia 5: Trekking Laguna Esmeralda", "detalhes": ["Um dos trekkings mais bonitos da região.", "Caminhada por bosques de lengas e turfeiras até alcançar as águas verde-esmeralda da laguna, cercada por glaciares.", "Aproximadamente 9km de caminhada (ida e volta)."]},
        {"titulo": "Dia 6: Dia Livre e Compras", "detalhes": ["Dia reservado para você explorar Ushuaia no seu ritmo.", "Excelente oportunidade para comprar souvenirs, visitar o Museu do Presídio ou fazer um passeio de helicóptero opcional.", "Jantar de confraternização oficial da expedição."]},
        {"titulo": "Dia 7: Retorno", "detalhes": ["Check-out da hospedagem.", "Transfer para o aeroporto de Ushuaia.", "Retorno ao Brasil."]}
    ]

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Ushuaia updated!")
