import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We will completely overwrite the expedition-details-container part.
container_start = html.find('<div class="container expedition-details-container">')
container_end = html.find('<div class="faq-container">')

# Wait, let's just replace the whole body inside <main> to be safe.
# Actually, let's just use string replacement on the whole file to make it perfect.

html_start = html[:container_start]
footer_start = html.find('<footer class="site-footer">')
html_end = html[footer_start:]

new_container = '''<div class="container expedition-details-container">
            <!-- 1 & 2: Historia e Vibe -->
            <div class="bento-grid" style="grid-template-columns: 1fr; margin-bottom: 3rem;">
                <div class="bento-box bento-intro" style="padding: 3rem;">
                    <h2 style="font-size: 2.5rem; color: var(--accent-color); margin-bottom: 1rem;">O Destino</h2>
                    <div style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 2rem; color: #ddd;">
                        {{ HISTORIA_CONTENT }}
                    </div>
                    <h2 style="font-size: 2rem; margin-bottom: 1rem;">Como vai rolar a trip</h2>
                    <div style="font-size: 1.1rem; line-height: 1.6; color: #bbb;">
                        {{ VIBE_CONTENT }}
                    </div>
                </div>
            </div>

            <!-- 3: Specs (already handled in the hero section) -->

            <!-- 5: Atenção (Warnings) -->
            {{ ATENCAO_CONTENT }}

            <!-- 4: Cronograma -->
            <div class="timeline-container" style="margin-bottom: 3rem;">
                <h2 class="section-title">O Roteiro Passo a Passo</h2>
                <div class="timeline">
                    {{ TIMELINE_CONTENT }}
                </div>
            </div>

            <!-- 6 & 7: Incluso / Não Incluso -->
            <div class="bento-grid" style="margin-bottom: 3rem;">
                <div class="bento-box bento-included">
                    <h3 class="box-title"><i class="fas fa-check-circle" style="color: #4CAF50; margin-right: 10px;"></i> Incluso no Investimento</h3>
                    <ul class="included-list">
                        {{ INCLUDED_CONTENT }}
                    </ul>
                </div>
                <div class="bento-box bento-excluded">
                    <h3 class="box-title"><i class="fas fa-times-circle" style="color: #F44336; margin-right: 10px;"></i> Não Incluso</h3>
                    <ul class="excluded-list">
                        {{ EXCLUDED_CONTENT }}
                    </ul>
                </div>
            </div>

            <!-- 8: Investimento -->
            <div class="price-container" style="margin-bottom: 3rem;">
                <h2 style="font-size: 2rem; color: #fff; margin-bottom: 2rem; text-align: center;">Investimento</h2>
                <div class="bento-box" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 2rem; text-align: center;">
                    {{ PRICE_CONTENT }}
                </div>
            </div>

            <!-- 9 & 10: Política & FAQ -->
            <div class="faq-container" style="margin-bottom: 3rem;">
                <h2 class="section-title">Perguntas Frequentes & Políticas</h2>
                <div class="accordion">
                    {{ FAQ_CONTENT }}
                    {{ POLITICA_CONTENT }}
                </div>
            </div>
'''

final_html = html_start + new_container + "        </div>\n    </main>\n\n    " + html_end

with open('template_expedicao.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Template atualizado para 10 blocos!")
