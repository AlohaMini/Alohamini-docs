/* Progressively enhance the guide: every step remains readable without JavaScript. */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.admonition.am-step, .admonition.am-extra').forEach(block => {
    const title = block.querySelector(':scope > .admonition-title');
    if (!title) return;
    const details = document.createElement('details');
    details.className = block.classList.contains('am-step') ? 'am-reading-step' : 'am-reading-extra';
    if (block.id) details.id = block.id;
    const summary = document.createElement('summary');
    summary.append(...title.childNodes);
    details.append(summary);
    title.remove();
    const body = document.createElement('div');
    body.className = 'am-step-content';
    body.append(...block.childNodes);
    details.append(body);
    block.replaceWith(details);
  });
  const steps = [...document.querySelectorAll('.am-reading-step')];
  if (!steps.length) return;
  const openTarget = () => {
    let hash;
    try { hash = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = hash && document.getElementById(hash);
    const step = target && (target.closest('.am-reading-step') ||
      (target.nextElementSibling?.matches('.am-reading-step') ? target.nextElementSibling : null));
    if (step) {
      steps.forEach(item => { item.open = item === step; });
      // Open nested explanations before scrolling to an internal anchor.
      for (let parent = target.parentElement; parent; parent = parent.parentElement) {
        if (parent.tagName === 'DETAILS') parent.open = true;
      }
      requestAnimationFrame(() => {
        if (decodeURIComponent(location.hash.slice(1)) === hash) target.scrollIntoView({block: 'start'});
      });
    }
    return !!step;
  };
  if (!openTarget()) steps[0].open = true;
  steps.forEach(step => {
    step.addEventListener('toggle', () => {
      if (step.open) steps.filter(item => item !== step).forEach(item => { item.open = false; });
    });
  });
  window.addEventListener('hashchange', openTarget);
  // Reopening the current hash must also work after manually closing its step.
  document.querySelectorAll('a[href^="#step-"]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button) return;
      event.preventDefault();
      location.hash = link.hash;
      openTarget();
      const target = document.getElementById(link.hash.slice(1));
      target?.querySelector('summary')?.focus({preventScroll: true});
    });
  });
});
