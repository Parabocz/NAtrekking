// Registrar o plugin ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Inicializar Lenis (Scroll Suave Inercial)
const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smooth: true,
    smoothTouch: false,
});

function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Sincronizar Lenis e ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

// --- Animações da Hero Section ---
const tlHero = gsap.timeline();

// Slow zoom infinito e imperceptível no background
gsap.to('.hero-video, .sobre-bg', {
    scale: 1.15,
    duration: 25,
    repeat: -1,
    yoyo: true,
    ease: 'sine.inOut'
});

// Fade-up staggers para os textos da Hero
tlHero.fromTo('.hero-pre-headline', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 1, ease: 'power3.out', delay: 0.2 })
      .fromTo('.hero-headline', { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 1.2, ease: 'power4.out' }, '-=0.6')
      .fromTo('.hero-subheadline', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 1, ease: 'power3.out' }, '-=0.8')
      .fromTo('.hero .btn-primary', { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' }, '-=0.6')
      .fromTo('.scroll-indicator', { opacity: 0 }, { opacity: 1, duration: 1, ease: 'power2.inOut' }, '-=0.2');


// --- Lógica do Catálogo Netflix (Gaveta Expansível) ---
const cards = document.querySelectorAll('.catalog-card');
let currentExpanded = null;

cards.forEach(card => {
    card.addEventListener('click', (e) => {
        const row = card.closest('.catalog-row');
        
        // Se já existe um painel aberto
        if (currentExpanded) {
            // Se clicou no mesmo card ou mesma linha e já está aberto
            if (currentExpanded.row === row) {
                // Atualizar dados no painel existente
                updateExpandedView(currentExpanded.element, card);
                return;
            } else {
                // Fechar o anterior
                closeExpandedView(currentExpanded.element);
            }
        }

        // Criar novo painel a partir do template
        const template = document.getElementById('expanded-view-template');
        const expandedNode = template.content.cloneNode(true);
        const expandedEl = expandedNode.querySelector('.expanded-view');
        
        updateExpandedView(expandedEl, card);

        // Inserir após a linha (row) atual
        row.insertAdjacentElement('afterend', expandedEl);
        
        // Listener de fechar
        expandedEl.querySelector('.expanded-close').addEventListener('click', () => {
            closeExpandedView(expandedEl);
        });

        // Trigger animação de abertura
        requestAnimationFrame(() => {
            expandedEl.classList.add('open');
            // Scroll suave para mostrar o painel se estiver fora da tela
            setTimeout(() => {
                const rect = expandedEl.getBoundingClientRect();
                if (rect.bottom > window.innerHeight) {
                    window.scrollBy({ top: rect.bottom - window.innerHeight + 50, behavior: 'smooth' });
                }
            }, 300);
        });

        currentExpanded = { element: expandedEl, row: row };
    });
});

function updateExpandedView(el, card) {
    const title = card.getAttribute('data-title');
    const date = card.getAttribute('data-date');
    const location = card.getAttribute('data-location');
    const duration = card.getAttribute('data-duration');
    const bgUrl = card.getAttribute('data-bg');
    
    // Pega a URL do inline style backgroundImage do card
    const bannerUrl = card.style.backgroundImage;

    el.querySelector('.exp-title').textContent = title;
    el.querySelector('.exp-date').textContent = date;
    el.querySelector('.exp-location').textContent = location;
    el.querySelector('.exp-duration').textContent = duration;
    
    el.querySelector('.expanded-bg').style.backgroundImage = `url('${bgUrl}')`;
    el.querySelector('.expanded-banner').style.backgroundImage = bannerUrl;
}

function closeExpandedView(el) {
    el.classList.remove('open');
    if(currentExpanded && currentExpanded.element === el) {
        currentExpanded = null;
    }
    // Aguardar transição CSS para remover do DOM
    setTimeout(() => {
        if(el.parentElement) el.remove();
    }, 600);
}

    // --- Animação de Entrada da Seção Sobre ---
    const tlSobre = gsap.timeline({
        scrollTrigger: {
            trigger: ".sobre",
            start: "top 65%", // Dispara quando a seção atinge 65% da altura da tela
            toggleActions: "play none none none" // Toca apenas uma vez
        }
    });

    tlSobre.fromTo(".sobre-label", 
        { x: -50, opacity: 0, letterSpacing: "0em" }, 
        { x: 0, opacity: 1, letterSpacing: "0.3em", duration: 1, ease: "power3.out" }
    )
    .fromTo(".sobre-headline-large", 
        { y: 120, opacity: 0, skewY: 5 }, 
        { y: 0, opacity: 1, skewY: 0, duration: 1.4, ease: "power4.out" }, 
        "-=0.7"
    )
    .fromTo(".manifesto", 
        { y: 50, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 1.2, ease: "power3.out" }, 
        "-=1.0"
    )
    .fromTo(".divider", 
        { scaleX: 0, transformOrigin: "left center" }, 
        { scaleX: 1, duration: 1, ease: "power4.inOut" }, 
        "-=0.8"
    )
    .fromTo(".escopo", 
        { y: 40, opacity: 0, filter: "blur(5px)" }, 
        { y: 0, opacity: 1, filter: "blur(0px)", duration: 1.2, ease: "power3.out" }, 
        "-=0.7"
    );

    // Sincronização do Vídeo com Scroll (Scrubbing)
    const trailVideo = document.querySelector('.trail-video-bg');
    if (trailVideo) {
        trailVideo.pause();

        let scrubInit = false;
        // Tenta iniciar a cada 100ms até que o vídeo tenha carregado seus metadados (duration)
        const checkVideo = setInterval(() => {
            if (trailVideo.duration && !scrubInit) {
                scrubInit = true;
                clearInterval(checkVideo);
                
                // Criação da animação nativa do GSAP para suavização (scrub: 1)
                gsap.fromTo(trailVideo, 
                    { currentTime: 0 },
                    {
                        scrollTrigger: {
                            trigger: ".agenda",
                            start: "top top",
                            end: "bottom bottom",
                            scrub: 1
                        },
                        currentTime: trailVideo.duration,
                        ease: "none"
                    }
                );
            }
        }, 100);
    }
});

