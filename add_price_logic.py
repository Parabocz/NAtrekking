import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add price_data to buckets
text = text.replace("'faq_data': [],", "'faq_data': [], 'price_data': [],")

# 2. Add price extraction logic to the loop
loop_start = "                if is_noise(line):\n                    continue"
price_extract = """
                if re.search(r'(R\\$|US\\$|USD)\\s*[\\d\\.,]+', line, re.IGNORECASE):
                    buckets['price_data'].append(line)
                    continue"""
text = text.replace(loop_start, loop_start + price_extract)

# 3. Add formatting for PRICE_CONTENT
formatting_start = "            faq_content = faq_html or \"\"\"<div class=\"accordion-item\">"
price_format = """
            if buckets['price_data']:
                price_content = "".join(f"<p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>{p}</p>" for p in buckets['price_data'])
                price_content += "<br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Garantir minha vaga</a>"
            else:
                price_content = "<p style='font-size: 1.1rem;'>Consulte nossa equipe para obter os valores e formas de pagamento atualizados.</p><br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Consultar Valores</a>"
"""
text = text.replace(formatting_start, price_format + "\n" + formatting_start)

# 4. Add template replacement for PRICE_CONTENT
replace_target = "page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_content)"
replace_price = "page_html = page_html.replace('{{ PRICE_CONTENT }}', price_content)"
text = text.replace(replace_target, replace_target + "\n        " + replace_price)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_unified.py updated for prices!")
