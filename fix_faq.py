import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_faq_logic = """            FAQ_QUESTIONS = [
                'qual o nível', 'quais custos', 'quais documentos', 'quais voos',
                'passagem aérea', 'preciso de transfer', 'que dia devo chegar',
                'bagagem', 'comunicação', 'clima', 'dividir', 'equipamento',
                'abandonar', 'política de cancelamento', 'politica de cancelamento',
                'quais vacinas', 'quem pode participar'
            ]
            
            def is_faq_trigger(line):
                if line.endswith('?') and len(line) < 150:
                    return True
                ll = line.lower()
                return any(q in ll for q in FAQ_QUESTIONS)"""

new_faq_logic = """            FAQ_EXACT = ['política de cancelamento', 'politica de cancelamento', 'políticas de cancelamento']
            def is_faq_trigger(line):
                if line.endswith('?') and len(line) < 150:
                    return True
                ll = line.lower().strip()
                return any(q == ll for q in FAQ_EXACT)"""

if old_faq_logic in text:
    text = text.replace(old_faq_logic, new_faq_logic)
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("FAQ logic fixed!")
else:
    print("Old logic not found. Trying regex.")
    text = re.sub(r'FAQ_QUESTIONS = \[.*?return any\(q in ll for q in FAQ_QUESTIONS\)', new_faq_logic, text, flags=re.DOTALL)
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("FAQ logic fixed via regex!")
