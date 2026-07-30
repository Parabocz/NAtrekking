import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract the pieces we need
bento_intro = re.search(r'(<div class="bento-box bento-intro">.*?</div>\s*</div>)', text, flags=re.DOTALL)
# Wait, the end of bento-intro is just </div>.
# Let's just use regex for the whole bento-grid and timeline-container

bento_grid_match = re.search(r'<div class="bento-grid">(.*?)</div>\s*<div class="timeline-container">', text, flags=re.DOTALL)
timeline_match = re.search(r'<div class="timeline-container">.*?</div>\s*</div>\s*<div class="faq-container">', text, flags=re.DOTALL)

# Let's just split the string directly by searching for the class names
# and parsing it carefully.
