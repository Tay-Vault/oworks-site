#!/usr/bin/env python3
"""Gera as páginas do site da O'Works a partir dos dados abaixo.

Rodar de dentro da pasta do site:  python3 _build/build.py
A pasta _build não é publicada (o GitHub Pages ignora pastas que começam com _).
"""
import html
import os
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = time.strftime("%Y%m%d%H%M%S")
SITE = "https://oworks.agency"

WHATS = "https://wa.me/message/UG2DE52RIKDYO1"
INSTA = "https://www.instagram.com/oworks.ag/"
EMAIL = "hello@oworks.agency"


def sym(t):
    return t.replace("☻", '<span class="sym">☻</span>')


def br(t):
    """Quebras pensadas para a desktop; no celular o texto corre livre."""
    return t.replace("\n", '<br class="d"> ')


def esc(t):
    return html.escape(t, quote=True)


# ---------------------------------------------------------------- dados
CASES = [
    dict(
        slug="maz-botafogo", n="01", nome="Maz Botafogo",
        seg="Gastronomia · Botafogo, Rio de Janeiro",
        lista="Uma marca criada do zero,\nque segue em uso até hoje.",
        frase="Feito à mão, servido com calma.",
        texto="Da massa aberta na hora ao prato pronto, a cozinha do Maz é cuidado. A identidade segue o mesmo cuidado, do logo às estampas, uniformes e embalagens que chegam à mesa de casa.",
        chips=["Estratégia de marca", "Identidade visual", "Estampas e uniformes", "Cardápio e embalagens", "Fotografia e vídeo", "Social media"],
        papel="Uma marca criada do zero.",
        sub="O universo visual criado pela O'Works segue em uso até hoje.",
        hero="maz-hero.jpg",
        uni=[[("img", "maz-u1.jpg")],
             [("img", "maz-u2.jpg"), ("img", "maz-u3.jpg")],
             [("img", "maz-u4.jpg"), ("sw", [("Preto", "#1D1D1B", "#EFEBE4"), ("Creme", "#F3ECE2", "#1D1D1B")])]],
        aplic=dict(titulo="Estampas, camisetas\ne aplicações", texto="Estampas personalizadas, uniformes e peças\nque levam a marca para fora do prato.",
                   imgs=["maz-a1.jpg", "maz-a2.jpg", "maz-a3.jpg"]),
        posts=["maz-p1.jpg", "maz-p2.jpg", "maz-p3.jpg", "maz-p4.jpg"],
        videos=["maz-1", "maz-2", "maz-3", "maz-4"],
    ),
    dict(
        slug="38-by-castelinho", n="02", nome="38 by Castelinho",
        seg="Gastronomia · Rio de Janeiro",
        lista="Uma marca pensada para ser desejada\nantes da primeira visita.",
        frase="Um lugar para se imaginar.",
        texto="Da identidade ao cardápio, da luz da manhã à mesa posta. Marca e conteúdos traduzem o clima da casa no ritmo calmo de quem aproveita sem pressa, e fazem o lugar ser desejado antes da primeira visita.",
        chips=["Estratégia de marca", "Universo visual", "Cardápios", "Fotografia e vídeo", "Direção criativa", "Social media"],
        papel="Uma marca pensada para ser desejada antes da primeira visita.",
        sub="O universo visual criado pela O'Works segue em uso até hoje.",
        hero="c38-hero.jpg",
        uni=[[("img", "c38-u1.jpg")],
             [("img", "c38-u2.jpg")],
             [("sw", [("Terracota", "#C1693B", "#F5F1EA"), ("Areia", "#D8CCB8", "#1E1E1E"), ("Preto", "#1E1E1E", "#F5F1EA"),
                      ("Oliva", "#80805F", "#F5F1EA"), ("Ferrugem", "#8B3A1C", "#F5F1EA"), ("Musgo", "#243A22", "#F5F1EA")])]],
        posts=["c38-p1.jpg", "c38-p2.jpg", "c38-p3.jpg", "c38-p4.jpg"],
        videos=["c38-1", "c38-2", "c38-3", "c38-4"],
    ),
    dict(
        slug="la-dolina-horno", n="03", nome="La Dolina Horno",
        seg="Gastronomia · Espírito Santo",
        lista="Uma marca nova dentro\nde uma casa que já existia.",
        frase="Do forno à caixa de pizza.",
        texto="A Horno nasceu como uma nova frente da La Dolina, focada em assados, pizzas, sanduíches e drinks. A identidade é mais clara e rústica que a da marca original e conversa com ela, do logo à caixa de pizza.",
        chips=["Arquitetura de marca", "Identidade visual", "Embalagens", "Cardápio", "Fotografia e vídeo", "Social media"],
        papel="Uma marca nova dentro de uma casa que já existia.",
        sub="O universo visual criado pela O'Works segue em uso até hoje.",
        hero="ld-hero.jpg",
        uni=[[("img", "ld-u1.jpg")],
             [("img", "ld-u2.jpg"), ("img", "ld-u3.jpg")],
             [("sw", [("Preto", "#141414", "#F5F1EA"), ("Ocre", "#E8AE5F", "#1E1E1E"), ("Sálvia", "#6F9C82", "#1E1E1E"),
                      ("Terracota", "#8E5A4C", "#F5F1EA"), ("Verde", "#3D6450", "#F5F1EA"), ("Terra", "#5B2615", "#F5F1EA")])]],
        posts=["ld-p1.jpg", "ld-p2.jpg", "ld-p3.jpg"],
        videos=["ld-1", "ld-2", "ld-3", "ld-4"],
    ),
    dict(
        slug="fogata", n="04", nome="Fogata",
        seg="Gastronomia · Vila Velha, Espírito Santo",
        lista="Um personagem que virou\no símbolo da casa.",
        frase="Argentina de coração, capixaba de endereço.",
        texto="Empanadas, vinhos e cozinha argentina feitas em Vila Velha. Com ilustração autoral inspirada no pet da família, Cacau, a identidade dá à casa um jeito próprio. Nos vídeos, a O'Works captou e editou o calor do forno e a história por trás de cada receita.",
        chips=["Estratégia de marca", "Identidade visual", "Personagem e ícones", "Naming", "Captação e edição de vídeos"],
        papel="Um personagem que virou o símbolo da casa.",
        sub="O universo visual criado pela O'Works segue em uso até hoje, aplicado pela própria equipe da casa.",
        hero="fog-hero.jpg",
        uni=[[("img", "fog-u1.jpg")],
             [("img", "fog-u2.jpg"), ("img", "fog-u3.jpg")],
             [("img", "fog-u4.jpg"), ("sw", [("Vermelho", "#DD380D", "#F5F1EA"), ("Laranja", "#FF8B24", "#1E1E1E"), ("Âmbar", "#FFAE39", "#1E1E1E"),
                                              ("Azul", "#87B5D4", "#1E1E1E"), ("Linho", "#E9E3D8", "#1E1E1E"), ("Preto", "#1E1E1E", "#F5F1EA")])]],
        posts=["fog-p1.jpg", "fog-p2.jpg", "fog-p3.jpg", "fog-p4.jpg"],
        videos=["fog-1", "fog-2", "fog-3", "fog-4"],
    ),
    dict(
        slug="lorena-vervloet", n="05", nome="Lorena Vervloet",
        seg="Saúde e estética",
        lista="A estética tratada como cuidado,\ne não como promessa.",
        frase="Cuidado que dá para ver.",
        texto="Uma cirurgiã-dentista especializada em harmonização orofacial, que trata a estética como cuidado, e não como promessa. A comunicação coloca a Lorena no centro: rosto real, explicação clara e a mesma delicadeza do consultório, agora nas telas.",
        chips=["Direção criativa", "Roteiro", "Captação", "Edição", "Design"],
        papel="A estética tratada como cuidado, e não como promessa.",
        sub="A comunicação coloca a Lorena no centro, com rosto real e explicação clara.",
        hero="lor-hero.jpg",
        videos=["lor-1", "lor-2", "lor-3", "lor-4"],
    ),
    dict(
        slug="avantec", n="06", nome="Avantec",
        seg="Engenharia",
        lista="Uma empresa técnica contada pelas\npessoas que fazem ela acontecer.",
        frase="Engenharia com rosto.",
        texto="Uma empresa técnica contada pelas pessoas que fazem ela acontecer. Entrevistas, datas importantes para o time e presença nas cidades onde atua deram à marca uma voz próxima e humana.",
        chips=["Direção criativa", "Planejamento", "Captação", "Edição"],
        papel="Uma empresa técnica contada pelas pessoas que fazem ela acontecer.",
        sub="Entrevistas, datas do time e presença nas cidades deram à marca uma voz próxima.",
        hero="ava-hero.jpg",
        videos=["ava-1", "ava-2", "ava-3", "ava-4"],
    ),
]

