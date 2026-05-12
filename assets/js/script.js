document.addEventListener('DOMContentLoaded', () => {
    
    // Navbar Scroll Effect (Sticky on Scroll Up)
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', () => {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        if (scrollTop > 150) {
            if (scrollTop > lastScrollTop) {
                // Scrolling Down
                navbar.classList.add('header-hidden');
                navbar.classList.remove('header-visible');
            } else {
                // Scrolling Up
                navbar.classList.add('header-visible');
                navbar.classList.remove('header-hidden');
            }
        } else {
            navbar.classList.remove('header-hidden');
            navbar.classList.remove('header-visible');
        }
        
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    });

    // Hide Preloader after 1 second
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('loaded');
        }
    }, 1000);
    
    // Synchronized Number Counter Animation
    const counters = document.querySelectorAll('.counter-value');
    const duration = 2000; // All animations will end exactly in 2 seconds

    const startCounters = (entries, observer) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                const counter = entry.target;
                const target = +counter.getAttribute('data-target');
                let startTime = null;

                const animate = (currentTime) => {
                    if (!startTime) startTime = currentTime;
                    const progress = Math.min((currentTime - startTime) / duration, 1);
                    const currentCount = Math.floor(progress * target);
                    
                    counter.innerText = currentCount;

                    if (progress < 1) {
                        requestAnimationFrame(animate);
                    } else {
                        counter.innerText = target;
                    }
                };
                requestAnimationFrame(animate);
                observer.unobserve(counter);
            }
        });
    };

    if ('IntersectionObserver' in window && counters.length > 0) {
        const observer = new IntersectionObserver(startCounters, { threshold: 0.5 });
        counters.forEach(counter => {
            observer.observe(counter);
        });
    }

    // Scroll to Top Button Visibility and Action
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    if(scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                scrollTopBtn.classList.add('show');
            } else {
                scrollTopBtn.classList.remove('show');
            }
        });

        scrollTopBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Fallback logic for mobile offcanvas close button
    const customCloseBtn = document.querySelector('.btn-close-custom');
    if (customCloseBtn) {
        customCloseBtn.addEventListener('click', () => {
            const offcanvasEl = document.getElementById('offcanvasNavbar');
            if (offcanvasEl) {
                const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) || new bootstrap.Offcanvas(offcanvasEl);
                bsOffcanvas.hide();
            }
        });
    }

    // Initialize Swiper for Hero Section
    if (document.querySelector('.heroImageSwiper')) {
        new Swiper('.heroImageSwiper', {
            loop: true,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
        });
    }

    // Initialize Swiper for Program Cards
    if (document.querySelector('.programSwiper')) {
        new Swiper('.programSwiper', {
            slidesPerView: 1.5, /* Shows partial next slide on mobile */
            spaceBetween: 25,
            loop: true,
            autoplay: {
                delay: 2500,
                disableOnInteraction: false,
            },
            breakpoints: {
                768: { slidesPerView: 2, spaceBetween: 30 },
                1024: { slidesPerView: 3, spaceBetween: 40 }
            }
        });
    }

    // Initialize Swiper for Testimonials
    if (document.querySelector('.testimonialSwiper')) {
        new Swiper('.testimonialSwiper', {
            slidesPerView: 1.7, /* Shows partial next slide on mobile */
            spaceBetween: 25,
            loop: true,
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                768: { slidesPerView: 2, spaceBetween: 30 },
                1024: { slidesPerView: 3, spaceBetween: 40 } /* Larger on Desktop (3 instead of 5) */
            }
        });
    }

    // Events Swiper Initialization
    new Swiper('.eventsSwiper', {
        slidesPerView: 1.5, /* Shows partial next slide on mobile */
        spaceBetween: 25,
        loop: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.events-pagination',
            clickable: true,
        },
        breakpoints: {
            768: { slidesPerView: 2 },
            1024: { slidesPerView: 3 }
        }
    });
});
