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
