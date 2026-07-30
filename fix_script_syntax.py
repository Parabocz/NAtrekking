with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Split at Accordion logic
parts = js.split('// --- Accordion Logic ---')
if len(parts) > 1:
    clean_js = parts[0] + """// --- Accordion Logic ---
const accordions = document.querySelectorAll('.accordion-header');
if (accordions.length > 0) {
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
}

// --- Timeline Intersection Observer ---
const timelineItems = document.querySelectorAll('.timeline-item');
if (timelineItems.length > 0) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    timelineItems.forEach(item => {
        observer.observe(item);
    });
}
"""
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(clean_js)
    print("Syntax error fixed!")
else:
    print("Could not find Accordion Logic marker.")
