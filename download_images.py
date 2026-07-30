import urllib.request
from duckduckgo_search import DDGS
import time
import os

queries = {
    "lencois-maranhenses-jul-2027.html": "Lençois Maranhenses landscape high resolution",
    "lencois-maranhenses-ago-2026.html": "Lençois Maranhenses sunset landscape high resolution",
    "torres-del-paine.html": "Torres del Paine mountain landscape high resolution",
    "curso-trekking-setembro.html": "hiking trail forest high resolution landscape",
    "curso-trekking-agosto.html": "trekking camping landscape high resolution",
    "fenda-cruz-de-pedra.html": "canyon green forest landscape high resolution",
    "travessia-picos-de-jaragua.html": "green mountains brazil landscape high resolution",
    "travessia-araca-x-crista.html": "serra do mar trail high resolution landscape",
    "espraiado-x-soldados.html": "canion espraiado santa catarina landscape",
    "pedra-do-cantagalo.html": "mountain peak forest sunset high resolution landscape"
}

public_dir = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\public"
ddgs = DDGS()

for filename, query in queries.items():
    print(f"Searching for {query}...")
    try:
        results = ddgs.images(
            keywords=query,
            region="wt-wt",
            safesearch="moderate",
            size="Large",
            color="color",
            type_image="photo",
            layout="Wide",
            max_results=3
        )
        
        saved = False
        for res in results:
            url = res['image']
            print(f"  Found {url}")
            try:
                # User-agent is required for some sites
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                img_data = urllib.request.urlopen(req, timeout=10).read()
                
                out_path = os.path.join(public_dir, f"dl_{filename.replace('.html', '')}.jpg")
                with open(out_path, 'wb') as f:
                    f.write(img_data)
                print(f"  Saved to {out_path}")
                saved = True
                break
            except Exception as e:
                print(f"  Failed to download: {e}")
                
        if not saved:
            print("  Could not save any image for this query.")
    except Exception as e:
        print(f"Error searching for {query}: {e}")
        
    time.sleep(2)
