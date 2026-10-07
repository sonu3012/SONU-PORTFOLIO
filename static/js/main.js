(function () {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  // Loader
  window.addEventListener('load', () => setTimeout(() => $('#loader').classList.add('done'), 700));

  // Navbar: scrolled state, progress bar, active link
  const nav = $('#nav'), bar = $('#progress');
  const sections = $$('section[id]');
  const links = $$('#links a');
  function onScroll() {
    const y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
    nav.classList.toggle('scrolled', y > 40);
    bar.style.width = (y / h * 100) + '%';
    let current = 'home';
    sections.forEach(s => { if (y + innerHeight * 0.35 >= s.offsetTop) current = s.id; });
    links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current));
  }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  const burger = $('#burger'), menu = $('#links');
  burger.addEventListener('click', () => menu.classList.toggle('open'));
  links.forEach(a => a.addEventListener('click', () => menu.classList.remove('open')));

  // Typing role rotation (roles are read from data via the first role; extra roles below mirror data.py)
  const roleEl = $('#role');
  const roles = (roleEl.dataset.roles ? JSON.parse(roleEl.dataset.roles) : null) || window.__ROLES__ || [roleEl.textContent];
  let ri = 0, ci = roles[0].length, deleting = true;
  function type() {
    const word = roles[ri];
    ci += deleting ? -1 : 1;
    roleEl.textContent = word.slice(0, ci);
    let delay = deleting ? 45 : 85;
    if (!deleting && ci === word.length) { delay = 1600; deleting = true; }
    else if (deleting && ci === 0) { deleting = false; ri = (ri + 1) % roles.length; delay = 300; }
    setTimeout(type, delay);
  }
  setTimeout(type, 2200);

  // Scroll reveal
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.12 });
  $$('.reveal').forEach(el => io.observe(el));

  // Tilt on the ID card
  const tilt = $('.tilt');
  if (tilt) {
    tilt.addEventListener('mousemove', e => {
      const r = tilt.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
      tilt.style.transform = `rotate(-4deg) rotateY(${x * 18}deg) rotateX(${-y * 18}deg)`;
    });
    tilt.addEventListener('mouseleave', () => tilt.style.transform = 'rotate(-4deg)');
  }

  // Contact form
  const form = $('#form'), status = $('#status'), send = $('#send');
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    status.textContent = 'Sending...';
    send.disabled = true;
    try {
      const r = await fetch('/api/contact', {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(d)
      });
      const j = await r.json();
      status.textContent = j.ok ? 'Thanks! I will get back to you soon.' : (j.error || 'Something went wrong.');
      if (j.ok) form.reset();
    } catch (_) {
      status.textContent = 'Network error. Please email me directly.';
    }
    send.disabled = false;
  });
})();
