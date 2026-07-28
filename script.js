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


// --- Animação da Agenda (Mapa Topográfico SVG) ---
// Configuração do caminho SVG
const pathActive = document.getElementById('route-path-active');
if(pathActive) {
    const pathLength = pathActive.getTotalLength();
    gsap.set(pathActive, { strokeDasharray: pathLength, strokeDashoffset: pathLength });

    // Scrubbing the path with ScrollTrigger
    gsap.to(pathActive, {
        strokeDashoffset: 0,
        ease: 'none',
        scrollTrigger: {
            trigger: '.map-container',
            start: 'top 50%',
            end: 'bottom 80%',
            scrub: 1,
        }
    });
}

// Nós do SVG e textos de destino (Acendendo um por um)
const nodes = document.querySelectorAll('.node');
const nodeGroups = document.querySelectorAll('.node-group');

gsap.set('.node', { scale: 0, opacity: 0, transformOrigin: "center center" });

nodeGroups.forEach((group, index) => {
    // Pop circle
    if(nodes[index]) {
        gsap.to(nodes[index], {
            scale: 1,
            opacity: 1,
            duration: 0.6,
            ease: 'back.out(1.7)',
            scrollTrigger: {
                trigger: group,
                start: 'top 70%',
                toggleActions: 'play none none reverse'
            }
        });
    }

    // Fade Group In (Title & Carousel)
    gsap.to(group, {
        y: 0,
        opacity: 1,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
            trigger: group,
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        }
    });

    // Make first slide active initially
    const carousel = group.querySelector('.carousel-container');
    if(carousel) {
        const originalSlides = Array.from(carousel.querySelectorAll('.carousel-slide'));
        
        // Multiplica os slides (Fake Infinite Loop)
        for(let i=0; i < 8; i++) {
            originalSlides.forEach(slide => {
                carousel.appendChild(slide.cloneNode(true));
            });
        }
        
        const slides = carousel.querySelectorAll('.carousel-slide');
        
        // Scroll listener for carousel coverflow logic
        const updateCoverflow = () => {
            const containerRect = carousel.getBoundingClientRect();
            const containerCenter = containerRect.left + (containerRect.width / 2);
            let closestSlide = null;
            let closestDistance = Infinity;

            slides.forEach(slide => {
                const slideRect = slide.getBoundingClientRect();
                const slideCenter = slideRect.left + (slideRect.width / 2);
                const distance = Math.abs(containerCenter - slideCenter);
                
                if (distance < closestDistance) {
                    closestDistance = distance;
                    closestSlide = slide;
                }
            });

            slides.forEach(s => s.classList.remove('active'));
            if(closestSlide) closestSlide.classList.add('active');
        };
        carousel.addEventListener('scroll', updateCoverflow);

        // Permite "seleção manual" tocando nos cards (scroll automático para o centro)
        slides.forEach(slide => {
            slide.addEventListener('click', () => {
                slide.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            });
        });

        // Auto-Pan Magnético
        let isDown = false;
        let isHovering = false;
        let startX;
        let scrollLeft;
        let autoPanSpeed = 0.7; // Velocidade reduzida e suave
        let exactScrollLeft = carousel.scrollLeft;

        const autoPan = () => {
            if(!isDown && !isHovering) {
                carousel.style.scrollSnapType = 'none'; // Desliga o snap para pan liso
                exactScrollLeft += autoPanSpeed;
                carousel.scrollLeft = exactScrollLeft;
            }
            requestAnimationFrame(autoPan);
        };
        requestAnimationFrame(autoPan);

        // Pausa do Auto-Pan e Drag-to-Scroll
        carousel.addEventListener('mouseenter', () => {
            isHovering = true;
            carousel.style.scrollSnapType = 'x mandatory'; // Liga snap magnético ao focar
            exactScrollLeft = carousel.scrollLeft; // Sync
        });
        
        carousel.addEventListener('mouseleave', () => {
            isHovering = false;
            isDown = false;
            carousel.style.scrollSnapType = 'none'; // Retoma auto pan
            exactScrollLeft = carousel.scrollLeft; // Sync
        });

        carousel.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.clientX;
            scrollLeft = carousel.scrollLeft;
            carousel.style.scrollBehavior = 'auto'; 
            carousel.style.scrollSnapType = 'none'; 
        });

        window.addEventListener('mouseup', () => {
            if(isDown) {
                isDown = false;
                carousel.style.scrollSnapType = 'x mandatory';
                carousel.style.scrollBehavior = 'smooth';
                exactScrollLeft = carousel.scrollLeft;
            }
        });

        carousel.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.clientX;
            const walk = (x - startX) * 2;
            carousel.scrollLeft = scrollLeft - walk;
            exactScrollLeft = carousel.scrollLeft;
        });
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
