import re
with open('expedicoes/patagonia-especial-reveillon.html', 'r', encoding='utf-8') as f:
    text = f.read()

prices = re.search(r'<div class="price-container".*?</div>\s*</div>', text, flags=re.DOTALL)
if prices:
    print('PRICE CONTAINER:')
    print(prices.group(0))
else:
    print('No price container found.')
