with open('generate_unified.py', 'r', encoding='utf-8') as f:
    gen = f.read()

# Fix timeline extraction
old_timeline_logic = """    for step in buckets['cronograma']:
        step_title = step.get('titulo', 'Passo')
        step_details = step.get('detalhes', [])
        details_html = "".join(f"<li>{d}</li>" for d in step_details)"""

new_timeline_logic = """    for step in buckets['cronograma']:
        step_title = step.get('titulo', 'Passo')
        step_details = step.get('detalhes', [])
        if not step_details and 'descricao' in step:
            # Handle string with newlines if 'descricao' is used
            step_details = step['descricao'].split('\\n')
        details_html = "".join(f"<li>{d}</li>" for d in step_details)"""

gen = gen.replace(old_timeline_logic, new_timeline_logic)

# Fix FAQ extraction
old_faq_logic = """    for faq in buckets['faq']:
        q = faq.get('pergunta', '')
        a_list = faq.get('resposta', [])
        a_html = "".join(f"<p>{ans}</p>" for ans in a_list)"""

new_faq_logic = """    for faq in buckets['faq']:
        q = faq.get('pergunta', '')
        a_list = faq.get('resposta', [])
        if isinstance(a_list, str):
            a_list = [a_list]
        a_html = "".join(f"<p>{ans}</p>" for ans in a_list)"""

gen = gen.replace(old_faq_logic, new_faq_logic)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(gen)

print("generate_unified.py fixed to handle descricao and string faqs!")
