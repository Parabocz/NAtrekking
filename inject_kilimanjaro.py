import json

# Load current JSON
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

url = 'https://natrekking.com.br/kilimanjaro2026'
if url not in db:
    db[url] = {}

exp = db[url]

# HISTORIA
exp['historia'] = """<p>A Tanzânia é descrita como um país de cultura rica e vida selvagem diversa. Durante a escalada do Kilimanjaro, o participante tem a chance de ver o nascer do sol do ponto mais alto da África, observar geleiras próximas à linha do equador (fenômeno raro) e contemplar a paisagem africana do topo do continente.</p>
<br>
<strong>Quem pode participar:</strong>
<ul style="margin-top: 10px; margin-left: 20px; list-style-type: disc;">
    <li>Experiência prévia em trilhas com pernoite em barraca</li>
    <li>Idade entre 18 e 65 anos (casos fora da faixa avaliados conforme saúde e condicionamento)</li>
    <li>A empresa auxilia com programa de preparação física, aclimatação e compra de aéreo</li>
    <li>Não recomendado para cardiopatas ou pessoas com limitações de mobilidade/longas caminhadas</li>
</ul>"""

# VIBE
exp['vibe'] = """<p>A expedição conta com equipe de apoio (guias locais, carregadores, cozinheiros, auxiliares). Ao chegar na Tanzânia, há revisão do equipamento do grupo, com possibilidade de locação de itens faltantes antes dos 7 dias de trekking até o Pico Uhuru (topo do Kilimanjaro).</p>"""

# TIMELINE
exp['timeline'] = """
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 1 — 04/out — Brasil → Tanzânia</h3>
        <p class="timeline-desc">Chegada no aeroporto de Kilimanjaro, recepção por representante local e transporte até a hospedagem (~50 min).</p>
        <div class="timeline-details">
            <div><strong>Incluso:</strong> transporte aeroporto-hospedagem, hospedagem compartilhada, café da manhã (dias seguintes)</div>
            <div><strong>Não incluso:</strong> alimentação (almoço/jantar), passagem aérea</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 2 — 05/out — Descanso e organização</h3>
        <p class="timeline-desc">Dia de recuperação da viagem e revisão/locação de equipamentos.</p>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 3 — 06/out — Início do trekking, Rota Lemosho</h3>
        <p class="timeline-desc">Saída da hospedagem, deslocamento até o Portão Londorossi, subida até o ponto de desembarque (3.400 m) e caminhada até o Shira 1 Camp.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.500 m → 3.610 m | Distância: 3,5 km | Tempo: 1,5h | Temp. dia: 7°C | Temp. noite: -2°C</div>
            <div><strong>Incluso:</strong> café da manhã, transporte até a trilha, almoço, jantar, barraca compartilhada, carregadores (até 15 kg)</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 4 — 07/out — Shira 1 → Shira 2</h3>
        <p class="timeline-desc">Caminhada leve com vistas das savanas e possibilidade de subir o Pico da Catedral (3.872 m, opcional). À tarde, caminhada de aclimatação até o Lava Tower Camp (ganho de 200 m).</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.610 m → 3.850 m | Distância: 10 km | Tempo: 4h | Temp. dia: 7°C | Temp. noite: -2°C</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 5 — 08/out — Shira 2 → Barranco</h3>
        <p class="timeline-desc">Caminhada até a Torre de Lava (ponto-chave para aclimatação, almoço no topo) e descida até o Acampamento Barranco, onde se avista a Muralha do Barranco.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.850 m → 3.900 m | Distância: 10 km | Tempo: 6h | Temp. dia: 7°C | Temp. noite: -2°C</div>
            <div><strong>Incluso:</strong> barraca, café, almoço, jantar</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 6 — 09/out — Barranco → Karanga</h3>
        <p class="timeline-desc">Escalada da Muralha do Barranco (~1h) seguida de trecho mais desafiador até o Karanga Camp. À tarde, caminhada de aclimatação rumo ao Barafu Camp (+200 m) com retorno ao acampamento.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.900 m → 3.995 m | Distância: 6 km | Tempo: 4h | Temp. dia: 7°C | Temp. noite: -2°C</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 7 — 10/out — Karanga → Barafu</h3>
        <p class="timeline-desc">Caminhada até o acampamento base do cume (Barafu). Caminhada de aclimatação adicional até o Kosovo Camp (4.800 m) e retorno.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.995 m → 4.673 m | Distância: 4 km | Tempo: 4h | Temp. dia: 1°C | Temp. noite: -8°C</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 8 — 11/out — Noite do Cume: Barafu → Pico Uhuru → Millennium Camp</h3>
        <p class="timeline-desc">Saída por volta da meia-noite, com equipe extra de carregadores de alta altitude e guias monitorando os participantes (chá quente, kits de primeiros socorros, oxigênio). Chegada ao Pico Uhuru (5.895 m) para o nascer do sol, ~30-40 min no topo. Descida até Barafu e, após 2h de descanso, continuação até o Millennium Camp. Aviso: 90% dos acidentes ocorrem na descida.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 4.673 m → 5.895 m → 3.950 m | Distância: 14 km | Tempo: 12,5h | Temp. dia: -8°C | Temp. noite: -17°C</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 9 — 12/out — Millennium Camp → Portão Mweka</h3>
        <p class="timeline-desc">Café da manhã e caminhada até a saída do parque (Portão Mweka), onde o transporte leva o grupo à hospedagem. Entrega do certificado da expedição.</p>
        <div class="timeline-details">
            <div><strong>Dados técnicos:</strong> Elevação: 3.950 m → 1.640 m | Distância: 13 km | Tempo: 5h | Temp. dia: 7°C | Temp. noite: -2°C</div>
            <div><strong>Incluso:</strong> transporte final, hospedagem, café da manhã</div>
        </div>
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
        <h3 class="timeline-title">Dia 10 — 13/out — Retorno ao Brasil</h3>
        <p class="timeline-desc">Fim da expedição.</p>
    </div>
</div>
"""