// Custom Cursor Logic for Carousels
const cursor = document.querySelector('.custom-cursor');
const carousels = document.querySelectorAll('.carousel-container');

if(cursor && carousels.length > 0) {
    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // Animate cursor smooth follow
    gsap.ticker.add(() => {
        cursorX += (mouseX - cursorX) * 0.2;
        cursorY += (mouseY - cursorY) * 0.2;
        gsap.set(cursor, { left: cursorX, top: cursorY });
    });

    carousels.forEach(car => {
        car.addEventListener('mouseenter', () => {
            cursor.classList.add('active');
        });
        car.addEventListener('mouseleave', () => {
            cursor.classList.remove('active');
        });
    });
}

// --- Animações Sobre Nós ---
// Parallax Background
gsap.to('.sobre-bg', {
    yPercent: 15,
    ease: 'none',
    scrollTrigger: {
        trigger: '.sobre',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
    }
});

// Stagger Texts Sobre Nós
gsap.fromTo('.sobre-content > *', 
    { y: 40, opacity: 0 },
    { 
        y: 0, 
        opacity: 1, 
        duration: 1, 
        stagger: 0.2,
        ease: 'power3.out',
        scrollTrigger: {
            trigger: '.sobre-content',
            start: 'top 80%'
        }
    }
);

// --- Animações Comunidade ---
gsap.fromTo('.comunidade-content > *', 
    { y: 40, opacity: 0 },
    { 
        y: 0, 
        opacity: 1, 
        duration: 1, 
        stagger: 0.2,
        ease: 'power3.out',
        scrollTrigger: {
            trigger: '.comunidade-content',
            start: 'top 80%'
        }
    }
);
