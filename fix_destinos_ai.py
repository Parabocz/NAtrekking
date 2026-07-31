import json
import re

with open("structured_copy.json", "r", encoding="utf-8") as f:
    sc = json.load(f)

# AI generated descriptions for destinations without history
ai_historia = {
    "https://natrekking.com.br/patagonia-especial": [
        "A Patagônia é um dos cenários mais deslumbrantes e selvagens do planeta. No extremo sul da América, glaciares imensos, montanhas pontiagudas e lagos azul-turquesa criam uma atmosfera de pura magia e imensidão.",
        "Estar na Patagônia no Réveillon é celebrar a virada cercado pela força indomável da natureza, renovando as energias diante das paisagens de Tierra del Fuego e Los Glaciares."
    ],
    "https://natrekking.com.br/patagoniachilenaespecial": [
        "A Patagônia Chilena abriga maravilhas lendárias, como as imponentes Torres del Paine. É um território de ventos fortes, montanhas dramáticas e uma energia ancestral inexplicável.",
        "A imponência da natureza local proporciona um sentimento profundo de liberdade, inspirando cada explorador a superar seus limites diante do cenário deslumbrante de lagos glaciais e fauna rica."
    ],
    "https://natrekking.com.br/calafate-chalten-especial": [
        "El Chaltén, a capital nacional do trekking na Argentina, é guardiã do mítico Cerro Fitz Roy, enquanto El Calafate abriga o espetacular Glaciar Perito Moreno.",
        "Essa região desperta o aventureiro que existe em nós. O contraste do gelo eterno caindo no lago com os picos dourados pelo sol transforma essa jornada em uma das experiências mais marcantes da vida."
    ],
    "https://natrekking.com.br/torresdelpaineo2027": [
        "O Parque Nacional Torres del Paine, no Chile, é o verdadeiro paraíso intocado. O cobiçado Circuito O revela o lado mais selvagem e remoto do parque, incluindo glaciares suspensos e florestas densas.",
        "É uma imersão total. Estar isolado na grandiosidade dos andes patagônicos é uma experiência que desafia o corpo e transforma a mente para sempre."
    ],
    "https://natrekking.com.br/travpicosdejaragua": [
        "Os picos de Jaraguá do Sul oferecem um visual privilegiado da transição entre a Serra do Mar e a costa catarinense. As montanhas escarpadas proporcionam trilhas técnicas cercadas pela rica Mata Atlântica.",
        "Respirar o ar puro no alto do Pico Boa Vista e do Jaraguá traz uma sensação única de conquista. É o cenário perfeito para se desconectar e contemplar as belezas naturais do nosso estado."
    ],
    "https://natrekking.com.br/fendacruzdepedra": [
        "Escondida na exuberante Mata Atlântica, a Fenda Cruz de Pedra é uma formação geológica impressionante e um santuário ecológico no coração de Santa Catarina.",
        "O trekking até a fenda nos insere num ambiente místico, onde o silêncio da floresta e a imponência da rocha evocam mistério e deslumbramento puro."
    ],
    "https://natrekking.com.br/curso-de-trekking-setembro": [
        "O Curso de Trekking em Rio dos Cedros é o seu portal de entrada para o mundo outdoor. A região da Represa de Rio dos Cedros (Região dos Lagos em SC) tem o cenário ideal para simular desafios e acampamentos reais.",
        "Neste curso, a paisagem se torna a sala de aula. Aqui você não apenas vê a natureza, mas aprende a conviver nela, ganhando confiança, independência e a técnica necessária para suas maiores aventuras."
    ],
    "https://natrekking.com.br/curso-de-trekking-agosto": [
        "O Curso de Trekking em Rio dos Cedros é o seu portal de entrada para o mundo outdoor. A região da Represa de Rio dos Cedros (Região dos Lagos em SC) tem o cenário ideal para simular desafios e acampamentos reais.",
        "Neste curso, a paisagem se torna a sala de aula. Aqui você não apenas vê a natureza, mas aprende a conviver nela, ganhando confiança, independência e a técnica necessária para suas maiores aventuras."
    ],
    "https://natrekking.com.br/lencois-maranhenses-jul-27": [
        "O Parque Nacional dos Lençóis Maranhenses é um espetáculo sem igual no planeta. Um oásis com dunas de areia branca interligadas por milhares de lagoas de águas doces e cristalinas que se formam após as chuvas.",
        "Fazer a travessia caminhando nas dunas causa uma epifania. A vastidão do deserto com mergulhos refrescantes diários proporciona a sensação de caminhar sobre uma pintura viva e indescritível."
    ],
    "https://natrekking.com.br/lencoismaranhensesagosto2026": [
        "O Parque Nacional dos Lençóis Maranhenses é um espetáculo sem igual no planeta. Um oásis com dunas de areia branca interligadas por milhares de lagoas de águas doces e cristalinas que se formam após as chuvas.",
        "Fazer a travessia caminhando nas dunas causa uma epifania. A vastidão do deserto com mergulhos refrescantes diários proporciona a sensação de caminhar sobre uma pintura viva e indescritível."
    ],
    "https://natrekking.com.br/rinoceronte": [
        "O Morro do Rinoceronte integra os impressionantes Campos do Quiriri, uma área de grande elevação e relevo marcante, famosa por seus nevoeiros repentinos e vistas arrebatadoras do litoral catarinense.",
        "A amplitude visual dos campos de altitude nos lembra da nossa pequenez. Acampar sob um manto de estrelas após conquistar o Rinoceronte é viver uma imersão profunda com o universo."
    ],
    "https://natrekking.com.br/torredaprata": [
        "A imponente Torre da Prata é o ponto culminante do litoral sul do Brasil (1.320m), reinando no topo da Serra da Prata, no Paraná, com um desafio de subida vertical constante na densa floresta tropical.",
        "Conquistar o cume é um atestado de resiliência. O visual que abrange a baía de Guaratuba, o Oceano Atlântico e a vastidão verde da serra traz uma gratificação que compensa cada gota de suor."
    ],
    "https://natrekking.com.br/cantagalo": [
        "A Pedra do Cantagalo é um dos tesouros escondidos de Santa Catarina. O pico oferece uma vista panorâmica incrível da floresta preservada em uma caminhada exigente, porém rápida e cativante.",
        "A energia da mata fechada combinada com o horizonte aberto lá no alto renova a alma de qualquer aventureiro, conectando corpo e mente à essência da montanha."
    ],
    "https://natrekking.com.br/espraiadoxsoldados": [
        "O Morro Boa Vista (ponto culminante de SC) e as místicas formações de arenito conhecidas como Soldados de Sebold encerram alguns dos maiores segredos do interior catarinense.",
        "Essa travessia épica de 3 dias vai testar sua força e encantar seus olhos, misturando picos gelados de altitude extrema com o encanto geológico de colunas de pedras que guardam o planalto como antigos guerreiros."
    ],
    "https://natrekking.com.br/travessiaaracaxcrista": [
        "A icônica travessia da Serra do Mar entre o Pico do Araçatuba e o sagrado Monte Crista une a fronteira do Paraná com Santa Catarina pelas cristas majestosas do Quiriri.",
        "São quilômetros caminhando por campos dourados sob céus abertos. A travessia carrega muita mística (os caminhos do Monte Crista remontam aos jesuítas e incas) e promove um autoconhecimento transformador na solidão dos ventos da serra."
    ]
}

# 1. Reverse the incorrect parser moving of "vibe" into "historia"
# In parse_expeditions.py, we moved it if historia was empty. So if a trip doesn't have an authentic "historia" (based on ai_historia keys), 
# its current "historia" is actually "vibe".
for url, data in sc.items():
    if url in ai_historia:
        # Move the content back to vibe (if it's not already in vibe, which it shouldn't be since it was moved)
        if not data.get("vibe") and data.get("historia"):
            data["vibe"] = data["historia"]
        
        # Inject AI history
        data["historia"] = ai_historia[url]

with open("structured_copy.json", "w", encoding="utf-8") as f:
    json.dump(sc, f, ensure_ascii=False, indent=2)

print("Injected AI Histories and fixed vibe logic.")