# ATENCAO
exp['atencao'] = """
<div class="bento-box" style="margin-bottom: 3rem; background: rgba(255,152,0,0.1); border-left: 4px solid #FF9800;">
    <h3 class="box-title" style="color: #FF9800; display: flex; align-items: center; gap: 0.5rem;">
        <i class="fas fa-exclamation-triangle"></i> Avisos Importantes
    </h3>
    <ul class="included-list">
        <li>Roteiro exige bom preparo físico; recomenda-se treino e seguir orientações antes da viagem</li>
        <li>Horários podem variar por trânsito, ritmo do grupo, clima ou decisão dos guias</li>
        <li>Grupos têm níveis físicos variados; atrativos podem ser reordenados/ajustados para segurança e melhor experiência de todos; ritmo pode ser adaptado</li>
        <li>Sempre há um guia na frente e outro atrás do grupo para manter todos próximos</li>
        <li>Condições climáticas: a empresa não garante bom tempo; cancelamento/adiamento só ocorre se houver risco de segurança ou se não atingir 10 vagas preenchidas</li>
    </ul>
</div>
"""

# INCLUSO
exp['incluso'] = """
<li>Hospedagem com café da manhã (dias 4, 5 e 12/out, quarto compartilhado)</li>
<li>Transporte aeroporto ↔ hospedagem e todos os transportes do cronograma</li>
<li>Assessoria completa pré-expedição</li>
<li>Barracas de alta montanha (capacidade 3, compartilhadas por 2 pessoas — individual mediante solicitação com 30 dias de antecedência e custo extra)</li>
<li>Pensão completa durante os 7 dias de trekking (do almoço do dia 6 ao café da manhã do dia 12)</li>
<li>Guias profissionais, assistentes, chef de cozinha e carregadores</li>
<li>Kit completo de primeiros socorros de montanha</li>
<li>Tubo de oxigênio médico</li>
<li>Equipamentos comuns (tendas, fogareiro, panelas, utensílios)</li>
<li>Comunicação VHF entre guias + GPS por guia</li>
<li>Dispositivo SpotX para rastreamento via satélite (acompanhamento por familiares/amigos online)</li>
<li>3 camisetas com proteção UV + 2 camisetas de algodão da loja NA Trekking</li>
<li>Brindes: 1 boné, 2 bandanas, 1 touca</li>
<li>2 guias NA Trekking + 1 guia local</li>
<li>Taxas de acesso</li>
<li>Cofre/armazenamento para itens que não sobem a montanha</li>
<li>Carregadores para até 15 kg de equipamento pessoal</li>
<li>Seguro internacional válido de 04 a 13/out/2026 (cotação de dias extras disponível)</li>
<li>Reuniões virtuais para tirar dúvidas</li>
"""

