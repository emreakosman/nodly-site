// Landing page motion. Everything here is decoration over content that is
// already in the HTML, so the page reads the same without it.
(() => {
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const BAND = [45, 70];   // target range on the gauge, both sides
  const CENTER = 10;       // back within this many degrees counts as returned

  // Scroll progress bar
  const bar = document.querySelector(".progress-bar");
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.setProperty("--p", max > 0 ? scrollY / max : 0);
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Reveal on scroll; count-ups start when their block appears
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add("in");
      entry.target.querySelectorAll("[data-count]").forEach(countUp);
      io.unobserve(entry.target);
    }
  }, { threshold: 0.2 });
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  function countUp(el) {
    const target = Number(el.dataset.count);
    if (still) { el.textContent = target; return; }
    const start = performance.now();
    const step = (now) => {
      const k = Math.min(1, (now - start) / 1400);
      el.textContent = Math.round(target * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  // Gauge: same arc as the exercise screen. A rep counts when the head
  // reaches the band and then comes back to center, like the app.
  function Gauge(root, onRep) {
    const R = 118, C = 150;
    const dot = root.querySelector("[data-dot]");
    const fill = root.querySelector("[data-fill]");
    const head = root.querySelector("[data-head]");
    const angle = root.querySelector("[data-angle]");
    const status = root.querySelector("[data-status]");
    const s = status.dataset;
    let reached = false;
    const pt = (deg) => {
      const r = deg * Math.PI / 180;
      return [C + R * Math.sin(r), C - R * Math.cos(r)];
    };
    return (deg) => {
      const [x, y] = pt(deg);
      const [x0, y0] = pt(0);
      dot.setAttribute("cx", x.toFixed(1));
      dot.setAttribute("cy", y.toFixed(1));
      fill.setAttribute("d", `M${x0} ${y0}A${R} ${R} 0 0 ${deg >= 0 ? 1 : 0} ${x.toFixed(1)} ${y.toFixed(1)}`);
      head.setAttribute("transform", `rotate(${deg.toFixed(1)} 150 150)`);
      angle.textContent = Math.round(Math.abs(deg));
      const a = Math.abs(deg);
      const hit = a >= BAND[0] && a <= BAND[1];
      root.classList.toggle("hit", hit);
      if (hit && !reached) {
        reached = true;
        root.classList.remove("pulse");
        void root.offsetWidth;   // restart the pulse
        root.classList.add("pulse");
      }
      if (reached && a < CENTER) { reached = false; onRep(); }
      status.textContent = hit ? s.reached : reached ? s.back : deg < -2 ? s.l : s.r;
    };
  }

  // Try-it slider
  const range = document.querySelector("[data-demo]");
  if (range) {
    const out = document.querySelector("[data-demo-reps]");
    let n = 0;
    const set = Gauge(document.querySelector("[data-gauge]"), () => { out.textContent = ++n; });
    range.addEventListener("input", () => set(Number(range.value)));
    set(0);
  }

  // Posture: the reminder banner comes and goes over the running session
  const duo = document.querySelector("[data-duo]");
  if (duo && !still) {
    let n = 0;
    setInterval(() => duo.classList.toggle("ping", ++n % 3 === 1), 2500);
  }
})();