DESC_PADRAO = "Estúdio de direção criativa e comunicação. Pensamos a estratégia, criamos a ideia e cuidamos de cada peça até ela ganhar vida, em vídeo, design e fotografia."


APOIO = br("Pensamos a estratégia, criamos a ideia\ne cuidamos de cada peça até ela ganhar\nvida, em vídeo, design e fotografia.")
INTRO = br("Mais de 40 marcas, dos mais diversos segmentos.\nDa saúde à gastronomia, da engenharia à tecnologia,\nalgumas histórias que ajudamos a contar.")
CITA = br("Os clientes que passaram\npela O'Works seguem usando\naté hoje o universo visual\ncriado por nós.")
COMO = br("Primeiro a estratégia de comunicação e a visual,\ndepois a de conteúdo. Cada etapa só começa\nquando a anterior está aprovada.")


# ---------------------------------------------------------------- partes
def head(titulo, caminho, desc=DESC_PADRAO):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{caminho}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="O'Works">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{caminho}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta name="theme-color" content="#1E1E1E">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=Instrument+Serif:ital@1&family=Noto+Sans+Symbols&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={VER}">
</head>
<body>
"""


def fim():
    return f"""<script src="/assets/js/site.js?v={VER}" defer></script>
</body>
</html>
"""


def cabecalho(atual="", fale="/contato/"):
    def item(href, nome, chave):
        cur = ' aria-current="page"' if atual == chave else ""
        return f'<a href="{href}"{cur}>{nome}</a>'
    return f"""<header class="cabecalho">
  <a class="logo" href="/">O'Works</a>
  <button class="menu-botao" type="button" aria-label="Abrir o menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  <nav class="menu" id="menu" aria-label="Principal">
    {item('/#clientes', 'Clientes', 'clientes')}
    {item('/estudio/', 'Estúdio', 'estudio')}
    {item('/contato/', 'Contato', 'contato')}
    <a class="btn medio" href="{fale}">Fale com a gente</a>
  </nav>
