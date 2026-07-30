import re
with open('expedicoes/ushuaia.html', 'r', encoding='utf-8') as f:
    text = f.read()

timeline = re.search(r'<div class="timeline-container".*?</div>\s*</div>\s*</div>', text, flags=re.DOTALL)
if timeline:
    print('TIMELINE CONTENT:')
    print(timeline.group(0))
else:
    print('Timeline not found with regex.')
