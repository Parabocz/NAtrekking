with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

intro = text.split('<div class="bento-box bento-intro">')[1].split('</div>\n                <div class="bento-box bento-included">')[0]
included = text.split('<div class="bento-box bento-included">')[1].split('</div>\n                <div class="bento-box bento-excluded">')[0]
excluded = text.split('<div class="bento-box bento-excluded">')[1].split('</div>\n            </div>')[0]

timeline = text.split('<div class="timeline-container">')[1].split('</div>\n            </div>\n\n            <div class="faq-container">')[0]

old_container_start = text.find('<div class="container expedition-details-container">')
old_container_end = text.find('<div class="faq-container">')

old_part = text[old_container_start:old_container_end]

new_part = f'''<div class="container expedition-details-container">
            <div class="bento-grid" style="grid-template-columns: 1fr; margin-bottom: 3rem;">
                <div class="bento-box bento-intro">
                    {intro}
                </div>
            </div>

            <div class="timeline-container" style="margin-bottom: 3rem;">
                {timeline}
            </div>

            <div class="bento-grid" style="margin-bottom: 3rem;">
                <div class="bento-box bento-included">
                    {included}
                </div>
                <div class="bento-box bento-excluded">
                    {excluded}
                </div>
            </div>

            <div class="price-container" style="margin-bottom: 3rem;">
                <h2 style="font-size: 2rem; color: #fff; margin-bottom: 2rem; text-align: center;">Investimento</h2>
                <div class="bento-box" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 2rem; text-align: center;">
                    {{{{ PRICE_CONTENT }}}}
                </div>
            </div>

            '''

new_text = text.replace(old_part, new_part)

with open('template_expedicao.html', 'w', encoding='utf-8') as f:
    f.write(new_text)
print('Success!')