</header>"""


def contatos_linha():
    return f"""<div class="contatos">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="{WHATS}" target="_blank" rel="noopener">WhatsApp (27) 99573-9709</a>
        <a href="{INSTA}" target="_blank" rel="noopener">@oworks.ag</a>
      </div>"""


def formulario():
    return f"""<form class="form" action="https://formsubmit.co/{EMAIL}" method="POST" data-ajax="https://formsubmit.co/ajax/{EMAIL}">
      <p class="rotulo">Ou escreva aqui</p>
      <label class="campo"><span class="visually-hidden">Nome</span><input name="nome" placeholder="Nome" required autocomplete="name"></label>
      <label class="campo"><span class="visually-hidden">E-mail</span><input type="email" name="email" placeholder="E-mail" required autocomplete="email"></label>
      <label class="campo"><span class="visually-hidden">WhatsApp</span><input type="tel" name="whatsapp" placeholder="WhatsApp" autocomplete="tel"></label>
      <label class="campo"><span class="visually-hidden">Marca ou empresa</span><input name="marca" placeholder="Marca ou empresa" autocomplete="organization"></label>
      <label class="campo"><span class="visually-hidden">Mensagem</span><textarea name="mensagem" placeholder="Conte sobre a sua marca e o que você precisa" required></textarea></label>
      <input type="hidden" name="_subject" value="Novo contato pelo site da O'Works">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="{SITE}/obrigado/">
      <div class="honey" aria-hidden="true"><input type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
      <button class="btn" type="submit">Enviar</button>
      <p class="aviso" role="status" hidden></p>
    </form>"""


def rodape_links():
    return f"""<footer class="rodape">
      <span>© 2026 O'Works</span>
      <span><a href="/#clientes">Clientes</a> · <a href="/estudio/">Estúdio</a> · <a href="/contato/">Contato</a> · <a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></span>
    </footer>
    <div class="assinatura" aria-hidden="true"><span>O'Works</span></div>"""