# EXCLUSO
exp['excluso'] = """
<li>Refeições não mencionadas no cronograma</li>
<li>Vestuário</li>
<li>Despesas de abandono da expedição, resgate e evacuação</li>
<li>Passagens aéreas</li>
<li>Alterações de hospedagem/datas solicitadas pelo cliente</li>
<li>Cobertura de resgate por helicóptero e montanhas até 6 m (obrigatório contratar antes de sair do Brasil)</li>
<li>Gorjeta para a equipe local</li>
<li>Qualquer item fora da aba "incluso"</li>
"""

# INVESTIMENTO
exp['price'] = """
<div style="font-size: 1.2rem; margin-bottom: 2rem;">
    <p>A página não exibe valores numéricos diretos, porém o investimento é negociado através do nosso atendimento oficial.</p>
</div>
<a href="https://wa.me/554799195878" class="btn-primary" style="display: inline-block;">Falar com Especialista no WhatsApp</a>
"""

# POLITICA E FAQ
exp['politica'] = """
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Política de Cancelamento</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">
        <ul style="padding-left: 20px;">
            <li>Segue a deliberação normativa nº 161 (09/08/1985) da EMBRATUR</li>
            <li>Cancelamento até 30 dias antes: reembolso de 70% do valor total</li>
            <li>Entre 29 e 21 dias antes: reembolso de 50%</li>
            <li>Entre 20 e 8 dias antes: reembolso de 40%</li>
            <li>Menos de 7 dias antes: sem devolução</li>
            <li>Força maior (clima, acesso, segurança): valor convertido em crédito para viagens futuras</li>
            <li>No-show: perda total do valor pago</li>
            <li>Desistência voluntária durante a viagem: sem reembolso, custos assumidos pelo participante</li>
            <li>Reembolsos processados em até 7 dias úteis (cartão de crédito pode levar até a próxima fatura)</li>
            <li>Aviso adicional: por causa da logística contratada (transporte, hospedagem, taxas, guia local etc.), a empresa pode reter valores de multas aplicadas por prestadores de serviço</li>
        </ul>
    </div>
</div>
"""

exp['faq'] = """
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Nível de experiência necessário</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Recomendado para iniciantes em alta montanha; subida gradual com aclimatação robusta. Sugerido ter experiência prévia em trekking no Brasil e preparo cardiovascular (bike, corrida, caminhada, futebol); pilates, musculação, crossfit e natação também ajudam.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Custos extras</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Aéreo, seguro de resgate por helicóptero (Global Rescue), visto, alimentação, gorjeta.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Documentos necessários</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Passaporte válido por 6+ meses; visto eletrônico da Tanzânia (US$ 50 padrão, US$ 100 para EUA); comprovante de passagem de retorno e hospedagem; certificado internacional de febre amarela impresso; certificado de vacina COVID impresso.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Como chegar (Voos)?</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Destino é o aeroporto de Kilimanjaro (JRO). Companhias saindo de Guarulhos: Qatar Airways (via Doha), Ethiopian Airlines (via Addis Abeba), Turkish Airlines (via Istambul), KLM (via Amsterdã). A empresa auxilia na organização.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Passagem aérea inclusa?</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Não, mas a empresa ajuda na escolha e reserva com melhor custo-benefício.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Transfer na chegada?</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Sim, representante aguarda no aeroporto com placa de identificação.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Clima esperado na montanha?</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">A expedição de início de outubro é período de transição para chuvas, com temperaturas mais baixas, possibilidade de neve e menos movimento na montanha (sem filas em gargalos).</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Divisão de barracas</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Por gênero (exceto casais); barracas para 3 pessoas divididas por 2; opção individual mediante consulta de valor.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Equipamento a carregar</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Apenas itens do dia (casaco, anorak, power bank, 2L de água, lanche); o resto (até 15 kg) é levado por carregadores.</div>
</div>
<div class="accordion-item">
    <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>Gorjeta (Tradição local)</span>
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="accordion-content">Recomendada. Faixa de US$ 250-300 entregue em envelope ao final da trilha (notas de US$ 50/100 emitidas a partir de 2009).</div>
</div>
"""

# Save JSON
with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=4, ensure_ascii=False)
print("Dados do Kilimanjaro injetados no JSON com sucesso!")
