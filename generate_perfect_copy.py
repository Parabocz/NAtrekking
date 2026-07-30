import json

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. USHUAIA
data['https://natrekking.com.br/ushuaia-dez26-jan27'] = {
    "historia": [
        "Ushuaia é a mítica cidade do 'Fim do Mundo', cravada no extremo sul da Patagônia Argentina, no arquipélago da Terra do Fogo. Uma terra de belezas extremas e paisagens dramáticas.",
        "Cercada pela imponente Cordilheira Martial de um lado e pelas águas gélidas do Estreito de Beagle do outro, a cidade oferece um cenário perfeito onde montanhas nevadas se encontram com o oceano. É também a porta de entrada clássica para a Antártida."
    ],
    "vibe": [
        "Nossa expedição em Ushuaia foi desenhada para mesclar o melhor do turismo clássico patagônico com a verdadeira essência aventureira da N.A Trekking.",
        "Você viverá dias intensos explorando lagunas de cores surreais, caminhando sobre glaciares milenares e navegando pelo Estreito de Beagle. Embora tenhamos todo o conforto de retornar para a cidade no fim do dia, os hikings exigirão um preparo físico moderado para que você possa aproveitar 100% de cada atrativo natural."
    ],
    "specs": [
        "<strong>Data:</strong> 27 de dezembro de 2026 a 02 de janeiro de 2027",
        "<strong>Duração:</strong> 7 dias e 6 noites",
        "<strong>Dificuldade:</strong> Moderada",
        "<strong>Ponto de Encontro:</strong> Aeroporto de Ushuaia (USH)"
    ],
    "cronograma": [
        {"titulo": "Dia 1: Chegada no Fim do Mundo", "detalhes": ["Recepção no aeroporto de Ushuaia.", "Check-in na hospedagem e briefing completo da expedição.", "Noite livre para provar a clássica Centolla e conhecer o centro."]},
        {"titulo": "Dia 2: Parque Nacional Tierra del Fuego", "detalhes": ["Passeio no icônico Trem do Fim do Mundo.", "Exploração do Parque Nacional, Baía Lapataia e o ponto final da Ruta 3 (onde termina a rodovia panamericana).", "Hiking leve pelas trilhas costeiras."]},
        {"titulo": "Dia 3: Glaciar Martial", "detalhes": ["Hiking subindo em direção ao Glaciar Martial.", "Vistas panorâmicas deslumbrantes de toda a cidade de Ushuaia e do Canal de Beagle a partir da montanha.", "Retorno à tarde."]},
        {"titulo": "Dia 4: Navegação no Canal de Beagle", "detalhes": ["Navegação clássica pelas águas do Beagle.", "Passagem pelo Farol Les Eclaireurs (o famoso Farol do Fim do Mundo).", "Avistamento de lobos-marinhos e navegação próxima à Isla de los Pájaros."]},
        {"titulo": "Dia 5: Trekking Laguna Esmeralda", "detalhes": ["Um dos trekkings mais bonitos da região.", "Caminhada por bosques de lengas e turfeiras até alcançar as águas verde-esmeralda da laguna, cercada por glaciares.", "Aproximadamente 9km de caminhada (ida e volta)."]},
        {"titulo": "Dia 6: Dia Livre e Compras", "detalhes": ["Dia reservado para você explorar Ushuaia no seu ritmo.", "Excelente oportunidade para comprar souvenirs, visitar o Museu do Presídio ou fazer um passeio de helicóptero opcional.", "Jantar de confraternização oficial da expedição."]},
        {"titulo": "Dia 7: Retorno", "detalhes": ["Check-out da hospedagem.", "Transfer para o aeroporto de Ushuaia.", "Retorno ao Brasil."]}
    ],
    "atencao": [
        "A Patagônia é famosa por suas quatro estações no mesmo dia. Espere por ventos fortíssimos e clima imprevisível.",
        "Mesmo sendo verão, as temperaturas podem chegar próximas de 0ºC. Um sistema de camadas eficiente (Anorak, Fleece, Segunda Pele) é obrigatório."
    ],
    "incluso": [
        "Hospedagem em Ushuaia durante todos os dias da expedição.",
        "Todos os transfers terrestres locais para as atividades descritas.",
        "Bilhete para o Trem do Fim do Mundo e taxas de entrada no Parque Nacional Tierra del Fuego.",
        "Navegação completa pelo Canal de Beagle.",
        "Guias locais experientes e guias brasileiros da N.A Trekking acompanhando o grupo desde o Brasil.",
        "Rastreamento via satélite SPOT X para segurança e acompanhamento por familiares.",
        "Seguro Viagem Internacional de Aventura (GTA ou similar).",
        "Kit N.A Trekking com 3 camisetas (2 UV e 1 algodão)."
    ],
    "nao_incluso": [
        "Passagens Aéreas.",
        "Alimentação (Almoço, Jantar e lanches de trilha).",
        "Passeios extras opcionais durante o dia livre.",
        "Equipamentos de uso pessoal e vestuário."
    ],
    "investimento": data['https://natrekking.com.br/ushuaia-dez26-jan27']['investimento'],
    "politica": [
        "Em caso de cancelamento por iniciativa do cliente, a devolução será feita de acordo com a deliberação normativa nº 161 da EMBRATUR.",
        "Condições climáticas que impeçam a realização de alguma atividade não gerarão reembolso, mas tentaremos realocar a atividade conforme disponibilidade.",
        "No-show no ponto de encontro implica perda de 100% do valor pago."
    ],
    "faq": [
        {"pergunta": "Qual o nível de dificuldade física?", "resposta": ["Nossa classificação é moderada. Caminharemos por terrenos irregulares, bosques e turfeiras. Não há necessidade de experiência prévia com alta montanha, mas recomendamos que você tenha o costume de praticar atividades físicas regularmente."]},
        {"pergunta": "Quais documentos preciso para entrar na Argentina?", "resposta": ["Brasileiros podem viajar para a Argentina apenas com o RG (Identidade) emitido há menos de 10 anos, em bom estado de conservação, ou Passaporte válido.", "CNH (Carteira de Motorista) não é aceita como documento de imigração."]}
    ]
}