def bloco_contato(com_form=False):
    if com_form:
        miolo = f"""<div class="chamada com-form">
      <div class="texto">
        <h2 class="vamos">Vamos criar algo juntos?</h2>
        <p class="conta">Conta pra gente o que{'<br class="d">'} a sua marca quer ser.</p>
        {contatos_linha()}
        <span class="carinha" aria-hidden="true">☻</span>
      </div>
      {formulario()}
    </div>"""
    else:
        miolo = f"""<div class="chamada">
      <div class="texto">
        <h2 class="vamos">Vamos criar algo juntos?</h2>
        <p class="conta">Conta pra gente o que{'<br class="d">'} a sua marca quer ser.</p>
        {contatos_linha()}
        <a class="btn" href="/contato/">Fale com a gente</a>
      </div>
      <span class="carinha" aria-hidden="true">☻</span>
    </div>"""
    return f"""<section class="escuro contato-bloco" id="contato">
  <div class="wrap">
    {miolo}
    {rodape_links()}
  </div>
</section>
"""


def selo_svg():
    return """<svg viewBox="0 0 232 232" aria-hidden="true">
        <circle cx="116" cy="116" r="116" fill="#EFEBE4"/>
        <g class="giro">
          <path id="selo-circulo" d="M16,116 a100,100 0 1,1 200,0 a100,100 0 1,1 -200,0" fill="none"/>
          <text font-family="Archivo, sans-serif" font-weight="600" font-size="13.5" fill="#1E1E1E"><textPath href="#selo-circulo" textLength="626" lengthAdjust="spacing">CRIATIVIDADE E ESTRATÉGIA PARA COMUNICAR SUA AUTENTICIDADE <tspan font-family="Noto Sans Symbols, sans-serif" font-weight="400">☻</tspan>&#160;</textPath></text>
        </g>
        <text x="116" y="118" text-anchor="middle" dominant-baseline="central" font-family="Noto Sans Symbols, sans-serif" font-size="92" fill="#1E1E1E">☻</text>
      </svg>"""


def faixa():
    palavras = ["Estratégia", "Marca", "Comunicação", "Conteúdo", "Performance"]
    itens = []
    for r in range(4):
        for i, p in enumerate(palavras):
            cls = ' class="it"' if (r * 5 + i) % 2 else ""
            itens.append(f'<span{cls}>{p}</span><span class="sym">☻</span>')
    um = "".join(itens)
    return f'<div class="faixa escuro" aria-hidden="true"><div class="faixa-trilho">{um}{um}</div></div>\n'


def video_tag(nome, rotulo):
    return (f'<div class="video"><video muted loop playsinline preload="none" data-src="/assets/video/clientes/{nome}.mp4" '
            f'poster="/assets/img/poster-{nome}.jpg" aria-label="{esc(rotulo)}"></video><span class="som" aria-hidden="true"></span></div>')


