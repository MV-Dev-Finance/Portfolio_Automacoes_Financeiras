# -*- coding: utf-8 -*-
"""Gera site (GitHub Pages), PDF e READMEs a partir de tools/data.py.
Uso:  python tools/build_site.py            (site + READMEs + REVISAR.md)
      python tools/build_site.py --pdf      (também gera o PDF; requer playwright + chromium)
Telas:  python tools/run_all.py             (regenera as imagens de demonstração)
"""
import os, sys, html, shutil, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
E = html.escape
PDF_NAME = "Portfolio_Miguel_Moura.pdf"
REPO = "Portfolio_Automacoes_Financeiras"
_G = PERFIL["github"] or "SEU-USUARIO"
PAGES = f"https://{_G.lower()}.github.io/{REPO}/"
HAS_FOTO = os.path.exists(os.path.join(ROOT, PERFIL.get("foto", "assets/foto.jpg")))
def avatar(rel="", extra=""):
    if HAS_FOTO: return f'<div class="avatar ph {extra}"><img src="{rel}{PERFIL["foto"]}" alt="{E(PERFIL["nome_curto"])}"></div>'
    return f'<div class="avatar {extra}">{PERFIL["iniciais"]}</div>'

def scr(slug, key): return f"assets/screens/{slug}__{key}.jpg"
def cover(p): return scr(p["slug"], p["cover"])
def dimg(slug): return f"assets/screens/dash__{slug}.jpg"

# ------------------------------------------------------------------ categorias de chip
def ccls(t):
    s = t.lower()
    if "sharepoint list" in s or any(k in s for k in ["sql", "postgre", "mysql", "oracle", "sqlite", "hana", "access", "dataverse"]): return "c-db"
    if any(k in s for k in ["power", "sharepoint", "teams", "docusign", "dax", "ai builder", "forms"]): return "c-pp"
    if any(k in s for k in ["python", "pandas", "numpy", "openpyxl", "xlsxwriter", "pymupdf", "sqlalchemy", "plotly", "streamlit", "regex", "decimal", "datetime"]): return "c-py"
    if any(k in s for k in ["sap", "nf-e", "sped"]): return "c-sap"
    if any(k in s for k in ["excel", "vba", "xlsx"]): return "c-xl"
    if any(k in s for k in ["html", "javascript", "css"]): return "c-web"
    return ""
def chips(items, small=False):
    return "".join(f'<span class="chip {ccls(x)}">{E(x)}</span>' for x in items)

# ------------------------------------------------------------------ uso das tecnologias
def allchips(p): return [c for v in p["camadas"].values() for c in v]
KEYS = [
    ("SQL e bancos de dados", lambda c: any(k in c.lower() for k in ["sql", "postgre", "oracle", "mysql", "hana", "access"]) and "sharepoint" not in c.lower()),
    ("Python e pandas", lambda c: any(k in c.lower() for k in ["python", "pandas"])),
    ("Streamlit", lambda c: "streamlit" in c.lower()),
    ("Excel e openpyxl", lambda c: any(k in c.lower() for k in ["excel", "openpyxl", "xlsx"])),
    ("SAP", lambda c: "sap" in c.lower()),
    ("Power BI e DAX", lambda c: any(k in c.lower() for k in ["power bi", "dax"])),
    ("Power Apps", lambda c: "power apps" in c.lower()),
    ("Power Automate", lambda c: "power automate" in c.lower()),
    ("SharePoint", lambda c: "sharepoint" in c.lower()),
    ("HTML e JavaScript", lambda c: any(k in c.lower() for k in ["html", "javascript"])),
    ("PDF e Regex", lambda c: any(k in c.lower() for k in ["pymupdf", "regex", "pdf"])),
    ("NF-e e fiscal (XML)", lambda c: any(k in c.lower() for k in ["nf-e", "livros fiscais"])),
]
def usage():
    out = []
    for name, fn in KEYS:
        n = sum(1 for p in PROJETOS if any(fn(c) for c in allchips(p)))
        if n: out.append((name, n))
    out.append(("IA em testes e revisão", sum(1 for p in PROJETOS if p.get("ia"))))
    return sorted(out, key=lambda x: -x[1])
USO = usage(); N_PROJ = len(PROJETOS); N_AUTO = sum(len(p["itens"]) for p in PROJETOS); N_DASH = len(DASH)
N_TEC = sum(len(g) for _, g in TECNOLOGIAS)
DBS = ["SQL Server", "PostgreSQL", "MySQL", "Oracle", "Azure SQL", "MS Access", "SharePoint Lists"]
def db_usage():
    out = []
    for d in DBS:
        n = sum(1 for p in PROJETOS if any(d.lower() in c.lower() for c in allchips(p)))
        if n: out.append((d, n))
    return out

