// O'Works · site. Menu do celular, reel do Sobre, vídeos dos cases e formulário.

const semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// menu do celular
document.querySelectorAll(".cabecalho").forEach(cab => {
  const botao = cab.querySelector(".menu-botao");
  if (!botao) return;
  botao.addEventListener("click", () => {
    const aberto = cab.classList.toggle("aberto");
    botao.setAttribute("aria-expanded", String(aberto));
  });
  cab.querySelectorAll(".menu a").forEach(a => a.addEventListener("click", () => {
    cab.classList.remove("aberto");
    botao.setAttribute("aria-expanded", "false");
  }));
});

// reel do Sobre: o mesmo reel do portfólio de gastronomia, em loop, sem som; toca quando aparece na tela
const reelVideo = document.querySelector(".reel video[data-src]");
if (reelVideo && !semMovimento) {
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting) {
      if (!reelVideo.getAttribute("src")) reelVideo.src = reelVideo.dataset.src;
      reelVideo.play().catch(() => {});
    } else reelVideo.pause();
  }, { threshold: 0.2 }).observe(reelVideo);
}

// vídeos dos cases: carregam e tocam sem som quando aparecem; um clique liga o som
const videos = [...document.querySelectorAll(".video video")];
const tocar = v => { if (!v.getAttribute("src")) v.src = v.dataset.src; v.play().catch(() => {}); };
if (!semMovimento && videos.length) {
  const io = new IntersectionObserver(entradas => {
    entradas.forEach(e => (e.isIntersecting ? tocar(e.target) : e.target.pause()));
  }, { threshold: 0.4 });
  videos.forEach(v => io.observe(v));
}
videos.forEach(v => v.closest(".video").addEventListener("click", () => {
  const ligar = v.muted;
  videos.forEach(o => { o.muted = true; o.closest(".video").classList.remove("com-som"); });
  if (ligar) { v.muted = false; v.closest(".video").classList.add("com-som"); }
  tocar(v);
}));

// formulário: envia pelo FormSubmit para o e-mail da O'Works, sem sair da página
document.querySelectorAll("form.form").forEach(form => {
  const aviso = form.querySelector(".aviso");
  const botao = form.querySelector("button[type=submit]");
  form.addEventListener("submit", async ev => {
    if (!window.fetch) return;
    ev.preventDefault();
    if (form.querySelector(".honey input").value) return;
    botao.disabled = true;
    const dados = Object.fromEntries(new FormData(form).entries());
    try {
      const r = await fetch(form.dataset.ajax, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(dados),
      });
      if (!r.ok) throw new Error(r.status);
      form.reset();
      aviso.textContent = "Recebemos a sua mensagem. Respondemos em breve ☻";
    } catch (e) {
      aviso.innerHTML = 'Não deu para enviar agora. Escreva para <a href="mailto:hello@oworks.agency">hello@oworks.agency</a>.';
    }
    aviso.hidden = false;
    botao.disabled = false;
  });
});
