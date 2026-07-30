        # ── Semantic Parser & Text Allocation (Heuristic Classifier) ────────────────────────────────────────────────
        def build_section(lines, html_tag="p"):
            return "".join(f"<{html_tag}>{l}</{html_tag}>" for l in lines)

        def build_list_items(lines):
            return "".join(f"<li>{l}</li>" for l in lines)
            
        def clean_lines(text):
            """Split on real newlines OR literal \\n, deduplicate, remove noise."""
            import re as _re
            seen, result = set(), []
            for line in _re.split(r'\\n|\n', text):
                line = line.strip().replace('\u200b','').replace('\xa0',' ').strip()
                if not line or len(line) < 5:
                    continue
                if line in seen:
                    continue
                seen.add(line)
                result.append(line)
            return result

        if not raw_text:
            intro_content    = "<p>Informações detalhadas estão sendo atualizadas para esta expedição.</p>"
            included_content = "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = "<li>Consulte nossa equipe para detalhes.</li>"
            timeline_content = """<div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content"><h3>Roteiro</h3><p>Em atualização — entre em contato para mais informações.</p></div></div>"""
            faq_content      = """<div class="accordion-item"><button class="accordion-header"><span>Tem dúvidas?</span><span class="icon">+</span></button><div class="accordion-body"><div class="accordion-content"><p>Entre em contato com nossa equipe — estamos prontos para ajudar você a planejar a expedição perfeita.</p></div></div></div>"""
        else:
            all_lines = clean_lines(raw_text)

            NOISE_PHRASES = {
                'uma experiência única', 'a natureza espera por você', 'garanta seu lugar', 
                'experiências inesquecíveis', 'como vai rolar essa trip', 'como vai rolar a trip',
                'o que esperar dessa viagem', 'quem pode participar', 'ricardo tiburtius',
                'somos uma empresa do sul do brasil', 'a n.a trekking nasceu',
                '"comida boa', 'não tem o que falar', 'guia gente boa', 'nota 1000'
            }
            
            def is_noise(line):
                ll = line.lower()
                for n in NOISE_PHRASES:
                    if n in ll:
                        return True
                return False

            META_SPEC_RE = re.compile(
                r'^(?:data:|ponto de encontro:|ganho de elevação:|perda de elevação:|'
                r'distância:|dificuldade física:|dificuldade técnica:|nível de preparação|'
                r'elevação m[íi]nima:|elevação m[áa]xima:|mudança na elevação:|'
                r'tempo de trekking:|noite média|classificamos esse|'
                r'esse roteiro acontecerá|\d{1,2}/\d{1,2}/|\d{4}\b)',
                re.IGNORECASE
            )

            TIME_RE = re.compile(r'^\d{1,2}:\d{2}\s')
            DAY_RE  = re.compile(r'^(?:dia\s+\d|d[ae]?\s*\d|\d+[°º]\s*dia)', re.IGNORECASE)
            ROUTE_ACTION_RE = re.compile(r'(?:acampamento\s+\S+\s*[>→]|portão\s+\S+\s*[>→]|acampamento\s+\w+\s*>\s*\w)', re.IGNORECASE)
            ROUTE_KEYWORDS = ['->', 'aeroporto de kilimanjaro ->']
            
            def is_timeline_trigger(line):
                if TIME_RE.match(line) or DAY_RE.match(line) or ROUTE_ACTION_RE.search(line):
                    return True
                if any(kw in line.lower() for kw in ROUTE_KEYWORDS):
                    return True
                return False

            WARNING_PHRASES = [
                'condições do tempo', 'não podemos garantir tempo bom',
                'esse é um roteiro que necessita', 'os horários podem variar',
                'as expedições em grupo são', 'não se preocupe pois sempre haverá'
            ]
            
            def is_warning(line):
                ll = line.lower()
                return any(w in ll for w in WARNING_PHRASES)

            FAQ_QUESTIONS = [
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
                return any(q in ll for q in FAQ_QUESTIONS)

            buckets = {
                'specs': [], 'intro': [], 'warnings': [],
                'timeline_data': [], 'included': [], 'excluded': [], 'faq_data': [],
            }
            
            ctx = {
                'mode': 'intro',
                'tl_title': None,
                'tl_body': [],
                'faq_q': None,
                'faq_a': []
            }
            
            def flush_tl():
                if ctx['tl_title'] or ctx['tl_body']:
                    t = ctx['tl_title'] if ctx['tl_title'] else "Etapa do roteiro"
                    buckets['timeline_data'].append((t, list(ctx['tl_body'])))
                ctx['tl_title'] = None
                ctx['tl_body'] = []
                
            def flush_faq():
                if ctx['faq_q']:
                    buckets['faq_data'].append((ctx['faq_q'], list(ctx['faq_a'])))
                ctx['faq_q'] = None
                ctx['faq_a'] = []

            for line in all_lines:
                ll = line.lower()
                if is_noise(line):
                    continue
                
                if ll in ['incluso no investimento', 'incluso no pacote', 'o que está incluso']:
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'included'
                    continue
                if ll in ['não incluso no investimento', 'não incluso', 'nao incluso', 'não está incluso']:
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'excluded'
                    continue
                    
                if is_faq_trigger(line):
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'faq'
                    ctx['faq_q'] = line
                    continue
                    
                if is_warning(line):
                    buckets['warnings'].append(line)
                    continue
                    
                if is_timeline_trigger(line):
                    flush_faq(); flush_tl()
                    ctx['mode'] = 'timeline'
                    ctx['tl_title'] = line
                    continue
                    
                if ctx['mode'] == 'intro' and META_SPEC_RE.match(line):
                    buckets['specs'].append(line)
                    continue

                if ctx['mode'] == 'intro':
                    if len(line) > 20: 
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'timeline':
                    ctx['tl_body'].append(line)
                elif ctx['mode'] == 'included':
                    if line.startswith('-') or len(line) < 120:
                        buckets['included'].append(line.lstrip('- '))
                    else:
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'excluded':
                    if line.startswith('-') or len(line) < 120:
                        buckets['excluded'].append(line.lstrip('- '))
                    else:
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'faq':
                    ctx['faq_a'].append(line)

            flush_tl()
            flush_faq()
            
            # Formatting Output
            intro_html = ""
            for p in buckets['intro'][:4]:
                intro_html += f"<p>{p}</p>"
            if not intro_html:
                intro_content = "<p>Uma aventura que transforma. Descubra paisagens únicas com segurança e apoio total da equipe NA Trekking.</p>"
                
            if buckets['specs']:
                intro_html += "<div class='expedition-specs' style='margin-top: 1.5rem; padding: 1.5rem; background: rgba(255,255,255,0.05); border-radius: 12px;'>"
                intro_html += "<h4 style='color: var(--primary-color); margin-bottom: 1rem; text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.1em;'>Especificações da Expedição</h4>"
                intro_html += "<ul style='list-style: none; padding: 0; margin: 0; display: grid; gap: 0.5rem;'>"
                for spec in buckets['specs']:
                    parts = spec.split(':', 1)
                    if len(parts) == 2:
                        intro_html += f"<li style='color: rgba(255,255,255,0.8);'><strong>{parts[0].strip()}:</strong> {parts[1].strip()}</li>"
                    else:
                        intro_html += f"<li style='color: rgba(255,255,255,0.8);'>{spec}</li>"
                intro_html += "</ul></div>"
            intro_content = intro_html

            if buckets['timeline_data']:
                timeline_content = ""
                for t_title, body_lines in buckets['timeline_data']:
                    body_html = "".join(f"<p>{l}</p>" for l in body_lines if l.strip())
                    timeline_content += f'''<div class="timeline-item">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>{t_title}</h3>
                            {body_html}
                        </div>
                    </div>'''
            else:
                timeline_content = """<div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content"><h3>Roteiro</h3><p>Informações do roteiro serão disponibilizadas em breve.</p></div></div>"""

            included_content = build_list_items(buckets['included']) or "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = build_list_items(buckets['excluded']) or "<li>Consulte nossa equipe para detalhes.</li>"

            faq_html = ""
            if buckets['warnings']:
                warnings_html = "".join(f"<p>{w}</p>" for w in buckets['warnings'])
                faq_html += f'''<div class="accordion-item">
                    <button class="accordion-header">
                        <span>Avisos Importantes</span>
                        <span class="icon">+</span>
                    </button>
                    <div class="accordion-body">
                        <div class="accordion-content">{warnings_html}</div>
                    </div>
                </div>'''

            for q, a_lines in buckets['faq_data']:
                a_text = "".join(f"<p>{l}</p>" for l in a_lines)
                if not a_text:
                    a_text = "<p>Entre em contato com nossa equipe para mais detalhes.</p>"
                faq_html += f'''<div class="accordion-item">
                    <button class="accordion-header">
                        <span>{q}</span>
                        <span class="icon">+</span>
                    </button>
                    <div class="accordion-body">
                        <div class="accordion-content">{a_text}</div>
                    </div>
                </div>'''
                
            faq_content = faq_html or """<div class="accordion-item">
                <button class="accordion-header"><span>Tem dúvidas?</span><span class="icon">+</span></button>
                <div class="accordion-body"><div class="accordion-content"><p>Entre em contato com nossa equipe — estamos prontos para ajudar você a planejar a expedição perfeita.</p></div></div>
            </div>"""

        # ── Inject into template ───────────────────────────────────────────
        page_html = template_html.replace('{{ TITLE }}', title)
        page_html = page_html.replace('{{ BACKGROUND_IMG }}', hero_image)
        page_html = page_html.replace('{{ DATES }}', dates)
        page_html = page_html.replace('{{ LOC }}', loc)
        page_html = page_html.replace('{{ DUR }}', dur)
        page_html = page_html.replace('{{ DIFFICULTY }}', difficulty)
        page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content if 'intro_content' in locals() else intro_html)
        page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_content)
        page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_content)
        page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_content)
        page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_content)
        page_html = page_html.replace('{{ ORIGINAL_LINK }}', url or '#')
