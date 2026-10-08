(() => {
  const links = [...document.querySelectorAll('.study-nav a:not(.study-name)')];
  if (!links.length || !('IntersectionObserver' in window)) return;
  const observer = new IntersectionObserver(entries => {
    const entry = entries.find(item => item.isIntersecting);
    if (!entry) return;
    links.forEach(link => {
      if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, {rootMargin: '-15% 0px -65% 0px'});
  document.querySelectorAll('.study-section').forEach(section => observer.observe(section));
})();
