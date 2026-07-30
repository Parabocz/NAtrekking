import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to find the <section class="bento-section">...</section> and <section class="timeline-section">...</section>
# Since regex might fail if there are nested tags, let's use string operations

bento_start = text.find('<section class="bento-section">')
bento_end = text.find('</section>', bento_start) + 10

timeline_start = text.find('<section class="timeline-section">')
timeline_end = text.find('</section>', timeline_start) + 10

if bento_start != -1 and timeline_start != -1:
    bento_html = text[bento_start:bento_end]
    timeline_html = text[timeline_start:timeline_end]
    
    price_html = '''
    <section class="price-section" style="margin-top: 4rem;">
        <div class="container">
            <h2 class="section-title">Valores da Expedição</h2>
            <div class="price-container" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 2rem;">
                {{ PRICE_CONTENT }}
            </div>
        </div>
    </section>
    '''
    
    # The order in file right now is bento then timeline.
    if bento_start < timeline_start:
        new_text = text[:bento_start] + timeline_html + "\n" + text[bento_end:timeline_start] + bento_html + "\n" + price_html + "\n" + text[timeline_end:]
    else:
        new_text = text[:timeline_start] + timeline_html + "\n" + text[timeline_end:bento_start] + bento_html + "\n" + price_html + "\n" + text[bento_end:]

    with open('template_expedicao.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Template reordered and price section added!")
else:
    print("Sections not found.")