# 2. PATAGONIA ESPECIAL
data['https://natrekking.com.br/patagonia-especial'] = {
    "historia": [
        "A Expedição Patagônia Especial (Réveillon) é a nossa obra-prima. Um roteiro desenhado minuciosamente para cruzar as fronteiras da Argentina e do Chile durante a virada do ano, reunindo em uma única viagem os maiores ícones do fim do mundo.",
        "De Ushuaia a Torres del Paine, e culminando na capital nacional do trekking, El Chaltén. Prepare-se para viver a magnitude indomável da natureza patagônica."
    ],
    "vibe": [
        "Essa é uma expedição de longa duração (18 dias) feita para viajantes que desejam uma imersão completa sem precisar se preocupar com a complexa logística de transportes e fronteiras da região.",
        "Nossa vibe será um balanço entre a contemplação de geleiras estrondosas a partir de passarelas e trekkings intensos e desafiadores, como a trilha até a base do imponente Fitz Roy. Celebraremos a chegada do ano novo em um dos cenários mais épicos da Terra."
    ],
    "specs": [
        "<strong>Data:</strong> 27 de dezembro de 2026 a 13 de janeiro de 2027",
        "<strong>Duração:</strong> 18 dias",
        "<strong>Dificuldade:</strong> Alta (Trekkings longos em El Chaltén)",
        "<strong>Ponto de Encontro:</strong> Ushuaia (Início) / El Calafate (Término)"
    ],
    "cronograma": [
        {"titulo": "Etapa 1: O Fim do Mundo (Ushuaia)", "detalhes": ["Chegada em Ushuaia, navegação no Canal de Beagle.", "Parque Nacional Tierra del Fuego e Trem do Fim do Mundo.", "Hiking ao Glaciar Martial e Laguna Esmeralda.", "Reveillon em Ushuaia!"]},
        {"titulo": "Etapa 2: A Fronteira (Punta Arenas e Natales)", "detalhes": ["Cruze de fronteira em ônibus cortando as estepes patagônicas.", "Chegada no Chile, explorando Puerto Natales e Punta Arenas."]},
        {"titulo": "Etapa 3: Torres del Paine", "detalhes": ["Exploração das paisagens incríveis do Parque Nacional Torres del Paine.", "Mirantes clássicos, lagos azuis e avistamento da fauna local (Guanacos, Condores)."]},
        {"titulo": "Etapa 4: Glaciar Perito Moreno", "detalhes": ["Retorno à Argentina com chegada em El Calafate.", "Visitação ao monumental Glaciar Perito Moreno.", "Tempo livre para observar o desprendimento de gelo e passadiços."]},
        {"titulo": "Etapa 5: O Desafio de El Chaltén", "detalhes": ["Transfer para El Chaltén, a capital nacional do trekking.", "Trekking desafiador até a Laguna de los Tres (Base do Monte Fitz Roy).", "Trekking até a Laguna Torre (Visão do Cerro Torre).", "Retorno para El Calafate e voo de volta ao Brasil."]}
    ],
    "atencao": [
        "Esta é uma viagem longa que exigirá transições em estradas e cruzamentos de fronteiras terrestres. Paciência é essencial.",
        "Os dias de trekking em El Chaltén são fisicamente muito exigentes, totalizando até 20km de caminhada por dia com ganho de elevação significativo."
    ],
    "incluso": [
        "Hospedagem em todas as cidades do roteiro.",
        "Toda a logística de transporte rodoviário entre Ushuaia, Natales, Calafate e Chaltén.",
        "Guias acompanhantes e taxas de entrada nos Parques Nacionais (Tierra del Fuego, Torres del Paine, Los Glaciares).",
        "Passeios em Ushuaia (Beagle, Trem).",
        "Dispositivo de rastreamento SPOT X e Seguro Aventura.",
        "Kit Oficial N.A Trekking (Camisetas)."
    ],
    "nao_incluso": [
        "Passagens Aéreas de ida e volta.",
        "Alimentação em geral.",
        "Atividades extras (ex: Trekking sobre o gelo no Perito Moreno).",
        "Custos extras decorrentes de imprevistos em fronteiras."
    ],
    "investimento": data['https://natrekking.com.br/patagonia-especial']['investimento'],
    "politica": [
        "Condições de devolução padrão da EMBRATUR.",
        "Em caso de atrasos nos ônibus de fronteira por questões climáticas, os custos adicionais de remarcação são de responsabilidade do passageiro."
    ],
    "faq": [
        {"pergunta": "Preciso ser atleta para ir?", "resposta": ["Não é necessário ser um atleta de elite, mas os dias em El Chaltén exigem muito. Se você não possui condicionamento para caminhar 20km em montanha, poderá optar por não fazer as trilhas mais duras em Chaltén e curtir a cidade ou trilhas leves."]},
        {"pergunta": "Como funciona o clima em dezembro/janeiro?", "resposta": ["É verão, o que significa muitas horas de sol (anoitece por volta de 22h). Porém, na Patagônia, as temperaturas ainda variam de 5ºC a 18ºC e os ventos podem ser extremos. O uso de Anorak é inegociável."]}
    ]
}

