import re
import os

# 1. Fix template_expedicao.html (Footer and ATENCAO_CONTENT)
with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hallucinated footer with the original one
bad_footer_start = html.find('<footer class="site-footer">')
bad_footer_end = html.find('</footer>', bad_footer_start) + 9

correct_footer = '''<footer class="footer">
        <p class="footer-phrase">A montanha chama.</p>
        <p class="footer-signature">© Natrekking. Feito para os selvagens.</p>
    </footer>'''

if bad_footer_start != -1:
    html = html[:bad_footer_start] + correct_footer + html[bad_footer_end:]

# Move ATENCAO_CONTENT below timeline
html = html.replace('{{ ATENCAO_CONTENT }}', '') # Remove it from its current position
timeline_end = html.find('</div>\n            </div>', html.find('<div class="timeline-container"')) + 27
if timeline_end != -1:
    # Insert it right after timeline-container ends
    html = html[:timeline_end] + '\n            {{ ATENCAO_CONTENT }}\n' + html[timeline_end:]

with open('template_expedicao.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix script.js (Remove DOMContentLoaded wrapper for accordion logic)
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the specific DOMContentLoaded block for accordion
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "// Accordion logic without DOMContentLoaded wrapper")
# We need to remove the closing }); for that block.
# Let's just find and replace the exact string from my previous insertion
old_js_block = """// --- Accordion Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', function() {
            this.classList.toggle('active');
            const content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                content.style.paddingTop = '0';
                content.style.paddingBottom = '0';
                content.style.opacity = '0';
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                content.style.paddingTop = '1rem';
                content.style.paddingBottom = '1rem';
                content.style.opacity = '1';
            }
        });
    });

    // --- Timeline Intersection Observer ---
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.timeline-item').forEach(item => {
        observer.observe(item);
    });
});"""

new_js_block = """// --- Accordion Logic ---
const accordions = document.querySelectorAll('.accordion-header');
accordions.forEach(acc => {
    acc.addEventListener('click', function() {
        this.classList.toggle('active');
        const content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            content.style.paddingTop = '0';
            content.style.paddingBottom = '0';
            content.style.opacity = '0';
        } else {
            content.style.maxHeight = content.scrollHeight + 40 + "px";
            content.style.paddingTop = '1rem';
            content.style.paddingBottom = '1rem';
            content.style.opacity = '1';
        }
    });
});

// --- Timeline Intersection Observer ---
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.timeline-item').forEach(item => {
    observer.observe(item);
});"""

js = js.replace(old_js_block, new_js_block)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Template, layout, and JS fixed!")
