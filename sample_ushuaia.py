import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

u = data['https://natrekking.com.br/ushuaia-dez26-jan27']

print('--- HISTÓRIA ---')
for p in u['historia']: print(p)

print('\n--- VIBE ---')
for p in u['vibe']: print(p)

print('\n--- SPECS ---')
for p in u['specs']: print(p)

print('\n--- CRONOGRAMA ---')
for item in u['cronograma']:
    print(f"{item['titulo']} -> {len(item['detalhes'])} detalhes")

print('\n--- INCLUSO ---')
print(f"{len(u['incluso'])} itens")

print('\n--- INVESTIMENTO ---')
for p in u['investimento']: print(p)

print('\n--- FAQ ---')
for item in u['faq']: print(f"{item['pergunta']} -> {len(item['resposta'])} parágrafos de resposta")