ICONS = {"test": '<path d="M9 3h6M10 3v6L5 19a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 19l-5-10V3"/><path d="M7.5 15h9"/>', "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>', "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.5A8 8 0 1 1 21 12z"/>', "spark": '<path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>'}
def icon(n, s=28, c="#e9d5ff"):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

def contatos():
    o = []
    if PERFIL["linkedin"]: o.append(f'<a href="https://{PERFIL["linkedin"]}" target="_blank">LinkedIn · {E(PERFIL["linkedin"])}</a>')
    if PERFIL["email"]: o.append(f'<a href="mailto:{PERFIL["email"]}">{E(PERFIL["email"])}</a>')
    if PERFIL["github"]: o.append(f'<a href="https://github.com/{PERFIL["github"]}" target="_blank">GitHub · {E(PERFIL["github"])}</a>')
    return "".join(o)

def head(title, rel, desc="", cls="", style=""):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="{rel}assets/style.css"></head><body class="{cls}" style="{style}">"""
def nav(rel):
    nm = PERFIL["nome"].split(); idx = rel + "index.html"
    return f"""<header class="nav"><div class="wrap"><a class="brand" href="{idx}"><i>{PERFIL['iniciais']}</i>{E(PERFIL.get('nome_curto') or nm[0]+' '+nm[-1])}</a><ul>
<li><a class="l" href="{idx}#sobre">Sobre</a></li><li><a class="l" href="{idx}#dominios">Domínios</a></li><li><a class="l" href="{idx}#tecnologias">Tecnologias</a></li><li><a class="l" href="{idx}#ia">IA</a></li><li><a class="l" href="{idx}#projetos">Projetos</a></li><li><a class="l" href="{idx}#dashboards">Dashboards</a></li>
<li><a class="btn p sm" href="{rel}{PDF_NAME}">Baixar PDF</a></li></ul></div></header>"""
def foot(rel):
    return f'<footer><div class="wrap">Todas as telas são demonstrações com dados fictícios. Nenhum dado real de empregador é exibido.<br>{E(PERFIL["nome"])} · {E(PERFIL["titulo"])}</div></footer><div class="lb" id="lb"><img alt=""></div><script src="{rel}assets/app.js"></script></body></html>'

# ------------------------------------------------------------------ INDEX
def build_index():
    h = head(f"{PERFIL['nome']} · Portfólio", "", PERFIL["headline"]) + nav("")
    ms = "".join(f'<img src="{x}" alt="">' for x in [cover(PROJETOS[0]), cover(PROJETOS[2]), cover(PROJETOS[10]), cover(PROJETOS[12])])
    h += f"""<section class="hero" style="padding:0"><div class="wrap"><div><span class="eyebrow">{E(PERFIL['titulo'])}</span><h1>Contabilidade, finanças e tributos <span>transformados em dados</span>.</h1>
<p class="lead">{E(PERFIL['headline'])}</p><div class="cta"><a class="btn p" href="#projetos">Ver projetos</a><a class="btn g" href="{PDF_NAME}">Baixar portfólio em PDF</a></div>
<div class="stats"><div><b>{N_PROJ}</b><span>projetos</span></div><div><b>{N_AUTO}</b><span>rotinas automatizadas</span></div><div><b>{N_DASH}</b><span>dashboards</span></div><div><b>{N_TEC}</b><span>tecnologias</span></div></div></div>
<div class="heroimg"><div class="mosaic">{ms}</div><div class="float f1">✔ Conciliado nos dois sentidos</div><div class="float f2">Dados 100% fictícios</div></div></div></section>"""
    ct = contatos()
    h += f"""<section id="sobre"><div class="wrap"><div class="sec-h"><small>Quem sou</small><h2>Sobre mim</h2></div><div class="about"><div class="avatar-card reveal">{avatar()}<h3>{E(PERFIL['nome'])}</h3><p>{E(PERFIL['titulo'])}<br>{E(PERFIL['local'])}</p>{f'<div class="contact">{ct}</div>' if ct else ''}</div>
<div class="txt reveal">{''.join(f'<p>{E(t)}</p>' for t in PERFIL['sobre'])}<div class="quote">{E(PERFIL['diferencial'])}</div></div></div>
<div class="method">{''.join(f'<div class="card reveal"><div class="num">{i+1}</div><h4>{E(a)}</h4><p>{E(b)}</p></div>' for i, (a, b) in enumerate(METODO))}</div></div></section>"""
    cores = ["linear-gradient(90deg,#3b82f6,#22d3ee)|#3b82f6", "linear-gradient(90deg,#16a34a,#84cc16)|#16a34a", "linear-gradient(90deg,#b45309,#eab308)|#b45309", "linear-gradient(90deg,#7c3aed,#c084fc)|#7c3aed"]
    dm = "".join(f'<div class="dom reveal" style="--g:{cores[i].split("|")[0]};--c:{cores[i].split("|")[1]}"><h4>{E(t)}</h4><div class="chips">' + "".join(f'<span class="chip">{E(x)}</span>' for x in items) + "</div></div>" for i, (t, items) in enumerate(DOMINIOS))
    h += f"""<section id="dominios" style="background:#fff"><div class="wrap"><div class="sec-h"><small>O que eu transformo em dados</small><h2>Domínios</h2><p>Contábil, financeiro, fiscal e tributário: tudo que tem regra, volume e prazo pode virar base, automação e painel.</p></div><div class="doms">{dm}</div></div></section>"""
    tg = "".join(f'<div class="tg reveal"><h4>{E(t)}</h4><div class="chips">{chips(items)}</div></div>' for t, items in TECNOLOGIAS)
    mx = max(c for _, c in USO)
    ub = "".join(f'<div class="ub"><b style="font-weight:600">{E(n)}</b><div class="t"><i style="width:{c/mx*100:.0f}%"></i></div><span class="n">{c} de {N_PROJ}</span></div>' for n, c in USO)
    dbu = " ".join(f'<span class="chip c-db">{E(n)} · {c}</span>' for n, c in db_usage())
    lg = "".join(f'<span><i style="background:{c}"></i>{n}</span>' for n, c in [("Bancos e SQL", "#6366f1"), ("Python", "#3b82f6"), ("Power Platform", "#a855f7"), ("SAP e fiscal", "#0ea5e9"), ("Excel", "#22c55e"), ("Web", "#f97316")])
    h += f"""<section id="tecnologias" class="techsec"><div class="wrap"><div class="sec-h"><small>O que eu uso</small><h2>Tecnologias</h2><p>Bancos de dados e SQL no centro, com Python, Power Platform, BI e ferramentas de ERP e fiscal ao redor.</p></div><div class="legend">{lg}</div><div class="tech">{tg}</div>
<div class="usage"><h3>Onde cada tecnologia foi aplicada</h3><div class="ubars">{ub}</div><div style="margin-top:22px"><h3 style="font-size:15px;margin-bottom:10px">Bancos de dados nos projetos</h3><div class="chips">{dbu}</div></div></div></div></section>"""
    ip = "".join(f'<div class="ip reveal"><div class="ic">{icon(ic)}</div><h4>{E(t)}</h4><p>{E(d)}</p></div>' for ic, t, d in IA["pilares"])
    pr = "".join(f"<span>{E(x)}</span>" for x in IA["principios"])
    h += f"""<section id="ia" class="iasec"><div class="wrap"><div class="sec-h"><small>IA aplicada</small><h2>{E(IA['titulo'])}</h2><p>{E(IA['intro'])}</p></div><div class="iap">{ip}</div><div class="iapr">{pr}</div>
<div class="iash"><figure><img src="assets/screens/ia__testes.jpg" alt="Cenários de teste gerados com IA"><figcaption>Cenários de teste sintéticos para validar a regra antes de usar dados reais</figcaption></figure><figure><img src="assets/screens/ia__assistente.jpg" alt="Assistente dentro do dashboard"><figcaption>Assistente integrado ao dashboard: explica variações e mostra a fonte</figcaption></figure></div></div></section>"""
    flt = '<button class="fbtn on" data-f="all">Todos</button>' + "".join(f'<button class="fbtn" data-f="{E(a)}">{E(a)}</button>' for a in AREAS)
    cards = ""
    for p in PROJETOS:
        th = p["theme"]; tops = ([c for c in p["camadas"]["dados"] if "SQL" in c or "Share" in c][:1] + p["camadas"]["proc"][:2] + p["camadas"]["ui"][:1])[:4]
        cards += f"""<a class="pcard reveal" data-area="{E(p['area'])}" href="projects/{p['slug']}.html" style="--a1:{th['a1']};--pb:{th['pbg']}"><div class="th"><span class="no">{p['n']:02d}</span><img src="{cover(p)}" alt="{E(p['title'])}"><span class="kd">{E(p['kind'])}</span></div>
<div class="bd"><span class="ar">{E(p['area'])}</span><h3>{E(p['title'])}</h3><p>{E(p['tag'])}</p><div class="chips">{chips(tops)}</div><span class="more">Ver lógica e solução →</span></div></a>"""
    h += f"""<section id="projetos"><div class="wrap"><div class="sec-h"><small>Portfólio</small><h2>Projetos</h2><p>Cada projeto tem sua própria identidade visual, o problema de negócio, a solução com dados e a stack completa.</p></div><div class="filters">{flt}</div><div class="pgrid">{cards}</div></div></section>"""
    gi = "".join(f'<div class="gi" data-full="{dimg(s)}"><img src="{dimg(s)}" alt="{E(t)}"><div class="cp">{E(t)}<span>{E(tema)} · {E(a)}</span></div></div>' for s, t, tema, a in DASH)
    h += f"""<section id="dashboards" class="galsec"><div class="wrap"><div class="sec-h"><small>Galeria</small><h2>Dashboards criados em temas diferentes</h2><p>Planejamento, contabilidade, fiscal, financeiro e investimentos, cada um com seu estilo. Clique para ampliar. Dados fictícios.</p></div><div class="gal">{gi}</div></div></section>"""
    fl = "".join(f'<div class="st"><b>{i+1}. {E(a)}</b><span>{E(b)}</span></div>' for i, (a, b) in enumerate([("Fontes", "SAP, Excel, PDFs, XML fiscais e bancos SQL"), ("Dados", "SQL e pandas: limpeza, chaves e cruzamentos"), ("Regras", "Contábeis, financeiras e fiscais em código"), ("Apps e painéis", "Streamlit, Power Platform, Power BI e HTML"), ("Entrega", "Planilhas, alertas, documentos e dashboards")]))
    h += f"""<section class="pipe"><div class="wrap"><div class="sec-h"><small style="color:#7dd3fc">Como trabalho</small><h2>Do dado bruto à decisão</h2><p>O mesmo caminho se repete em todas as automações.</p></div><div class="flow">{fl}</div></div></section>"""
    h += f"""<section id="contato"><div class="wrap"><div class="cta-box"><h2>Vamos conversar?</h2><p>Se a vaga mistura contabilidade, finanças, fiscal e dados, este portfólio mostra como eu trabalho.</p><div class="row"><a class="btn d" href="{PDF_NAME}">Baixar portfólio em PDF</a></div>{f'<div style="margin-top:18px;display:flex;gap:18px;justify-content:center;flex-wrap:wrap;font-weight:600">{ct.replace("<a ", "<a style=color:#06112a ")}</div>' if ct else ''}</div></div></section>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(h + foot(""))

# ------------------------------------------------------------------ PROJETO
def frame_html(p):
    th_l = p["layout"]["frame"]
    imgs = "".join(f'<img class="{"on" if j==0 else ""}" src="../{scr(p["slug"], k)}" alt="{E(l)}">' for j, (k, l) in enumerate(p["screens"]))
    bar = f'<div class="bar"><i></i><i></i><i></i><em>{E(p["slug"])}.app</em></div>' if th_l == "browser" else ""
    tabs = "".join(f'<button class="tab {"on" if j==0 else ""}" data-i="{j}">{E(l)}</button>' for j, (k, l) in enumerate(p["screens"]))
    return (f'<div class="tabs">{tabs}</div>' if len(p["screens"]) > 1 else ""), f'<div class="frame">{bar}{imgs}</div>'

def biz_html(p, v):
    rules = p["regras"]
    if v == "cards":
        return f'<div class="biz-cards"><div class="cardp"><h4>Como funciona o processo</h4><p>{E(p["contexto"])}</p><div class="pain"><b>O problema</b>{E(p["dor"])}</div></div><div class="cardp"><h4>Regras que governam o processo</h4><ul class="rl">{"".join(f"<li>{E(r)}</li>" for r in rules)}</ul></div></div>'
    if v == "banner":
        return f'<div class="biz-banner"><div class="pb"><small>O problema</small>{E(p["dor"])}</div><p class="ld">{E(p["contexto"])}</p><div class="r4">{"".join(f"<div class=cardp><b>R{i+1}</b><p>{E(r)}</p></div>" for i, r in enumerate(rules))}</div></div>'
    return f'<div class="biz-split"><div class="sticky"><div class="cardp"><h4>Como funciona o processo</h4><p>{E(p["contexto"])}</p><div class="pain"><b>O problema</b>{E(p["dor"])}</div></div></div><div><div class="cardp" style="padding:20px 20px 8px"><h4>Regras que governam o processo</h4></div><ol class="nl" style="margin-top:12px">{"".join(f"<li>{E(r)}</li>" for r in rules)}</ol></div></div>'

def steps_html(p, v):
    ps = p["passos"]
    if v == "timeline": return '<div class="tl">' + "".join(f'<div class="s"><div class="dot">{k+1}</div><div class="tx"><h4>{E(a)}</h4><p>{E(b)}</p></div></div>' for k, (a, b) in enumerate(ps)) + "</div>"
    if v == "grid": return '<div class="sg5">' + "".join(f'<div class="tx"><div class="dot">{k+1}</div><h4>{E(a)}</h4><p>{E(b)}</p></div>' for k, (a, b) in enumerate(ps)) + "</div>"
    if v == "zigzag": return '<div class="zig">' + "".join(f'<div class="zi"><div class="dot">{k+1}</div><div class="tx"><h4>{E(a)}</h4><p>{E(b)}</p></div></div>' for k, (a, b) in enumerate(ps)) + "</div>"
    return '<div class="sbig">' + "".join(f'<div class="sb"><b>{k+1:02d}</b><div><h4>{E(a)}</h4><p>{E(b)}</p></div></div>' for k, (a, b) in enumerate(ps)) + "</div>"

def stack_html(p, v):
    items = [(nome, p["camadas"][k]) for k, nome in CAMADAS_ORDEM if p["camadas"].get(k)]
    if v == "rows": return '<div class="layers">' + "".join(f'<div class="layer"><div class="lb2">{E(n)}</div><div class="chips">{chips(it)}</div></div>' for n, it in items) + "</div>"
    if v == "tiles": return '<div class="tiles">' + "".join(f'<div class="tile"><h5>{E(n)}</h5><div class="chips">{chips(it)}</div></div>' for n, it in items) + "</div>"
    return '<div class="fl2">' + "".join(f'<div class="fc"><h5>{E(n)}</h5><div class="chips">{chips(it)}</div></div>' for n, it in items) + "</div>"

def build_project(i, p):
    th = p["theme"]; lay = p["layout"]; rel = "../"
    prev = PROJETOS[i - 1] if i > 0 else None; nxt = PROJETOS[i + 1] if i < len(PROJETOS) - 1 else None
    cls = "proj" + (" pdark" if th["mode"] == "dark" else "")
    st = f"--a1:{th['a1']};--a2:{th['a2']};--hero:{th['hero']};--pbg:{th['pbg']}"
    h = head(f"{p['title']} · {PERFIL['nome']}", rel, p["tag"], cls, st) + nav(rel)
    ch = f'<span class="chip">{E(p["area"])}</span>' + "".join(f'<span class="chip">{E(x)}</span>' for x in p["itens"])
    tabs, fr = frame_html(p); hv = lay["hero"]
    crumbs = f'<div class="crumbs"><a href="../index.html">Início</a> / <a href="../index.html#projetos">Projetos</a> / {p["n"]:02d}</div>'
    txt = f'{crumbs}<span class="kindtag">{E(p["kind"])}</span><h1>{E(p["title"])}</h1><p class="lead">{E(p["tag"])}</p><div class="chips">{ch}</div>'
    if hv == "split":
        h += f'<header class="hero2 hero-split"><div class="wrap grid2"><div>{txt}</div><div>{tabs}<div class="tilt">{fr}</div><div class="note">Tela de demonstração com dados fictícios</div></div></div></header><div class="wrap">'
    else:
        big = f'<div class="big">{p["n"]:02d}</div>' if hv == "poster" else ""
        h += f'<header class="hero2 hero-{hv}">{big}<div class="wrap">{txt}</div></header><div class="wrap"><div class="shot">{tabs}{fr}<div class="note">Tela de demonstração com dados fictícios</div></div>'
    n = 1
    def blk(title, content):
        nonlocal n; s = f'<div class="blk"><div class="bh"><div class="n">{n:02d}</div><h2>{title}</h2></div>{content}</div>'; n += 1; return s
    h += blk("Lógica do negócio", biz_html(p, lay["biz"]))
    h += blk("Como resolvi com dados", steps_html(p, lay["steps"]))
    h += blk("Tecnologias utilizadas", stack_html(p, lay["stack"]))
    h += blk("Funcionalidades", '<div class="feats">' + "".join(f'<div class="feat">{E(f)}</div>' for f in p["feats"]) + "</div>")
    if RESULTADOS.get(p["slug"]):
        h += blk("Resultados", '<div class="res">' + "".join(f'<div class="cardp"><b>{E(v)}</b><span>{E(k)}</span></div>' for k, v in RESULTADOS[p["slug"]]) + "</div>")
    if p.get("ia"): h += blk("IA aplicada neste projeto", f'<div class="iab"><i>{icon("spark",28)}</i><div><b>Como usei IA</b><p>{E(p["ia"])}</p></div></div>')
    comps = list(dict.fromkeys(p["comp"] + p["camadas"]["proc"][:2] + p["camadas"]["ui"][:1]))
    h += f'<div class="who">{avatar(rel)}<div><h3>{E(PERFIL["nome"])}</h3><p>{E(p.get("papel", PAPEL))}</p><div class="chips">{"".join(f"<span class=chip>{E(c)}</span>" for c in comps)}</div></div><a class="btn p" href="../index.html#sobre">Sobre mim</a></div>'
    h += f'<div class="pnav">{f"<a href=%s.html><small>← Anterior</small><b>%s</b></a>" % (prev["slug"], E(prev["title"])) if prev else "<span style=flex:1></span>"}{f"<a class=r href=%s.html><small>Próximo →</small><b>%s</b></a>" % (nxt["slug"], E(nxt["title"])) if nxt else "<span style=flex:1></span>"}</div></div><div style="height:60px"></div>'
    os.makedirs(os.path.join(ROOT, "projects"), exist_ok=True)
    open(os.path.join(ROOT, "projects", p["slug"] + ".html"), "w", encoding="utf-8").write(h + foot(rel))

JS = """document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');const f=b.dataset.f;document.querySelectorAll('.pcard').forEach(c=>{c.style.display=(f==='all'||c.dataset.area===f)?'':'none'})}));
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));t.classList.add('on');document.querySelectorAll('.frame img').forEach((im,i)=>im.classList.toggle('on',i==t.dataset.i))}));
const lb=document.getElementById('lb');
document.querySelectorAll('.gi,.iash img').forEach(el=>el.addEventListener('click',()=>{const src=el.dataset.full||el.getAttribute('src');lb.querySelector('img').src=src;lb.classList.add('on')}));
lb.addEventListener('click',()=>lb.classList.remove('on'));document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
"""

# ------------------------------------------------------------------ README
def badge(t):
    m = {"Python": ("Python", "3776AB", "python"), "Streamlit": ("Streamlit", "FF4B4B", "streamlit"), "pandas": ("pandas", "150458", "pandas"), "SQL Server": ("SQL_Server", "CC2927", "microsoftsqlserver"),
         "PostgreSQL": ("PostgreSQL", "4169E1", "postgresql"), "MySQL": ("MySQL", "4479A1", "mysql"), "Oracle": ("Oracle", "F80000", "oracle"), "Power BI": ("Power_BI", "F2C811", "powerbi"), "Power Apps": ("Power_Apps", "742774", "powerapps"),
         "Power Automate": ("Power_Automate", "0066FF", "powerautomate"), "SharePoint": ("SharePoint", "0078D4", "microsoftsharepoint"), "SAP": ("SAP", "0FAAFF", "sap"), "HTML": ("HTML%2FJS", "E34F26", "html5"), "Excel": ("Excel", "217346", "microsoftexcel")}
    for k, (a, c, l) in m.items():
        if k.lower() in t.lower(): return f"![{k}](https://img.shields.io/badge/{a}-{c}?style=for-the-badge&logo={l}&logoColor=white)"
    return None
def badges_for(p):
    seen = []
    for c in allchips(p):
        b = badge(c)
        if b and b not in seen: seen.append(b)
    return " ".join(seen)
def mermaid(p):
    ids = []
    for key, nome in CAMADAS_ORDEM:
        it = p["camadas"].get(key)
        if it: ids.append((key, nome + "<br/>" + "<br/>".join(re.sub(r"[()\"]", "", x) for x in it[:3])))
    return "flowchart LR\n" + "".join(f'    {k}["{lab}"]\n' for k, lab in ids) + "    " + " --> ".join(k for k, _ in ids)

def project_md(p):
    rg = "\n".join(f"- {r}" for r in p["regras"]); ps = "\n".join(f"{k+1}. **{a}**: {b}" for k, (a, b) in enumerate(p["passos"]))
    lay = "| Camada | Tecnologias |\n|---|---|\n" + "\n".join(f"| {n} | {', '.join(p['camadas'][k])} |" for k, n in CAMADAS_ORDEM if p["camadas"].get(k))
    ft = "\n".join(f"- {f}" for f in p["feats"]); shots = "\n\n".join(f"**{l}**\n\n![{l}](../../{scr(p['slug'], k)})" for k, l in p["screens"])
    res = ("\n## Resultados\n\n| Indicador | Resultado |\n|---|---|\n" + "\n".join(f"| {k} | {v} |" for k, v in RESULTADOS[p["slug"]]) + "\n") if RESULTADOS.get(p["slug"]) else ""
    return f"""# {p['title']}

> {p['tag']}

**Tipo de tela:** {p['kind']}

{badges_for(p)}

[Ver esta página no site]({PAGES}projects/{p['slug']}.html) · [Voltar ao portfólio](../../README.md)

## 1. Lógica do negócio

{p['contexto']}

**Regras que governam o processo**

{rg}

> **O problema:** {p['dor']}

## 2. Como resolvi com dados

{ps}

## 3. Tecnologias utilizadas

```mermaid
{mermaid(p)}
```

{lay}

## 4. Funcionalidades

{ft}
{res}
## IA aplicada neste projeto

{p['ia']}

## Telas

{shots}

## Quem fez

**{PERFIL['nome']}**: {p.get('papel', PAPEL)}

> Todas as telas usam dados sintéticos de uma empresa fictícia.
"""

def main_md():
    us = "| Tecnologia | Projetos |\n|---|---|\n" + "\n".join(f"| {n} | {c} de {N_PROJ} |" for n, c in USO)
    dm = "\n".join(f"| **{t}** | {' · '.join(items)} |" for t, items in DOMINIOS); tc = "\n".join(f"| **{t}** | {' · '.join(items)} |" for t, items in TECNOLOGIAS)
    rows = "\n".join(f"| {p['n']:02d} | [{p['title']}](projects/{p['slug']}/README.md) | {p['kind']} | {p['area']} |" for p in PROJETOS)
    th = ""
    for i, p in enumerate(PROJETOS):
        th += f"<td align='center' width='25%'><a href='projects/{p['slug']}/README.md'><img src='{cover(p)}' width='100%'><br><b>{p['n']:02d} · {p['title']}</b></a></td>"
        if i % 4 == 3 and i < len(PROJETOS) - 1: th += "</tr><tr>"
    gal = ""
    for i, (s, t, tema, a) in enumerate(DASH):
        gal += f"<td align='center' width='33%'><img src='{dimg(s)}' width='100%'><br><sub>{t} · {tema}</sub></td>"
        if i % 3 == 2 and i < len(DASH) - 1: gal += "</tr><tr>"
    met = "\n".join(f"{i+1}. **{a}**: {b}" for i, (a, b) in enumerate(METODO)); ia = "\n".join(f"- **{t}:** {d}" for _, t, d in IA["pilares"])
    mapa = "\n".join(f"| {', '.join(p['itens'])} | {p['title']} |" for p in PROJETOS)
    ct = []
    if PERFIL["linkedin"]: ct.append(f"[LinkedIn](https://{PERFIL['linkedin']})")
    if PERFIL["email"]: ct.append(f"[{PERFIL['email']}](mailto:{PERFIL['email']})")
    foto = f'<p align="center"><img src="assets/foto.jpg" width="150" height="150" alt="{PERFIL["nome_curto"]}"></p>\n' if HAS_FOTO else ""
    return f"""{foto}<h1 align="center">{PERFIL['nome']}</h1>
<h3 align="center">{PERFIL['titulo']}</h3>
<p align="center">{PERFIL['headline']}</p>
<p align="center"><a href="{PDF_NAME}"><b>Baixar portfólio em PDF</b></a> · <a href="{PAGES}"><b>Ver site</b></a></p>
<p align="center"><b>{N_PROJ}</b> projetos · <b>{N_AUTO}</b> rotinas automatizadas · <b>{N_DASH}</b> dashboards · <b>{N_TEC}</b> tecnologias</p>

> As telas são **demonstrações com dados fictícios**. Nenhum dado real de empregador é exibido.

## Sobre mim

{chr(10).join(PERFIL['sobre'])}

> {PERFIL['diferencial']}

{' · '.join(ct)}

## Como eu trabalho

{met}

## Domínios

| Área | O que transformo em dados |
|---|---|
{dm}

## Tecnologias

| Grupo | Ferramentas |
|---|---|
{tc}

### Onde cada tecnologia foi aplicada

{us}

## Inteligência artificial no meu trabalho

{IA['intro']}

{ia}

## Projetos

<table><tr>{th}</tr></table>

| # | Projeto | Tipo de tela | Área |
|---|---|---|---|
{rows}

## Dashboards em temas diferentes

<table><tr>{gal}</tr></table>

## Mapa: o que foi automatizado × projeto

| Automação | Projeto |
|---|---|
{mapa}

## Sobre os dados

> Todas as telas deste repositório usam **dados sintéticos** gerados por script (`tools/`), com uma empresa fictícia. Não há dados, contas, processos, fornecedores ou documentos reais de nenhum empregador.

## Como regenerar tudo

```bash
pip install playwright && playwright install chromium
python tools/run_all.py              # telas
python tools/build_site.py --pdf     # site, READMEs e PDF a partir de tools/data.py
```
"""

def profile_md():
    g = PERFIL["github"] or "SEU-USUARIO"; feat = [PROJETOS[0], PROJETOS[10], PROJETOS[13]]
    cols = "".join(f"<td align='center' width='33%'><a href='https://github.com/{g}/{REPO}/tree/main/projects/{p['slug']}'><img src='assets/{p['slug']}.jpg' width='100%'><br><b>{p['title']}</b></a><br><sub>{p['tag']}</sub></td>" for p in feat)
    bs = " ".join(b for b in [badge(t) for t in ["Python", "Streamlit", "SQL Server", "PostgreSQL", "Power BI", "Power Apps", "Power Automate", "SharePoint", "SAP", "Excel"]] if b)
    ct = []
    if PERFIL["linkedin"]: ct.append(f"- LinkedIn: [{PERFIL['linkedin']}](https://{PERFIL['linkedin']})")
    if PERFIL["email"]: ct.append(f"- E-mail: {PERFIL['email']}")
    dm = "\n".join(f"| **{t}** | {' · '.join(items[:7])} |" for t, items in DOMINIOS)
    foto = f'<p align="center"><img src="assets/foto.jpg" width="150" height="150" style="border-radius:50%" alt="{PERFIL["nome_curto"]}"></p>\n' if HAS_FOTO else ""
    return f"""{foto}<h1 align="center">{PERFIL['nome']}</h1>
<h3 align="center">{PERFIL['titulo']}</h3>
<p align="center">{PERFIL['headline']}</p>

<p align="center"><a href="{PAGES}"><b>Ver portfólio completo</b></a> · <a href="https://github.com/{g}/{REPO}/raw/main/{PDF_NAME}"><b>Baixar PDF</b></a></p>

---

### Sobre mim

{PERFIL['sobre'][0]}

{PERFIL['sobre'][1]}

### Projetos em destaque

<table><tr>{cols}</tr></table>

### O que transformo em dados

| Área | Exemplos |
|---|---|
{dm}

### Tecnologias

{bs}

{chr(10).join(ct)}

<sub>Todos os projetos públicos usam dados fictícios.</sub>
"""

def revisar_md():
    rows = "\n".join(f"| {p['n']:02d} {p['title']} | " + " · ".join(f"**{n}:** {', '.join(p['camadas'][k])}" for k, n in CAMADAS_ORDEM if p["camadas"].get(k)) + " |" for p in PROJETOS)
    return f"""# Revise antes de publicar

## O que veio do seu histórico (alta confiança)
- **App Digital Inventory:** Power Apps, Power Automate, SharePoint e bases do SAP, sem Python. Funcionalidades, fluxos e a ajuda do Copilot em código e cenários de teste vieram das suas conversas.
- **Resultados do Digital Inventory** (bipagem 2 h → 1 h, inventário 5 h → 3 h, custo R$ 0): vieram do formulário do desafio de inovação e são aproximados. Confirme antes de publicar.
- **Extrator de extratos (projeto 08):** PyMuPDF, openpyxl, mais de 90 PDFs e cerca de 20 bancos. O AI Builder foi testado antes e não funcionou com muitos layouts.
- **SQL Server:** você tem acesso a um banco SQL Server. Os demais bancos (PostgreSQL, MySQL, Oracle, SQLite, SAP HANA, Azure SQL, Access, Dataverse) **foram adicionados a pedido** e precisam ser confirmados.

## O que é sugestão minha (confirme)
- A **stack por projeto** abaixo, principalmente onde aparece SQL Server, Power Automate, Power BI e SharePoint.
- Os projetos **13 a 16** (apuração, ICMS, reforma tributária, migração): textos, regras e telas são **demonstrativos**. Ajuste ao que você de fato implementou.
- A lista de **domínios** (forecast, budget, SPED, aging etc.): remova o que não for real.
- A seção de **IA**: descreve geração de cenários de teste, revisão de código e assistentes em apps/dashboards. Ajuste ao que já está em uso.
- Valores, alíquotas e percentuais nas telas de ICMS e do simulador da reforma são **ilustrativos**. O calendário da reforma (2026 a 2033) segue a EC 132/2023 e a LC 214/2025.

| Projeto | Stack atual no portfólio |
|---|---|
{rows}

## Também preencher
- **Foto:** `python tools/foto.py sua-foto.jpg` (recorta em quadrado) e depois `python tools/build_site.py --pdf`. Sem foto, aparecem as iniciais.
- `RESULTADOS` com números reais (antes → depois) para os demais projetos.
- Confirmar com a empresa o que pode ser divulgado.

Depois de editar `tools/data.py`, rode `python tools/build_site.py --pdf`.
"""

# ------------------------------------------------------------------ PDF
PDF_CSS = """
@page{size:1280px 800px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Liberation Sans','Segoe UI',Arial,sans-serif;color:#0f172a;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:1280px;height:800px;overflow:hidden;position:relative;page-break-after:always;background:#f6f8fc;padding:38px 46px}
.dark{background:radial-gradient(800px 420px at 85% -10%,rgba(59,130,246,.4),transparent 60%),#0a1226;color:#fff}
.grad{background:linear-gradient(135deg,#3b82f6,#22d3ee)}.gt{background:linear-gradient(135deg,#3b82f6,#22d3ee);-webkit-background-clip:text;background-clip:text;color:transparent}
.eb{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:#2563eb;font-weight:700}.dark .eb{color:#7dd3fc}
h1{font-size:46px;letter-spacing:-1.5px;line-height:1.05}h2{font-size:30px;letter-spacing:-.8px}
.big .chip{font-size:13px;padding:5px 12px;margin:0 6px 7px 0}
.chip{display:inline-block;font-size:11px;padding:3px 9px;border-radius:20px;background:#eaf1fd;color:#1e3a8a;border:1px solid #d4e1f8;margin:0 5px 5px 0;font-weight:600}
.c-db{background:#e0e7ff;color:#3730a3;border-color:#c7d2fe}.c-pp{background:#f3e8ff;color:#6b21a8;border-color:#e9d5ff}.c-py{background:#dbeafe;color:#1e40af;border-color:#bfdbfe}.c-sap{background:#e0f2fe;color:#075985;border-color:#bae6fd}.c-xl{background:#dcfce7;color:#166534;border-color:#bbf7d0}.c-web{background:#ffedd5;color:#9a3412;border-color:#fed7aa}
.card{background:#fff;border:1px solid #e5ebf5;border-radius:14px;padding:16px 18px}
.frame{border-radius:12px;overflow:hidden;border:1px solid #dbe3f0;box-shadow:0 14px 40px rgba(10,18,38,.2);background:#fff}.frame img{display:block;width:100%}
.ft{position:absolute;left:46px;right:46px;bottom:14px;display:flex;justify-content:space-between;font-size:10.5px;color:#8b9ab5}.dark .ft{color:#7d8fb3}
.h4{font-size:11px;letter-spacing:1.3px;text-transform:uppercase;color:var(--a1,#2563eb);font-weight:700;margin-bottom:7px}
.num{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:7px;font-weight:700;font-size:12px;color:#fff;background:linear-gradient(135deg,var(--a1,#3b82f6),var(--a2,#22d3ee))}
"""
def pimg(rel):
    """Cópia reduzida da imagem para o PDF."""
    from PIL import Image
    src = os.path.join(ROOT, rel); dst = os.path.join(ROOT, "_pdfimg", rel.replace("/", "_"))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if not os.path.exists(dst):
        im = Image.open(src).convert("RGB"); w = 1100
        if im.width > w: im = im.resize((w, int(im.height * w / im.width)))
        im.save(dst, quality=80, optimize=True)
    return "file://" + dst

def pdf_avatar():
    if HAS_FOTO:
        return f'<img src="{pimg(PERFIL["foto"])}" style="width:140px;height:140px;border-radius:36px;object-fit:cover;display:block;margin:0 auto 14px;border:3px solid rgba(255,255,255,.25)">'
    return f'<div class="grad" style="width:92px;height:92px;border-radius:28px;margin:0 auto 14px;display:grid;place-items:center;font-size:34px;font-weight:800;color:#06112a">{PERFIL["iniciais"]}</div>'

def pdf_html():
    ct = " · ".join(x for x in [PERFIL["linkedin"], PERFIL["email"], ("github.com/" + PERFIL["github"]) if PERFIL["github"] else ""] if x)
    base = 7; total = base + len(PROJETOS)
    def ft(n): return f'<div class="ft"><span>{E(PERFIL["nome"])} · {E(PERFIL["titulo"])}</span><span>{ct + " · " if ct else ""}{n}/{total}</span></div>'
    pages = []
    mos = "".join(f'<div class="frame"><img src="{pimg(x)}" style="height:210px;object-fit:cover;object-position:top left"></div>' for x in [cover(PROJETOS[0]), cover(PROJETOS[2]), cover(PROJETOS[10]), cover(PROJETOS[12])])
    st = lambda v, l: f'<div><div class="gt" style="font-size:38px;font-weight:700">{v}</div><div style="font-size:12px;color:#93a6c8">{l}</div></div>'
    pages.append(f"""<div class="pg dark"><div style="display:grid;grid-template-columns:1fr 560px;gap:40px;height:100%;align-items:center"><div><div class="eb">{E(PERFIL['titulo'])}</div><h1 style="margin:16px 0 14px">{E(PERFIL['nome'])}</h1>
<div style="font-size:23px;font-weight:700;margin-bottom:12px">Contabilidade, finanças e tributos <span class="gt">transformados em dados</span>.</div><div style="font-size:15.5px;color:#b8c6e0;max-width:520px;line-height:1.5">{E(PERFIL['headline'])}</div>
<div style="display:flex;gap:30px;margin-top:32px">{st(N_PROJ,'projetos')}{st(N_AUTO,'rotinas automatizadas')}{st(N_DASH,'dashboards')}{st(N_TEC,'tecnologias')}</div><div style="margin-top:30px;font-size:12px;color:#8fa3c8">Telas de demonstração com dados 100% fictícios.</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{mos}</div></div>{ft(1)}</div>""")
    sobre = "".join(f'<p style="font-size:15.5px;color:#26344f;line-height:1.58;margin-bottom:13px">{E(t)}</p>' for t in PERFIL["sobre"])
    met = "".join(f'<div class="card" style="padding:20px"><span class="num">{i+1}</span><div style="font-weight:700;margin:10px 0 4px;font-size:15.5px">{E(a)}</div><div style="font-size:13px;color:#5b6b86;line-height:1.5">{E(b)}</div></div>' for i, (a, b) in enumerate(METODO))
    pages.append(f"""<div class="pg"><div class="eb">Quem sou</div><h2>Sobre mim</h2><div style="display:grid;grid-template-columns:320px 1fr;gap:34px;margin-top:20px"><div class="dark" style="border-radius:18px;padding:28px;text-align:center">{pdf_avatar()}<div style="font-size:18px;font-weight:700">{E(PERFIL['nome'])}</div><div style="font-size:12.5px;color:#a9bbdc;margin-top:4px">{E(PERFIL['titulo'])}</div></div>
<div>{sobre}<div style="border-left:4px solid #3b82f6;background:#eef4ff;padding:14px 18px;border-radius:0 12px 12px 0;color:#1e3a8a;font-weight:600;font-size:15px;line-height:1.5">{E(PERFIL['diferencial'])}</div></div></div>
<div class="h4" style="margin-top:34px">Como eu trabalho</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{met}</div>{ft(2)}</div>""")
    cores = ["#3b82f6", "#16a34a", "#b45309", "#7c3aed"]
    dm = "".join(f'<div class="card" style="padding:16px 18px;border-top:5px solid {cores[i]}"><div class="h4" style="color:{cores[i]}">{E(t)}</div>' + "".join(f'<span class="chip">{E(x)}</span>' for x in items) + "</div>" for i, (t, items) in enumerate(DOMINIOS))
    pages.append(f"""<div class="pg big"><div class="eb">O que eu transformo em dados</div><h2>Domínios</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px">{dm}</div>{ft(3)}</div>""")
    tg = "".join(f'<div class="card" style="padding:14px 16px"><div class="h4">{E(t)}</div>' + "".join(f'<span class="chip {ccls(x)}">{E(x)}</span>' for x in items) + "</div>" for t, items in TECNOLOGIAS)
    mx = max(c for _, c in USO)
    ub = "".join(f'<div style="display:grid;grid-template-columns:160px 1fr 52px;gap:10px;align-items:center;font-size:12px;margin-bottom:6px"><b>{E(n)}</b><div style="height:8px;background:#e6edf8;border-radius:8px"><div class="grad" style="height:8px;border-radius:8px;width:{c/mx*100:.0f}%"></div></div><span style="color:#64748b;text-align:right">{c}/{N_PROJ}</span></div>' for n, c in USO)
    pages.append(f"""<div class="pg big"><div class="eb">O que eu uso</div><h2>Tecnologias</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">{tg}</div><div class="h4" style="margin-top:16px">Onde cada tecnologia foi aplicada</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:0 36px">{ub}</div>{ft(4)}</div>""")
    ip = "".join(f'<div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);border-radius:14px;padding:16px 18px"><div>{icon(ic,26)}</div><div style="font-weight:700;font-size:16px;margin:6px 0 5px">{E(t)}</div><div style="font-size:12.5px;color:#d8ccff;line-height:1.5">{E(d)}</div></div>' for ic, t, d in IA["pilares"])
    pages.append(f"""<div class="pg" style="background:radial-gradient(800px 400px at 85% 0,rgba(124,58,237,.4),transparent 60%),#0f0a24;color:#fff"><div class="eb" style="color:#c4b5fd">IA aplicada</div><h2>{E(IA['titulo'])}</h2><div style="font-size:14px;color:#c4b5fd;margin:8px 0 16px;max-width:900px">{E(IA['intro'])}</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{ip}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px"><div class="frame"><img src="{pimg('assets/screens/ia__testes.jpg')}" style="height:330px;object-fit:cover;object-position:top"></div><div class="frame"><img src="{pimg('assets/screens/ia__assistente.jpg')}" style="height:330px;object-fit:cover;object-position:top"></div></div>{ft(5)}</div>""")
    gi = "".join(f'<div style="background:#fff;border-radius:10px;overflow:hidden;border:1px solid #dbe3f0"><img src="{pimg(dimg(s))}" style="width:100%;height:158px;object-fit:cover;object-position:top left;display:block"><div style="padding:6px 10px;font-size:11.5px;font-weight:700;display:flex;justify-content:space-between">{E(t)}<span style="font-weight:400;color:#64748b;font-size:10px">{E(tema)}</span></div></div>' for s, t, tema, a in DASH)
    pages.append(f"""<div class="pg"><div class="eb">Galeria</div><h2>Dashboards em temas diferentes</h2><div style="font-size:13px;color:#5b6b86;margin:4px 0 14px">Planejamento, contabilidade, fiscal, financeiro e investimentos · dados fictícios</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">{gi}</div>{ft(6)}</div>""")
    ov = "".join(f'<div style="background:#fff;border-radius:10px;overflow:hidden;border:1px solid #e5ebf5;border-top:4px solid {p["theme"]["a1"]}"><img src="{pimg(cover(p))}" style="width:100%;height:96px;object-fit:cover;object-position:top left;display:block"><div style="padding:6px 9px"><div style="font-size:9px;color:{p["theme"]["a1"]};font-weight:700;letter-spacing:.8px;text-transform:uppercase">{p["n"]:02d} · {E(p["kind"])}</div><div style="font-size:11.5px;font-weight:700;line-height:1.2;margin-top:2px">{E(p["title"])}</div></div></div>' for p in PROJETOS)
    pages.append(f"""<div class="pg"><div class="eb">Portfólio</div><h2>Visão geral dos {N_PROJ} projetos</h2><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:11px;margin-top:14px">{ov}</div>{ft(7)}</div>""")
    LC = {"fontes": "#64748b", "dados": "#6366f1", "proc": "#3b82f6", "ui": "#14b8a6", "saida": "#10b981", "auto": "#f59e0b"}
    for k, p in enumerate(PROJETOS):
        th = p["theme"]; dk = th["mode"] == "dark"; bg = th["pbg"] if dk else "#f6f8fc"; fg = "#e5e7eb" if dk else "#0f172a"; sub = "#9ca3af" if dk else "#4a5a78"; cd = "#111827" if dk else "#fff"; bd = "#1f2937" if dk else "#e5ebf5"
        rg = "".join(f'<li style="margin-bottom:3px">{E(x)}</li>' for x in p["regras"][:4])
        ps = "".join(f'<div style="display:grid;grid-template-columns:30px 1fr;gap:8px;margin-bottom:6px"><span class="num" style="width:24px;height:24px">{j+1}</span><div style="font-size:12px;line-height:1.4"><b>{E(a)}.</b> <span style="color:{sub}">{E(b)}</span></div></div>' for j, (a, b) in enumerate(p["passos"]))
        lay = "".join(f'<div style="display:grid;grid-template-columns:104px 1fr;gap:6px;margin-bottom:4px"><div style="font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.3px;padding-top:5px;white-space:nowrap;color:{LC[key]}">■ {E(nome if key != "auto" else "Automação")}</div><div>' + "".join(f'<span class="chip {ccls(x)}" style="font-size:10px;padding:2px 8px;margin-bottom:3px">{E(x)}</span>' for x in p["camadas"][key]) + "</div></div>" for key, nome in CAMADAS_ORDEM if p["camadas"].get(key))
        res = ""
        if RESULTADOS.get(p["slug"]): res = '<div style="display:flex;gap:8px;margin-top:8px">' + "".join(f'<div style="background:{cd};border:1px solid {bd};border-radius:10px;padding:6px 10px"><div style="font-size:14px;font-weight:700;color:{th["a1"]}">{E(v)}</div><div style="font-size:9.5px;color:{sub}">{E(kk)}</div></div>' for kk, v in RESULTADOS[p["slug"]]) + "</div>"
        iab = f'<div style="margin-top:8px;background:linear-gradient(135deg,#1e1b4b,#4c1d95);color:#fff;border-radius:10px;padding:8px 12px;font-size:11px;line-height:1.4"><b style="color:#c4b5fd;font-size:9.5px;letter-spacing:1px;text-transform:uppercase">IA neste projeto</b><br>{E(p["ia"])}</div>' if p.get("ia") else ""
        shots = "".join(f'<div class="frame" style="{"" if j==0 else "margin-top:6px"}"><img src="{pimg(scr(p["slug"], kk))}" style="height:{360 if len(p["screens"])==1 else (128 if RESULTADOS.get(p["slug"]) else 158)}px;object-fit:cover;object-position:top left"></div>' for j, (kk, _) in enumerate(p["screens"][:2]))
        txtcol = f'<div><div class="card" style="background:{cd};border-color:{bd};margin-bottom:10px;padding:13px 16px;color:{fg}"><div class="h4">Lógica do negócio</div><div style="font-size:12.6px;line-height:1.48;color:{fg}">{E(p["contexto"])}</div><ul style="font-size:11.5px;margin:7px 0 0 16px;line-height:1.35;color:{sub}">{rg}</ul><div style="margin-top:8px;background:{"#2a1a14" if dk else "#fff7ed"};border:1px solid {"#7c2d12" if dk else "#fed7aa"};color:{"#fdba74" if dk else "#9a3412"};border-radius:8px;padding:6px 10px;font-size:11px;line-height:1.35"><b>Problema:</b> {E(p["dor"])}</div></div><div class="card" style="background:{cd};border-color:{bd};padding:13px 16px;color:{fg}"><div class="h4">Como resolvi com dados</div>{ps}</div></div>'
        viscol = f'<div>{shots}<div class="card" style="background:{cd};border-color:{bd};margin-top:10px;padding:11px 14px;color:{fg}"><div class="h4">Tecnologias utilizadas</div>{lay}</div>{res}{iab}</div>'
        cols = "55% 1fr" if k % 2 == 0 else "1fr 55%"; body = txtcol + viscol if k % 2 == 0 else viscol + txtcol
        pages.append(f"""<div class="pg" style="background:{bg};color:{fg};padding:0;--a1:{th['a1']};--a2:{th['a2']}"><div style="height:92px;background:linear-gradient(120deg,{th['hero']},{th['a1']});padding:16px 46px;color:#fff;display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;opacity:.85;font-weight:700">{p['n']:02d} · {E(p['area'])} · {E(p['kind'])}</div><div style="font-size:26px;font-weight:700;letter-spacing:-.6px;line-height:1.12;margin-top:3px">{E(p['title'])}</div></div><div style="font-size:10.5px;padding:5px 12px;border-radius:20px;background:rgba(255,255,255,.18);white-space:nowrap">DADOS FICTÍCIOS</div></div>
<div style="display:grid;grid-template-columns:{cols};gap:22px;padding:16px 46px 0">{body}</div>{ft(base + 1 + k)}</div>""")
    return f"<html><head><meta charset='utf-8'><style>{PDF_CSS}</style></head><body>{''.join(pages)}</body></html>"

def build_pdf():
    from playwright.sync_api import sync_playwright
    tmp = os.path.join(ROOT, "_print.html"); open(tmp, "w", encoding="utf-8").write(pdf_html())
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME_PATH") or None, args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1280, "height": 800}); pg.goto("file://" + tmp); pg.wait_for_timeout(800)
        bad = pg.evaluate("""()=>{const out=[];document.querySelectorAll('.pg').forEach((p,i)=>{let m=0;p.querySelectorAll('*').forEach(e=>{if(e.closest('.ft'))return;const b=e.getBoundingClientRect().bottom-p.getBoundingClientRect().top;if(b>m)m=b});const f=p.querySelector('.ft').getBoundingClientRect().top-p.getBoundingClientRect().top;if(m>f-2)out.push([i+1,Math.round(m-f)])});return out}""")
        print("Páginas do PDF com conteúdo encostando no rodapé (pág, px):", bad)
        pg.pdf(path=os.path.join(ROOT, PDF_NAME), width="1280px", height="800px", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0")); b.close()
    os.remove(tmp); shutil.rmtree(os.path.join(ROOT, "_pdfimg"), ignore_errors=True)

def cleanup_screens():
    used = set()
    for p in PROJETOS:
        for k, _ in p["screens"]: used.add(f"{p['slug']}__{k}.jpg")
    for s, *_ in DASH: used.add(f"dash__{s}.jpg")
    used |= {"ia__testes.jpg", "ia__assistente.jpg"}
    d = os.path.join(ROOT, "assets", "screens")
    for f in os.listdir(d):
        if f not in used: os.remove(os.path.join(d, f)); print("removido (não usado):", f)
    miss = [u for u in used if not os.path.exists(os.path.join(d, u))]
    if miss: print("FALTAM imagens:", miss)

def main():
    open(os.path.join(ROOT, "assets", "app.js"), "w", encoding="utf-8").write(JS)
    cleanup_screens(); build_index()
    for i, p in enumerate(PROJETOS): build_project(i, p)
    for p in PROJETOS:
        d = os.path.join(ROOT, "projects", p["slug"]); os.makedirs(d, exist_ok=True); open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(project_md(p))
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(main_md()); open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    open(os.path.join(ROOT, "REVISAR.md"), "w", encoding="utf-8").write(revisar_md())
    pdir = os.path.abspath(os.path.join(ROOT, "..", "perfil-github")); os.makedirs(os.path.join(pdir, "assets"), exist_ok=True)
    for p in (PROJETOS[0], PROJETOS[10], PROJETOS[13]): shutil.copy(os.path.join(ROOT, cover(p)), os.path.join(pdir, "assets", p["slug"] + ".jpg"))
    if HAS_FOTO: shutil.copy(os.path.join(ROOT, PERFIL["foto"]), os.path.join(pdir, "assets", "foto.jpg"))
    open(os.path.join(pdir, "README.md"), "w", encoding="utf-8").write(profile_md())
    if "--pdf" in sys.argv: build_pdf()
    print("ok", N_PROJ, N_AUTO, N_TEC, USO[:4])

if __name__ == "__main__":
    main()
