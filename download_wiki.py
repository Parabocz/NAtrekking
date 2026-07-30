import urllib.request
import json
import os
import time

# Map filename to Wikipedia page title that has good images
wiki_pages = {
    "lencois-maranhenses-jul-2027.html": "Lençóis_Maranhenses_National_Park",
    "lencois-maranhenses-ago-2026.html": "Lençóis_Maranhenses_National_Park",
    "torres-del-paine.html": "Torres_del_Paine_National_Park",
    "curso-trekking-setembro.html": "Atlantic_Forest",
    "curso-trekking-agosto.html": "Atlantic_Forest",
    "fenda-cruz-de-pedra.html": "Itaimbezinho",
    "travessia-picos-de-jaragua.html": "Pico_Paraná", # Close enough for majestic SC/PR mountains
    "travessia-araca-x-crista.html": "Serra_do_Mar",
    "espraiado-x-soldados.html": "Serra_Geral",
    "pedra-do-cantagalo.html": "Serra_Geral"
}

public_dir = r"C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\public"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for filename, page_title in wiki_pages.items():
    print(f"Fetching images for {page_title}...")
    try:
        # Get page images in EN or PT wiki
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(page_title)}&prop=pageimages&format=json&pithumbsize=1600"
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req).read()
        data = json.loads(response)
        
        pages = data['query']['pages']
        page_id = list(pages.keys())[0]
        
        if page_id == '-1':
            # Try PT wiki
            url = f"https://pt.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(page_title)}&prop=pageimages&format=json&pithumbsize=1600"
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req).read()
            data = json.loads(response)
            pages = data['query']['pages']
            page_id = list(pages.keys())[0]

        if 'thumbnail' in pages[page_id]:
            img_url = pages[page_id]['thumbnail']['source']
            print(f"Found image: {img_url}")
            
            # Download image
            img_req = urllib.request.Request(img_url, headers=headers)
            img_data = urllib.request.urlopen(img_req).read()
            
            out_path = os.path.join(public_dir, f"wiki_{filename.replace('.html', '')}.jpg")
            with open(out_path, 'wb') as f:
                f.write(img_data)
            print(f"Saved to {out_path}")
        else:
            print("No thumbnail found.")
    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(1)