def escrever(caminho, conteudo):
    alvo = os.path.join(RAIZ, caminho)
    os.makedirs(os.path.dirname(alvo), exist_ok=True)
    with open(alvo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print("ok", caminho)


def seg_lista(seg):
    """Segmento e local em partes separadas, para a quebra no celular acontecer por sentido."""
    if " · " not in seg:
        return f'<span>{seg}</span>'
    segmento, local = seg.split(" · ", 1)
    local = ", ".join(parte.replace(" ", "\u00a0") for parte in local.split(", "))
    return f'<span>{segmento}</span><span class="local">{local}</span>'


# ---------------------------------------------------------------- Início
def pagina_inicio():
    lista = []
    for c in CASES:
        lista.append(f"""<li class="cliente">
        <div class="nome"><span class="num">{c['n']}</span><h3>{c['nome']}</h3></div>
        <p class="seg">{seg_lista(c['seg'])}</p>
        <a class="btn pequeno" href="/clientes/{c['slug']}/" aria-label="Explore o case {esc(c['nome'])}">Explore →</a>
      </li>""")
    itens = [("01", "Guia da marca", "Como a marca fala, se mostra e\nse aplica, reunido em um só lugar."),
             ("02", "Arquivos abertos", "Logo, paleta, tipografia e elementos\nprontos para qualquer equipe usar."),
             ("03", "Modelos de peças", "Bases de posts, stories, cardápios\ne materiais gráficos."),
             ("04", "Banco de imagens", "Fotos e vídeos produzidos para\na marca seguir publicando.")]
    itens_html = "".join(f'<div><p class="t"><span class="it">{n}</span>{t}</p><p>{br(d)}</p></div>' for n, t, d in itens)
    corpo = f"""{head("O'Works · Criamos e gerimos marcas estrategicamente autênticas", "/")}
<section class="claro abertura">
  <div class="wrap">
    {cabecalho('', '#contato')}
    <div class="conteudo">
      <p class="rotulo">Estúdio de direção criativa e comunicação</p>
      <h1 class="frase-marca">Criamos e gerimos marcas<br> <span class="it">estrategicamente autênticas {sym('☻')}</span></h1>
      <div class="apoio">
        <p>{APOIO}</p>
        <div class="botoes"><a class="btn" href="#clientes">Ver clientes</a><a class="btn outline" href="/estudio/">Conheça o estúdio</a></div>
      </div>
    </div>
  </div>
</section>
{faixa()}<section class="escuro sec sobre" id="sobre">
  <div class="wrap colunas">
    <div class="texto">
      <p class="rotulo">Sobre o estúdio</p>
      <h2 class="titulo">Toda marca tem<br> uma personalidade.<br> Nosso trabalho é<br> fazer ela aparecer.</h2>
      <p class="corpo">Na O'Works, toda marca começa pela estratégia. Primeiro definimos como a marca pensa, fala e se mostra. Só depois vem o conteúdo. A estética é consequência do negócio, não acaso.</p>
      <p class="corpo muted">Da primeira conversa à peça publicada, o mesmo olhar acompanha tudo. Trabalhamos como o time criativo da marca: perto, presente e com o resultado em mente.</p>
      <a class="link" href="/estudio/">Conheça o estúdio →</a>
    </div>
    <div class="visual">
      <div class="reel" role="img" aria-label="Reel com takes de produções de gastronomia da O'Works">
        <video class="ativo" muted loop playsinline preload="none" data-src="/assets/video/reel-gastronomia.mp4" poster="/assets/img/poster-reel.jpg"></video>
      </div>
      <div class="selo">{selo_svg()}</div>
    </div>
  </div>
</section>
<section class="claro sec clientes" id="clientes">
  <div class="wrap">
    <div class="clientes-topo">
      <h2>Quem já criou com a O'Works</h2>
      <p class="corpo">{INTRO}</p>
    </div>
    <ul class="lista-clientes">
      {''.join(lista)}
    </ul>
  </div>
</section>
<section class="claro sec-linha autonomia">
  <div class="wrap">
    <div class="com-linha">
      <div class="colunas">
        <div class="texto">
          <p class="rotulo">Marcas com autonomia</p>
          <h2 class="titulo">Quando o trabalho termina,<br class="d"> a marca continua.</h2>
          <p class="corpo">Cada universo visual que a O'Works cria sai com tudo o que o cliente precisa para seguir aplicando a marca: guia, arquivos essenciais abertos, modelos de peças e banco de imagens.</p>
          <p class="corpo muted">Por isso a identidade não se perde quando a equipe muda. O cliente pode trabalhar com outras pessoas e a comunicação continua alinhada, sem recomeçar do zero a cada troca.</p>
        </div>
        <div class="destaque">
          <blockquote>{CITA}</blockquote>
          <p class="muted">O quanto desse material fica com cada cliente acompanha o escopo do projeto. E, mesmo com o contrato encerrado, a O'Works segue por perto: os clientes nos procuram para realinhar o que for preciso, em assessorias pontuais.</p>
        </div>
      </div>
      <div class="itens4">{itens_html}</div>
    </div>
  </div>
</section>
{bloco_contato(com_form=True)}{fim()}"""
    escrever("index.html", corpo)


# ---------------------------------------------------------------- Estúdio
def pagina_estudio():
    servicos = [("01", "Direção criativa", "O conceito que guia a marca e dá coerência\na tudo o que ela publica, lança e mostra."),
                ("02", "Estratégia de comunicação", "Posicionamento, linha editorial e planejamento para\nque cada ação leve a marca aonde ela quer chegar."),
                ("03", "Design", "Identidade e sistemas visuais para\nredes, campanhas e peças de marca."),
                ("04", "Vídeo", "Do roteiro à edição final, com captação\nno local, equipe e equipamento próprios."),
                ("05", "Fotografia", "Produto, ambiente, pessoas e bastidores,\nna mesma linguagem da marca."),
                ("06", "Imprensa e influência", "Release, relação com a mídia e\ncuradoria de influenciadores e parceiros."),
                ("07", "Performance", "Campanhas em Meta, Google e TikTok,\ncom rastreamento e relatórios.")]
    serv = "".join(f'<li><p class="n"><span class="it">{n}</span>{t}</p><p>{br(d)}</p></li>' for n, t, d in servicos)
    etapas = [("01", "Diagnóstico", "Entender o negócio, o público, a história\nda marca e o que já existe ao redor."),
              ("02", "Conceito", "Um caminho de marca, aprovado com\no cliente antes de qualquer desenho."),
              ("03", "Universo", "Identidade, universo visual,\nlinguagem e todas as aplicações."),
              ("04", "Serviço", "A marca na rua: lançamento,\nconteúdo e comunicação contínua.")]
    et = "".join(f'<div><span class="it">{n}</span><h3>{t}</h3><p>{br(d)}</p></div>' for n, t, d in etapas)
    corpo = f"""{head("Estúdio · O'Works", "/estudio/")}
<section class="claro estudio-abertura">
  <div class="wrap">
    {cabecalho('estudio')}
    <div class="conteudo">
      <p class="rotulo">Estúdio</p>
      <h1>A gente dá forma ao que<br class="d"> a sua marca quer ser.</h1>
      <div class="dois-textos">
        <p>Na O'Works, estratégia e criação andam juntas. A gente mergulha no negócio, entende o que a marca é e para quem ela fala, e transforma isso em ideias que as pessoas veem, sentem e lembram.</p>
        <p class="muted">É assim que um vídeo, um post e uma foto deixam de ser peças soltas e passam a contar a mesma história. Trabalhamos como o time criativo da marca: perto, presente e com o resultado em mente.</p>
      </div>
    </div>
  </div>
</section>
<section class="escuro sec">
  <div class="wrap">
    <p class="rotulo" style="margin-bottom:40px">O que fazemos</p>
    <ul class="servicos">{serv}</ul>
  </div>
</section>
<section class="claro sec">
  <div class="wrap">
    <div class="topo-secao" style="margin-bottom:0">
      <div style="display:grid;gap:24px"><p class="rotulo">Como trabalhamos</p><h2 class="titulo">Do começo ao fim,<br> o mesmo olhar.</h2></div>
      <p class="muted">{COMO}</p>
    </div>
    <div class="etapas">{et}</div>
  </div>
</section>
<section class="claro sec-linha">
  <div class="wrap">
    <div class="quem linha-topo">
      <img src="/assets/img/estudio-tay.jpg" alt="Tayssi Rocha, diretora criativa e fundadora da O'Works" width="960" height="1200" loading="lazy">
      <div class="texto">
        <p class="rotulo">Quem dirige</p>
        <h2 class="titulo">Tayssi Rocha</h2>
        <p class="cargo">Diretora criativa e fundadora da O'Works</p>
        <p class="corpo">Tayssi trabalha no encontro entre estratégia e estética. Entende o que a marca precisa comunicar e cuida para que cada peça carregue essa ideia com verdade e beleza.</p>
        <p class="corpo muted">Com mais de 40 marcas no portfólio, de clínicas e restaurantes a empresas de engenharia e tecnologia, acredita que uma boa marca é reconhecida antes mesmo de aparecer o nome.</p>
      </div>
    </div>
  </div>
</section>
{bloco_contato()}{fim()}"""
    escrever("estudio/index.html", corpo)


# ---------------------------------------------------------------- Contato
def pagina_contato():
    corpo = f"""{head("Contato · O'Works", "/contato/", "Conta pra gente o que a sua marca quer ser. E-mail, WhatsApp e Instagram da O'Works.")}
<section class="escuro pagina-contato" style="padding-bottom:0">
  <div class="wrap">
    {cabecalho('contato', '#contato-form')}
    <div class="colunas">
      <div class="texto">
        <h1 class="vamos">Vamos criar algo juntos?</h1>
        <p class="conta">Conta pra gente o que<br class="d"> a sua marca quer ser.</p>
        <div class="lista-contato">
          <a href="mailto:{EMAIL}"><span class="r">E-mail</span><span class="v">{EMAIL}</span></a>
          <a href="{WHATS}" target="_blank" rel="noopener"><span class="r">WhatsApp</span><span class="v">(27) 99573-9709</span></a>
          <a href="{INSTA}" target="_blank" rel="noopener"><span class="r">Instagram</span><span class="v">@oworks.ag</span></a>
        </div>
      </div>
      <div id="contato-form" style="flex:none;max-width:100%">{formulario()}</div>
    </div>
    <div style="padding-top:120px">{rodape_links()}</div>
  </div>
</section>
{fim()}"""
    escrever("contato/index.html", corpo)


def pagina_obrigado():
    corpo = f"""{head("Obrigado · O'Works", "/obrigado/")}
<section class="escuro pagina-contato" style="padding-bottom:0;min-height:100vh">
  <div class="wrap">
    {cabecalho()}
    <div class="colunas"><div class="texto">
      <h1 class="vamos">Recebemos a sua mensagem.</h1>
      <p class="conta">Respondemos em breve {sym('☻')}</p>
      <p style="padding-top:24px"><a class="btn" href="/">Voltar para o início</a></p>
    </div></div>
    <div style="padding-top:120px">{rodape_links()}</div>
  </div>
</section>
{fim()}"""
    escrever("obrigado/index.html", corpo)


def pagina_404():
    corpo = f"""{head("Página não encontrada · O'Works", "/404.html")}
<section class="escuro pagina-contato" style="padding-bottom:0;min-height:100vh">
  <div class="wrap">
    {cabecalho()}
    <div class="colunas"><div class="texto">
      <h1 class="vamos">Essa página não existe.</h1>
      <p class="conta">Mas a O'Works continua aqui {sym('☻')}</p>
      <p style="padding-top:24px"><a class="btn" href="/">Voltar para o início</a></p>
    </div></div>
    <div style="padding-top:120px">{rodape_links()}</div>
  </div>
</section>
{fim()}"""
    escrever("404.html", corpo)


# ---------------------------------------------------------------- Cases
def luz(hexcor):
    h = hexcor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (0.299 * r + 0.587 * g + 0.114 * b) > 215


def pagina_case(i):
    c = CASES[i]
    prox = CASES[(i + 1) % len(CASES)]
    chips = "".join(f"<li>{x}</li>" for x in c["chips"])
    partes = []
    if c.get("uni"):
        cols = []
        for col in c["uni"]:
            filhos = []
            for tipo, val in col:
                if tipo == "img":
                    filhos.append(f'<img src="/assets/img/{val}" alt="Universo visual de {esc(c["nome"])}" loading="lazy">')
                else:
                    um = " uma-coluna" if len(val) <= 2 else ""
                    cores = "".join(f'<div class="cor{" borda" if luz(h) else ""}" style="background:{h};color:{t}">{n}</div>' for n, h, t in val)
                    filhos.append(f'<div class="paleta{um}" style="grid-auto-rows:1fr">{cores}</div>')
            dupla = " dupla" if len(col) > 1 else ""
            cols.append(f'<div class="uni-col{dupla}">{"".join(filhos)}</div>')
        partes.append(f"""<section class="claro sec">
  <div class="wrap">
    <div class="topo-secao"><h2>Universo visual</h2><span class="rotulo-dir">Logo, paleta e aplicações</span></div>
    <div class="uni">{''.join(cols)}</div>
  </div>
</section>""")
    if c.get("aplic"):
        a = c["aplic"]
        partes.append(f"""<section class="claro sec-linha">
  <div class="wrap">
    <div class="com-linha">
      <div class="topo-secao"><h2>{br(a['titulo'])}</h2><p>{br(a['texto'])}</p></div>
      <div class="aplic">
        <div class="grande"><img src="/assets/img/{a['imgs'][0]}" alt="Estampa do {esc(c['nome'])}" loading="lazy"></div>
        <div class="col"><img src="/assets/img/{a['imgs'][1]}" alt="Camiseta do {esc(c['nome'])}" loading="lazy"><img src="/assets/img/{a['imgs'][2]}" alt="Aplicação da marca {esc(c['nome'])}" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>""")
    midia = []
    if c.get("posts"):
        tres = " tres" if len(c["posts"]) == 3 else ""
        posts = "".join(f'<div class="post"><img src="/assets/img/{p}" alt="Post de {esc(c["nome"])} feito pela O\'Works" loading="lazy"></div>' for p in c["posts"])
        midia.append(f'<div class="linha-midia{tres}">{posts}</div>')
    vids = "".join(video_tag(v, f"Vídeo de {c['nome']} feito pela O'Works") for v in c["videos"])
    midia.append(f'<div class="linha-midia">{vids}</div>')
    rotulo_redes = "Posts e vídeos feitos pela O'Works" if c.get("posts") else "Vídeos feitos pela O'Works"
    partes.append(f"""<section class="escuro sec">
  <div class="wrap">
    <div class="topo-secao"><h2>Nas redes</h2><span class="rotulo-dir">{rotulo_redes}</span></div>
    {''.join(midia)}
  </div>
</section>""")
    partes.append(f"""<section class="claro sec proximo">
  <div class="wrap">
    <p class="rotulo">Próximo trabalho</p>
    <a href="/clientes/{prox['slug']}/"><span class="it">{prox['n']}</span> {prox['nome']} <span class="seta">→</span></a>
  </div>
</section>""")
    desc = f"{c['nome']}: {c['frase']} {c['texto']}"[:300]
    corpo = f"""{head(c['nome'] + " · O'Works", f"/clientes/{c['slug']}/", desc)}
<section class="escuro case-abertura">
  <div class="wrap">
    {cabecalho('clientes')}
    <nav class="trilha" aria-label="Você está em"><a href="/#clientes">Clientes</a><span class="sep">/</span><span>{c['nome']}</span></nav>
    <div class="colunas">
      <div class="texto">
        <p class="case-num">{c['n']}.</p>
        <h1 class="case-nome">{c['nome']}</h1>
        <p class="case-seg">{c['seg']}</p>
        <p class="case-frase">{c['frase']}</p>
        <p class="case-texto">{c['texto']}</p>
        <ul class="chips">{chips}</ul>
      </div>
      <div class="case-imagem">
        <img src="/assets/img/{c['hero']}" alt="{esc(c['nome'])}: trabalho da O'Works" width="1280" height="1440">
        <div class="papel"><span class="r">O papel da estratégia</span><strong>{c['papel']}</strong><p>{c['sub']}</p></div>
      </div>
    </div>
  </div>
</section>
{chr(10).join(partes)}
{bloco_contato()}{fim()}"""
    escrever(f"clientes/{c['slug']}/index.html", corpo)


def sitemap():
    urls = ["/", "/estudio/", "/contato/"] + [f"/clientes/{c['slug']}/" for c in CASES]
    hoje = time.strftime("%Y-%m-%d")
    linhas = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{hoje}</lastmod></url>\n" for u in urls)
    escrever("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{linhas}</urlset>\n')
    escrever("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    pagina_inicio()
    pagina_estudio()
    pagina_contato()
    pagina_obrigado()
    pagina_404()
    for k in range(len(CASES)):
        pagina_case(k)
    sitemap()
