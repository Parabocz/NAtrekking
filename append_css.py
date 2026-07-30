wix_css = """
/* --- WIX STATIC CONTENT OVERRIDES --- */
#wix-static-content {
    background-color: var(--bg-color);
    color: var(--text-color);
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    font-family: 'Inter', sans-serif;
}
#wix-static-content * {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    transform: none !important;
    width: auto !important;
    height: auto !important;
    min-height: 0 !important;
    background: transparent !important;
    color: inherit !important;
    margin: 0 !important;
    box-shadow: none !important;
    border: none !important;
}
#wix-static-content img, 
#wix-static-content wix-image,
#wix-static-content [data-type="image"],
#wix-static-content svg {
    display: none !important;
}
#wix-static-content h1, 
#wix-static-content h2, 
#wix-static-content h3, 
#wix-static-content h4, 
#wix-static-content h5, 
#wix-static-content h6 {
    color: var(--accent-color) !important;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
    font-weight: 700 !important;
    font-size: 1.5rem !important;
}
#wix-static-content p, 
#wix-static-content span {
    margin-bottom: 0.5rem !important;
    line-height: 1.6 !important;
}
#wix-static-content div {
    padding: 0.25rem 0 !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(wix_css)

print("CSS appended.")
