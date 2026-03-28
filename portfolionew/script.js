// ==========================================
// SCROLL REVEAL (Intersection Observer)
// ==========================================
const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            
            // Staggered Text Line Reveal
            if(entry.target.classList.contains('reveal-text')) {
                const lines = entry.target.querySelectorAll('.line-in');
                lines.forEach((line, index) => {
                    setTimeout(() => {
                        line.classList.add('active');
                    }, index * 150); // Faster stagger
                });
            }
        }
    });
}, observerOptions);

document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale').forEach(el => observer.observe(el));
document.querySelectorAll('.reveal-text').forEach(el => observer.observe(el));

// Initial trigger for hero section
setTimeout(() => {
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.classList.add('active');
        const lines = heroTitle.querySelectorAll('.line-in');
        lines.forEach((line, index) => {
            setTimeout(() => {
                line.classList.add('active');
            }, index * 150 + 200);
        });
    }
}, 50);

// ==========================================
// NAVBAR SCROLL & MOBILE MENU
// ==========================================
const navbar = document.querySelector('.nav-bar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("change");
    navMenu.classList.toggle("nav-active");
});

document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
        hamburger.classList.remove("change");
        navMenu.classList.remove("nav-active");
    });
});

// ==========================================
// PARALLAX SHAPES
// ==========================================
const parallaxElements = document.querySelectorAll('.parallax');

window.addEventListener('scroll', () => {
    if(window.innerWidth > 768) {
        let scrollY = window.scrollY;
        parallaxElements.forEach(el => {
            let speed = el.getAttribute('data-speed');
            el.style.transform = `translateY(${scrollY * speed * 0.2}px)`;
        });
    }
});
