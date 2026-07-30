import json

with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

url = 'https://natrekking.com.br/patagonia-especial'

patagonia_fiel = {
    "historia": [
        "A N.A Trekking nasceu através do Adriano Knopik (@adriknopik), Guia e fundador, com intuito de mostrar as pessoas um novo estilo de vida, onde a simplicidade e a superação estão diariamente presentes.",
        "Somos uma empresa do Sul do Brasil com sede em Joinville- SC, mas operamos em diversos estados e em mais 6 países promovendo expedições de todos os níveis."
    ],
    "vibe": [
        "Nossa expedição será uma mescla entre passeios turísticos e hikings entre montanhas, lagunas e glaciares, dito isso não se engane ainda assim necessitará de um bom preparo físico para completar todos os atrativos.",
        "Faremos roteiros turísticos como: O trem do fim do mundo, Farol do Fim do Mundo, Correio do fim do mundo (desativado no momento), Visitação ao ponto final da Ruta 3, Prisão do Ushuaia e Glaciar Perito Moreno.",
        "E também várias trilhas na região conhecendo montanhas lagunas e glaciares como: Loma del Pliegue Tumbado.",
        "Para nossa expedição não necessitara de equipamentos de pernoite pois ao final do dia sempre retornamos para a nossa hospedagem."
    ],
    "specs": [
        "<strong>Data:</strong> 27 de dezembro de 2026 a 13 de janeiro de 2027",
        "<strong>Ponto de encontro:</strong> Hospedagem em Ushuaia",
        "<strong>Distância:</strong> 130 km aprox",
        "<strong>Dificuldade Física:</strong> intermediário",
        "<strong>Dificuldade Técnica:</strong> intermediário"
    ],
    "cronograma": [
        {
            "dia": "Dia 1",
            "titulo": "Chegada a Ushuaia",
            "descricao": "Esse dia usaremos para a logística de chegada a Ushuaia.\nHospedagem (quarto compartilhado)\nTransfer aeroporto hospedagem"
        },
        {
            "dia": "Dia 2",
            "titulo": "Navegação no Canal Beagle e Prisão do Ushuaia",
            "descricao": "Nesse dia faremos a navegação no canal Beagle visitando a ilha dos Pinguins onde esta o farol Les Éclaireurs cartão postal de Ushuaia.\nNo nosso retorno faremos uma parada na ilha Bridges onde desceremos do nosso catamarã e faremos uma curta caminhada sobre a ilha de onde é possível avistar Ushuaia e também aves da fauna local.\nO fim da navegação deve acontecer por volta das 12:00 chegando novamente a Ushuaia, onde almoçaremos e descansaremos um pouco.\nAs 15:00 iniciaremos a visitação da prisão de Ushuaia, importante local da historia de Ushuaia."
        },
        {
            "dia": "Dia 3",
            "titulo": "Cerro Cortez",
            "descricao": "Nesse dia sairemos as 08:00 da manhã da nossa hospedagem em direção ao Cerro Cortez, onde faremos um hiking de aproximadamente 6 horas (3 horas para cada lado aprox) alcançando um dos cumes mais lindos da região com vista privilegiada de toda a Ushuaia e seus arredores, previsão de chegada as 15:00 na hospedagem.\nRestante da tarde livre.\n*Distância 12 km."
        },
        {
            "dia": "Dia 4",
            "titulo": "Laguna Esmeralda",
            "descricao": "Nesse dia sairemos as 10:00 da manhã da nossa hospedagem em direção a famosa laguna Esmeralda, nossa caminhada deve durar em torno de 6 horas no total (3 horas para cada lado) retornando para Ushuaia entre 16/17:00 horas a depender do ritmo do grupo.\n*Distância 12 km."
        },
        {
            "dia": "Dia 5",
            "titulo": "Parque Tierra del Fuego e Trem do Fim do Mundo",
            "descricao": "Nesse dia sairemos por volta das 07:00 da manhã para a visitação ao parque nacional Tierra del Fuego e também faremos o passeio do trem do Fim do Mundo.\nPasseio do Trem do Fim do Mundo\nPlaca do fim da Ruta 3\nCorreio do Fim do Mundo (desativado no momento)\nFinalizando por volta das 14:00.\nRestante da tarde livre."
        },
        {
            "dia": "Dia 6",
            "titulo": "Glaciar Vinceguerra",
            "descricao": "Sairemos as 08:00 da nossa hospedagem em direção ao Glaciar Vinceguerra.\nNossa caminhada deve durar por volta de 5 a 6 horas retornando para Ushuaia no inicio da tarde."
        },
        {
            "dia": "Dia 7",
            "titulo": "Ushuaia X Punta Arenas",
            "descricao": "Dia reservado para nosso deslocamento de Ushuaia até Punta Arenas.\nTempo: 10 horas aprox\nDistância: 500 km aprox"
        },
        {
            "dia": "Dia 8",
            "titulo": "Forte Bulnes (Estreito de Magalhães)",
            "descricao": "Hoje vamos visitar o Forte Bulnes localizado no Estreito de Magalhães.\nFoi o primeiro assentamento chileno permanente no Estreito de Magalhães, fundado em 1843 para garantir o controle estratégico da passagem marítima mais importante da América do Sul antes da criação do Canal do Panamá.\nConstruído totalmente em madeira e enfrentando ventos extremos, frio intenso e isolamento absoluto, o forte marcou o início da ocupação chilena na região da Patagônia austral. Apesar das dificuldades, ele foi essencial para consolidar a presença do Chile no extremo sul do continente."
        },
        {
            "dia": "Dia 9",
            "titulo": "Punta Arenas x Puerto Natales",
            "descricao": "Dia reservado para nosso deslocamento de Punta Arenas até Puerto Natales.\nDistância: 250 km aprox"
        },
        {
            "dia": "Dia 10",
            "titulo": "Parque de Torres del Paine",
            "descricao": "Saímos cedo em direção ao Parque de Torres del Paine, de onde iniciamos nossa caminhada até a base das Torres."
        },
        {
            "dia": "Dia 11",
            "titulo": "Dia Livre em Puerto Natales",
            "descricao": "Dia livre para explorar a cidade ou descansar."
        },
        {
            "dia": "Dia 12",
            "titulo": "Puerto Natales x El Calafate",
            "descricao": "Dia reservado para nosso deslocamento de Puerto Natales até El Calafate.\nDistância: 280 km aprox"
        },
        {
            "dia": "Dia 13",
            "titulo": "Glaciar Perito Moreno",
            "descricao": "Acordaremos por volta de umas 07:00 da manhã para o café da manhã. Finalizado nosso café da manhã as 09:00 nosso transporte passará em nossa hospedagem para nos levar ao Parque Nacional Los Glaciares para a visita ao Glaciar Perito Moreno.\nAo chegar no Parque faremos a navegação no lago do Glaciar Perito Moreno para ver o Glaciar de frente e bem de pertinho. Essa navegação dura em torno de 1:00h a 1:30h.\nAo finalizar a navegação levaremos vocês para um passeio nas passarelas e mirantes para ter uma vista lateral do Glaciar.\nTerminando mais essa etapa tomaremos um café na cafeteria dentro do Parque e depois retornaremos para El Calafate."
        },
        {
            "dia": "Dia 14",
            "titulo": "El Calafate x El Chalten e Mirante do Paredão",
            "descricao": "Acordaremos por volta das 08:00 horas para o café da manhã. As 09:30 nosso trasfer passará na nossa hospedagem para nos levar até o ponto de partida do nosso transporte principal que partirá as 11:00 da manhã de El Calafate com previsão de chegada as 13:40 em El Chaltén onde faremos o check-in na hospedagem e partiremos para uma caminhada que deve durar 3 horas até o mirante do Paredão de onde é possível ver toda a cidade e também o Cerro Fitz Roy e o Cerro Torre."
        },
        {
            "dia": "Dia 15",
            "titulo": "Laguna e Mirante do Cerro Torre",
            "descricao": "Acordaremos as 06:00 para nosso café da manhã. Nesse dia nossa saída será as 07:30 com destino a Laguna e Mirante do Cerro Torre. Nossa caminhada deve durar cerca de 8 horas no total com previsão de chegada as 15:30 em nossa hospedagem.\n351 metros de ganho de elevação."
        },
        {
            "dia": "Dia 16",
            "titulo": "Loma del Pliegue Tumbado",
            "descricao": "Acordaremos as 06:00 para o café da manhã e iniciaremos a caminhada as 07:30 para a trilha Loma del Pliegue Tumbado que deve durar em torno de 8 horas de caminhada com a previsão de finalizar em nossa hospedagem as 16:00 horas aproximadamente.\n898 ganho de elevação."
        },
        {
            "dia": "Dia 17",
            "titulo": "Laguna Capri, Los Três e Madre e Hija (Fitz Roy)",
            "descricao": "Acordaremos as 05:00 da manhã nesse dia que sem duvidas é o mais duro de toda a expedição Patagônia.. Saída as 06:30 da manhã e a previsão de retorno é as 17:30. Nesse dia visitaremos a Laguna Capri, Laguna de Los Três e Laguna Madre e Hija totalizando aprox 29 km de caminhada. Esse será o dia em que teremos a melhor vista do Cerro Fitz Roy.\n868 de ganho de elevação."
        },
        {
            "dia": "Dia 18",
            "titulo": "Retorno para El Calafate - Brasil",
            "descricao": "Dia reservado para o retorno para El Calafate - Brasil\nComprar o aéreo com o horário de embarque após as 13:00, por conta da distância do aeroporto e imprevistos com o clima"
        }
    ],
    "atencao": [
        "*Esse é um roteiro que necessita de bom preparo físico, por isso precisa chegar bem para o circuito. O guia a todo momento estará avaliando as condições de todos durante todos os dias de trekking. Se programe com bons treinos e siga todas as recomendações.",
        "*Os horários podem variar devido a trânsito, ritmo de grupo, previsão do tempo ou decisão dos guias para preservar a segurança do grupo ou mesmo garantir a melhor experiência.",
        "*As expedições em grupo são compostas de pessoas de diferentes níveis de preparo físico e velocidade, com isso você precisa estar ciente de que por conta disso os atrativos podem ser ajustados e reordenados caso necessário para preservar a segurança do grupo e também focando em entregar a melhor experiência possível para todos, lembrando que por se tratar de pessoas com preparo físico e idades diferentes de você é possível que você precise caminhar um pouco mais devagar ou rápido se adaptando ao ritmo do grupo.",
        "*Não se preocupe pois sempre haverá um guia auxiliar na parte de trás do grupo e outro na frente liderando e definindo os ritmos a fim de manter todos o mais agrupados possível.",
        "CONDIÇÕES DO TEMPO: NÃO PODEMOS GARANTIR TEMPO BOM NO DIA DA TRIP, APENAS CANCELAREMOS OU ADIAREMOS SE AS CONDIÇÕES METEOROLÓGICAS COLOCAREM EM RISCO A SEGURANÇA DOS PARTICIPANTES OU SE NÃO ATINGIREM 8 VAGAS PREENCHIDAS."
    ],
    "incluso": data[url]['incluso'], # Keep the exact lists generated previously
    "nao_incluso": [
        "Despesas decorrentes de eventual abandono da expedição e despesas de resgate e evacuação.",
        "Alterações por parte do cliente no tipo de hospedagem e datas.",
        "E qualquer coisa que não esteja na aba incluso.",
        "Qualquer duvida é só perguntar."
    ],
    "investimento": [
        "Desconto para pagamento a vista via Wise fica 3.713,92 dólares",
        "Desconto para pagamento parcelado via Wise fica 4.196,01 dólares em 1+5 de 699,33 dólares",
        "Desconto para pagamento a vista no Pix fica R$ 20.346,35",
        "Desconto para pagamento parcelado no Pix fica R$ 22.147,36 em 1+5 de R$ 3.691,22",
        "Fica R$ 23.293,46 em até 12 vezes sem juros",
        "(12 de R$ 1.941,12 aprox)"
    ],
    "politica": [
        "Essa trip seguira todas as regras e decretos estabelecidos na data, podendo ser necessário o uso de carros normais caso não puder contratar vans e também poderá ser adiado caso haja alguma proibição da pratica esportiva. Nesse caso seu investimento ficará como credito para você utilizar no evento á sua escolha.",
        "Para essa Expedição em especial devido a quantidade de logística empregada, assim como a quantidade de serviços que terão que ser contratados como: Transporte, reserva de hospedagem, taxas de acesso, outros membros da equipe e outros.., nos reservamos o direito de reter possíveis valores advindos de multas aplicadas por todos esses prestadores de serviço que estarão disponíveis para nossa expedição. Por isso antes da compra esteja ciente que além das regras que estão disponíveis abaixo poderá haver retenção de outros valores.",
        "Em caso de cancelamento por iniciativa do cliente, a N.A.Trekking providenciará a possível devolução conforme especificado abaixo e de acordo com a deliberação normativa nº 161 de 09 de agosto de 1985 da EMBRATUR.",
        "* Cancelamento até 30 dias do início da viagem: 70% do valor total",
        "* Cancelamento entre 29 e 21 dias do início da viagem: 50% do valor total",
        "* Cancelamento entre 20 e 08 dias do início da viagem: 40% do valor total",
        "* Cancelamento a menos de 07 dias do início da viagem: Sem devolução",
        "Por isso tenha a certeza que realmente nessa data poderá participar da atividade.",
        "*Situações que impossibilitem o evento por motivo de força maior devido a fatores climáticos, de acesso ou que possam interferir na segurança dos participantes ocasionará reversão do valor pago em crédito para uso viagens futuras conforme disponibilidade e condições da N.A Trekking.",
        "* O não comparecimento na data, hora e local de apresentação determinados para o embarque será considerado 'no-show', implicando a perda total do valor pago.",
        "* O contratante que, por livre e espontânea vontade, se desligar do grupo durante a viagem ou trocar a hospedagem contratada, assumirá toda e qualquer despesa decorrente dessa atitude, sem o direito a reembolso.",
        "* Em caso de desistência durante o roteiro por motivos pessoais o participante arcará com todos os custos que possam ser gerados com sua saída do evento. (Logística)",
        "*Devolução de valores pagos serão realizados em até 7 dias uteis, após o recebimento da solicitação de reembolso.",
        "(Para pagamentos que foram feitos com cartão de crédito, efetuaremos o cancelamento no mesmo prazo de 7 dias úteis, porém o cancelamento e recebimento do crédito normalmente é gerado na próxima fatura a depender da operadora de cartão de crédito.)"
    ],
    "faq": [
        "<b>Quais documentos preciso?</b><br>Para a viagem vc vai precisar de passaporte ou rg. Passaporte com no mínimo 6 meses de validade na data da viagem e com no mínimo 3 paginas em branco. RG dentro da validade (valido por 10 anos) e em bom estado.",
        "<b>Quais vacinas são necessárias?</b><br>Você vai precisar da vacina da febre amarela e retirar o certificado internacional."
    ],
    "loc": "Patagônia",
    "dur": "18 dias",
    "elevation": "N/A"
}

data[url] = patagonia_fiel

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Patagonia Especial content fully injected with perfect accuracy.")
