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


// --- Lógica de Expansão In-line (Acordeão Horizontal) ---
const cards = document.querySelectorAll('.catalog-card');
let currentlyExpandedCard = null;

const createExpandedHTML = (title, date, location, duration, bgUrl, bannerUrl) => `
    <div class="inline-expanded-bg" style="background-image: url('${bgUrl}')"></div>
    <div class="inline-expanded-content">
        <div class="inline-expanded-left">
            <div class="inline-expanded-banner" style='background-image: ${bannerUrl}'></div>
        </div>
        <div class="inline-expanded-right">
            <div class="inline-expanded-info">
                <h2 class="exp-title">${title}</h2>
                <p class="exp-meta"><span class="exp-date">${date}</span> &bull; <span class="exp-duration">${duration}</span></p>
                <p class="exp-location">${location}</p>
            </div>
            <div class="expanded-cta-wrapper">
                <button class="btn-primary exp-cta">Embarcar Nessa Rota</button>
            </div>
        </div>
    </div>
    <button class="inline-expanded-close">&times;</button>
`;

cards.forEach(card => {
    card.addEventListener('click', (e) => {
        // Se clicar no botão de fechar
        if (e.target.classList.contains('inline-expanded-close')) {
            e.stopPropagation();
            closeCard(card);
            return;
        }

        // Se já estiver expandido, não faz nada ao clicar de novo
        if (card.classList.contains('expanded')) return;

        // Se tiver outro aberto, fecha ele
        if (currentlyExpandedCard && currentlyExpandedCard !== card) {
            closeCard(currentlyExpandedCard);
        }

        // Extrai os dados
        const title = card.getAttribute('data-title');
        const date = card.getAttribute('data-date');
        const location = card.getAttribute('data-location');
        const duration = card.getAttribute('data-duration');
        const bgUrl = card.getAttribute('data-bg');
        const bannerUrl = card.style.backgroundImage;

        // Injeta o HTML interno do expansor
        card.innerHTML = createExpandedHTML(title, date, location, duration, bgUrl, bannerUrl);

        // Adiciona a classe que dispara o CSS (flex-basis 85vw)
        card.classList.add('expanded');
        card.closest('.row-carousel').classList.add('has-expanded');
        currentlyExpandedCard = card;

        // Centraliza o scroll suavemente na tela para o card esticado
        setTimeout(() => {
            card.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        }, 50);
    });
});

function closeCard(card) {
    card.classList.remove('expanded');
    card.closest('.row-carousel').classList.remove('has-expanded');
    // Remove o conteúdo do DOM após a transição de largura acabar (0.6s)
    setTimeout(() => {
        if(!card.classList.contains('expanded')) {
            card.innerHTML = '';
        }
    }, 600);
    
    if (currentlyExpandedCard === card) {
        currentlyExpandedCard = null;
    }
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
