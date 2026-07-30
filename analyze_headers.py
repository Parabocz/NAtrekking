import requests
from bs4 import BeautifulSoup

urls = [
    "https://natrekking.com.br/kilimanjaro2026",
    "https://natrekking.com.br/fendacruzdepedra"
]

for url in urls:
    print(f"\n--- {url} ---")
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    texts = []
    for p in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']):
        t = p.get_text(strip=True)
        if t and t not in texts:
            texts.append(t)
    
    # Just print potential major headers
    for t in texts:
        tl = t.lower()
        if 'incluso' in tl or 'investimento' in tl or 'politica' in tl or 'perguntas' in tl or 'cronograma' in tl or 'roteiro' in tl:
            print(t)