# 3. MONTE RORAIMA
data['https://natrekking.com.br/roraimanov2026'] = {
    "historia": [
        "O Monte Roraima é um gigantesco Tepui (montanha em formato de mesa) que se ergue imponente acima das nuvens na tríplice fronteira entre Brasil, Venezuela e Guiana.",
        "Conhecido como o 'Mundo Perdido' que inspirou Arthur Conan Doyle, caminhar em seu topo é como pisar em um planeta alienígena: rios de cristais, formações rochosas ancestrais que não existem em nenhum outro lugar da Terra e uma energia inexplicável."
    ],
    "vibe": [
        "Diferente de roteiros turísticos, a Expedição Monte Roraima é um trekking de resistência, imersão total na selva e desconexão completa.",
        "Você viverá lado a lado com os indígenas Pemon, que cuidam de toda a logística e carregam os equipamentos coletivos. Aqui não há luxo, não há sinal de internet e não há banho quente. Há apenas você, a comunidade, o silêncio da Gran Sabana e a força bruta da montanha."
    ],
    "specs": [
        "<strong>Data:</strong> 20 a 29 de novembro de 2026",
        "<strong>Duração:</strong> 10 dias (6 de trekking)",
        "<strong>Dificuldade:</strong> Alta (Trekking de Resistência)",
        "<strong>Elevação:</strong> 2.810m (Topo do Tepui)"
    ],
    "cronograma": [
        {"titulo": "Dia 1: Chegada em Boa Vista e Fronteira", "detalhes": ["Recepção no aeroporto de Boa Vista (RR) pela manhã.", "Transfer de van até a fronteira com a Venezuela e trâmites de imigração.", "Chegada em Santa Elena de Uairén, check-in no hotel e briefing com os guias locais."]},
        {"titulo": "Dia 2: O Início do Caminho (Paraitepuy > Rio Tek)", "detalhes": ["Transfer em veículos 4x4 até a comunidade indígena de Paraitepuy.", "Início do trekking. Caminhada suave pelas colinas da Gran Sabana.", "Travessia de rios e chegada ao Acampamento Rio Tek para a primeira noite em barracas."]},
        {"titulo": "Dia 3: Acampamento Base", "detalhes": ["Caminhada até o Acampamento Base do Monte Roraima.", "O tepui gigante começa a se agigantar na nossa frente. Pernoite na base da montanha."]},
        {"titulo": "Dia 4: A Rampa e o Mundo Perdido", "detalhes": ["O dia mais desafiador. Subida íngreme através da densa floresta úmida pela 'Rampa'.", "Chegada ao topo do Monte Roraima.", "Acomodação nos chamados 'Hotéis' (cavernas naturais onde montamos o acampamento)."]},
        {"titulo": "Dias 5, 6 e 7: Explorando o Topo", "detalhes": ["Três dias inteiros isolados no topo do tepui.", "Visitaremos o Valle de los Cristales, a Tríplice Fronteira (marco geográfico), os Jacuzzis naturais e o mirante La Ventana.", "Banho em águas cristalinas (e congelantes)."]},
        {"titulo": "Dia 8: A Descida", "detalhes": ["Despedida do topo e início da descida intensa até o Acampamento Rio Tek.", "Caminhada de cerca de 14km ladeira abaixo."]},
        {"titulo": "Dia 9: Retorno a Santa Elena", "detalhes": ["Último trecho de trekking até Paraitepuy.", "Almoço de celebração e transfer 4x4 de volta para o hotel em Santa Elena de Uairén."]},
        {"titulo": "Dia 10: Retorno", "detalhes": ["Transfer de Santa Elena até o aeroporto de Boa Vista (RR).", "Fim da expedição e voos de retorno."]}
    ],
    "atencao": [
        "A Vacina de Febre Amarela (com Certificado Internacional de Vacinação) é estritamente obrigatória para entrar na Venezuela.",
        "Não existe resgate de helicóptero no Monte Roraima. Você estará isolado em uma região extrema, exigindo resiliência mental absurda."
    ],
    "incluso": [
        "Transfers de Boa Vista a Santa Elena e até a Comunidade de Paraitepuy em veículos 4x4.",
        "Hospedagem em hotel em Santa Elena de Uairén (primeira e última noite).",
        "Toda a alimentação durante os 6 dias de trekking (café da manhã, almoço leve/trilha, jantares quentes).",
        "Guias locais indígenas e guia da N.A Trekking.",
        "Carregadores indígenas para barracas e equipamentos coletivos.",
        "Kit de Primeiros Socorros e Seguro Aventura."
    ],
    "nao_incluso": [
        "Passagens Aéreas até Boa Vista.",
        "Alimentação nas cidades (Boa Vista e Santa Elena).",
        "Carregador pessoal (caso não queira levar a própria mochila, é possível contratar um carregador à parte, custo aproximado de R$ 600).",
        "Saco de dormir e isolante térmico (locação opcional)."
    ],
    "investimento": [],
    "politica": [
        "Pelas regras locais e instabilidades de fronteira, se houver o fechamento imprevisível da fronteira venezuelana, o roteiro poderá sofrer adaptações extremas ou ser convertido em crédito.",
        "Políticas de cancelamento padrão N.A Trekking aplicáveis."
    ],
    "faq": [
        {"pergunta": "Qual o peso que terei que carregar na mochila?", "resposta": ["Se você não contratar um carregador pessoal, levará sua mochila cargueira com todo seu vestuário, saco de dormir, isolante e lanches pessoais (cerca de 10 a 14kg). O ideal é levar o mínimo possível."]},
        {"pergunta": "Como é a comida na montanha?", "resposta": ["Nossos cozinheiros preparam refeições incrivelmente saborosas em campo. Teremos desde arepas típicas no café da manhã até macarrão, carnes e sopas ricas em carboidratos à noite para recuperação."]},
        {"pergunta": "E o banheiro?", "resposta": ["No Monte Roraima usamos 'banheiros ecológicos'. É montada uma pequena tenda afastada do acampamento com um assento e sacos ecológicos contendo cal. Toda a cal e detritos retornam à civilização, mantendo o topo sagrado impecável."]}
    ]
}

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Copy perfeita gerada para Ushuaia, Patagonia Especial e Roraima!")
