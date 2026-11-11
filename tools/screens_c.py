# -*- coding: utf-8 -*-
"""Galeria de dashboards em temas diferentes + telas da seção de IA. Dados fictícios."""
import random
from kit import *
from screens_a import tg

def kpi_dark(items, acc):
    return "".join(f'<div class=kc><span>{a}</span><b style="color:{c}">{b}</b><i>{d}</i></div>' for a, b, d, c in items)

# 1 · Forecast × Budget (dark neon)
def d_forecast():
    css = """body{background:#070b17;color:#e2e8f0;padding:26px 34px}.h{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}h1{font-size:24px;letter-spacing:2px;text-transform:uppercase}h1 span{color:#22d3ee}.tg span{font-size:11px;border:1px solid #1e2a44;border-radius:20px;padding:6px 14px;margin-left:8px;color:#94a3b8}.tg .on{background:#22d3ee;color:#04121a;border-color:#22d3ee;font-weight:700}
.k{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-bottom:16px}.kc{background:linear-gradient(160deg,#0d1427,#0a1020);border:1px solid #1b2745;border-radius:14px;padding:13px 16px}.kc span{font-size:10px;letter-spacing:1.4px;text-transform:uppercase;color:#64748b}.kc b{display:block;font-size:26px;margin:5px 0 2px;text-shadow:0 0 18px currentColor}.kc i{font-style:normal;font-size:11px;color:#64748b}
.g{display:grid;grid-template-columns:1.8fr 1fr;gap:16px;margin-bottom:16px}.p{background:#0b1226;border:1px solid #1b2745;border-radius:16px;padding:16px}.p h3{font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:#64748b;margin-bottom:10px}
table{width:100%;font-size:12px}th{color:#64748b;text-align:left;font-size:10px;letter-spacing:1px;text-transform:uppercase;padding:7px;border-bottom:1px solid #1b2745}td{padding:7px;border-bottom:1px solid #121b33}.n{text-align:right;font-family:'Liberation Mono',monospace}"""
    mo = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    bud = [100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 146]; act = [98, 106, 107, 115, 118, 121, 123, 130, None, None, None, None]; fc = [98, 106, 107, 115, 118, 121, 123, 130, 135, 139, 144, 150]
    d = [(m, b, a if a else 0, f) for m, b, a, f in zip(mo, bud, act, fc)]
    ch = line([(m, b, f) for m, b, a, f in d], ["#475569", "#e879f9"], 800, 280, "#64748b", "#16213d", area=True, dashed=(0,), markers=False, mfill="#070b17") 
    ch2 = line([(m, a) for m, b, a, f in d[:8]], ["#22d3ee"], 800, 280, "#64748b", "#16213d", markers=True, mfill="#070b17")
    rows = "".join(f"<tr><td>{a}</td><td class=n>{b}</td><td class=n>{c}</td><td class=n style='color:{'#34d399' if v>=0 else '#fb7185'}'>{'+' if v>=0 else ''}{v:.1f}%</td></tr>".replace(".", ",") for a, b, c, v in [("Receita", "R$ 148,2 mi", "R$ 151,0 mi", 1.9), ("Custos operacionais", "R$ 61,0 mi", "R$ 63,4 mi", -3.9), ("Despesas comerciais", "R$ 18,4 mi", "R$ 17,9 mi", 2.7), ("EBITDA", "R$ 52,1 mi", "R$ 53,2 mi", 2.1), ("CAPEX", "R$ 22,0 mi", "R$ 24,6 mi", -11.8)])
    body = f"""<div class=h><h1>Forecast <span>×</span> Budget · FY2025</h1><div class=tg><span>Mês</span><span class=on>Acumulado</span><span>Ano</span></div></div>
<div class=k>{kpi_dark([("Receita YTD","R$ 959 mi","+1,9% vs budget","#22d3ee"),("EBITDA YTD","R$ 331 mi","+2,1% vs budget","#a3e635"),("Forecast do ano","R$ 1.561 mi","+2,6% vs budget","#e879f9"),("Desvio de custos","−3,9%","acima do budget","#fb7185"),("Atingimento","96,8%","do budget do ano","#facc15")],"")}</div>
<div class=g><div class=p><h3>Budget · Forecast · Realizado (R$ mi)</h3><div style="position:relative;height:280px">{ch}<div style="position:absolute;left:0;top:0">{ch2.replace('stroke="#16213d"','stroke="transparent"')}</div></div></div><div class=p style="text-align:center"><h3>Atingimento do budget</h3>{gauge(96.8,300,"#22d3ee","#16213d","#e2e8f0","do budget acumulado")}<div style="margin-top:14px">{hbars([("Receita",101.9),("EBITDA",102.1),("Custos",103.9),("CAPEX",111.8)],360,"#e879f9","#94a3b8","#16213d",lambda v:f"{v:.1f}%".replace(".",","),rowh=30,labw=70)}</div></div></div>
<div class=p><h3>Variações por linha · acumulado</h3><table><tr><th>Linha</th><th class=n>Budget</th><th class=n>Realizado</th><th class=n>Desvio</th></tr>{rows}</table></div>"""
    return doc(body, css, 1400, 860)

# 2 · DRE executiva (editorial)
def d_dre():
    css = """body{background:#f8f4ea;color:#0b2545;padding:34px 44px;font-family:'Liberation Serif',Georgia,serif}.h{border-bottom:3px double #b8860b;padding-bottom:10px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:flex-end}h1{font-size:34px;letter-spacing:-.5px}.h span{font-family:'Liberation Sans',Arial;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#8a6d1a}
.g{display:grid;grid-template-columns:1.5fr 1fr;gap:30px}.p{background:#fffdf7;border:1px solid #e7dcc0;padding:20px}.p h3{font-family:'Liberation Sans',Arial;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#8a6d1a;margin-bottom:10px}
table{width:100%;font-size:14px}td{padding:8px 4px;border-bottom:1px solid #eee2c3}td.n{text-align:right;font-family:'Liberation Sans',Arial;font-size:13px}tr.b td{font-weight:700;border-top:2px solid #0b2545}.v{color:#166534}.x{color:#991b1b}
.m{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:20px}.m div{text-align:center;border-top:3px solid #b8860b;padding-top:10px}.m b{display:block;font-size:34px}.m span{font-family:'Liberation Sans',Arial;font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:#8a6d1a}"""
    wf = waterfall([("Receita bruta", 100, "t"), ("Deduções", -14, "d"), ("Custos", -39, "d"), ("Despesas", -22, "d"), ("EBITDA", 25, "t"), ("D&A", -7, "d"), ("Financeiro", -3, "d"), ("IR/CSLL", -5, "d"), ("Lucro líquido", 10, "t")], 780, 360, "#166534", "#991b1b", "#0b2545", "#0b2545", "#e7dcc0", lambda v: f"{v:g}", 11)
    rows = "".join(f"<tr class='{c}'><td>{a}</td><td class=n>{b}</td><td class=n>{d}</td><td class='n {'v' if e>=0 else 'x'}'>{'+' if e>=0 else ''}{e:.1f}%</td></tr>".replace(".", ",") for a, b, d, e, c in [("Receita líquida", "86,0", "84,2", 2.1, "b"), ("Custo dos serviços", "(39,0)", "(38,1)", -2.3, ""), ("Lucro bruto", "47,0", "46,1", 2.0, "b"), ("Despesas operacionais", "(22,0)", "(22,4)", 1.8, ""), ("EBITDA", "25,0", "23,7", 5.5, "b"), ("Lucro líquido", "10,0", "9,1", 9.9, "b")])
    body = f"""<div class=h><h1>Demonstração do Resultado · 3T25</h1><span>Visão executiva · R$ milhões</span></div><div class=g><div class=p><h3>Da receita bruta ao lucro líquido</h3>{wf}</div><div class=p><h3>Realizado × orçado</h3><table><tr><td></td><td class=n><i>Real</i></td><td class=n><i>Orç.</i></td><td class=n><i>Var.</i></td></tr>{rows}</table></div></div>
<div class=m><div><b>29,1%</b><span>Margem EBITDA</span></div><div><b>54,7%</b><span>Margem bruta</span></div><div><b>11,6%</b><span>Margem líquida</span></div></div>"""
    return doc(body, css, 1400, 780)

# 3 · Apuração de tributos (laranja)
def d_tributos():
    css = """body{background:#fff;color:#1c1917;padding:28px 36px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#78716c;margin:4px 0 18px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff7ed;border-radius:16px;padding:14px 16px;border:1px solid #fed7aa}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#c2410c}.kc b{display:block;font-size:25px;margin-top:4px;color:#7c2d12}
.g{display:grid;grid-template-columns:420px 1fr 300px;gap:16px;margin-bottom:16px}.p{background:#fff;border:1px solid #f5e1d0;border-radius:16px;padding:16px;box-shadow:0 6px 20px rgba(194,65,12,.07)}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#c2410c;margin-bottom:10px}
table{width:100%;font-size:12px}th{text-align:left;font-size:10.5px;text-transform:uppercase;color:#9a3412;padding:7px;border-bottom:2px solid #fed7aa}td{padding:7px;border-bottom:1px solid #fff1e6}.n{text-align:right}.c{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #fff1e6;font-size:12.5px}.c b{color:#c2410c}"""
    dn = donut([("ICMS", 38), ("PIS/COFINS", 22), ("ISS", 8), ("IRPJ/CSLL", 24), ("Outros", 8)], ["#ea580c", "#f59e0b", "#fb923c", "#78716c", "#d6d3d1"], 190, .6, "#44403c", None, 420)
    mo = ["Abr", "Mai", "Jun", "Jul", "Ago", "Set"]
    ch = bars([(m, a, b) for m, a, b in zip(mo, [4.1, 4.3, 4.0, 4.6, 4.4, 4.8], [3.2, 3.3, 3.1, 3.5, 3.4, 3.7])], ["#ea580c", "#a8a29e"], 560, 230, "#78716c", "#f5e6da", series=["Débitos", "Créditos"], bw=.6)
    uf = "".join(f"<tr><td>{u}</td><td class=n>{brl(d)}</td><td class=n>{brl(c)}</td><td class=n>{brl(d-c)}</td><td>{st}</td></tr>" for u, d, c, st in [("SP", 2840500, 2166600, tg("A conciliar", "a")), ("RJ", 1120400, 902310, tg("Apurado", "g")), ("MG", 980220, 804100, tg("Apurado", "g")), ("BA", 640300, 598200, tg("Recolhido", "b")), ("PR", 502110, 410780, tg("Apurado", "g"))])
    venc = "".join(f"<div class=c><span>{a}</span><b>{b}</b></div>" for a, b in [("ICMS · 10/10", "R$ 724 mil"), ("PIS/COFINS · 25/10", "R$ 664 mil"), ("ISS · 10/10", "R$ 65 mil"), ("IRPJ/CSLL · 31/10", "R$ 402 mil"), ("Retenções · 20/10", "R$ 88 mil")])
    body = f"""<h1>Apuração de tributos · setembro</h1><div class=s>Débitos e créditos por tributo, conciliação com o razão e calendário de vencimentos · dados fictícios</div>
<div class=k><div class=kc><span>Imposto a recolher</span><b>R$ 1,94 mi</b></div><div class=kc><span>Créditos aproveitados</span><b>R$ 3,70 mi</b></div><div class=kc><span>Carga sobre a receita</span><b>11,8%</b></div><div class=kc><span>Itens a conciliar</span><b>2</b></div></div>
<div class=g><div class=p><h3>Composição do imposto</h3>{dn}</div><div class=p><h3>Débitos × créditos (R$ mi)</h3>{ch}</div><div class=p><h3>Vencimentos</h3>{venc}</div></div>
<div class=p><h3>ICMS por UF</h3><table><tr><th>UF</th><th class=n>Débito</th><th class=n>Crédito</th><th class=n>Saldo a recolher</th><th>Status</th></tr>{uf}</table></div>"""
    return doc(body, css, 1400, 860)

# 4 · Fluxo de caixa (mint)
def d_caixa():
    css = """body{background:#ecfdf5;color:#064e3b;padding:28px 36px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#047857;margin:4px 0 16px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:18px;padding:14px 16px;box-shadow:0 8px 22px rgba(5,150,105,.12)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#047857}.kc b{display:block;font-size:25px;margin-top:4px}
.g{display:grid;grid-template-columns:1.7fr 1fr;gap:16px;margin-bottom:16px}.p{background:#fff;border-radius:18px;padding:16px;box-shadow:0 8px 22px rgba(5,150,105,.12)}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#047857;margin-bottom:10px}"""
    wk = [(f"S{i}", a, b) for i, (a, b) in enumerate([(6.2, 5.1), (5.8, 6.4), (7.1, 5.6), (6.6, 7.3), (7.4, 6.1), (6.9, 6.0), (7.8, 6.6), (7.2, 7.5)], 1)]
    ch = line([(a, b, c) for a, b, c in wk], ["#059669", "#f43f5e"], 760, 250, "#047857", "#d1fae5", series=["Entradas", "Saídas"], mfill="#ecfdf5")
    R = random.Random(4); days = [[R.choice([0, 0, 1, 2, 3, 4]) for _ in range(7)] for _ in range(5)]
    hm = heat(days, ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5"], ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"], 420, 220, lambda i, j, v: ["#d1fae5", "#a7f3d0", "#6ee7b7", "#34d399", "#059669"][v], "#047857", 12, 5, lambda v: "", 52)
    top = hbars([("Folha", 4.2), ("Fornecedores", 3.6), ("Tributos", 2.9), ("Aluguéis", 1.4), ("Serviços TI", 1.1)], 440, "#f43f5e", "#064e3b", "#d1fae5", lambda v: f"R$ {v:.1f} mi".replace(".", ","), rowh=32, labw=100)
    body = f"""<h1>Fluxo de caixa · próximas 8 semanas</h1><div class=s>Entradas, saídas e saldo projetado · dados fictícios</div><div class=k><div class=kc><span>Saldo inicial</span><b>R$ 18,4 mi</b></div><div class=kc><span>Entradas previstas</span><b style="color:#059669">R$ 54,9 mi</b></div><div class=kc><span>Saídas previstas</span><b style="color:#e11d48">R$ 50,6 mi</b></div><div class=kc><span>Saldo projetado</span><b>R$ 22,7 mi</b></div></div>
<div class=g><div class=p><h3>Entradas × saídas por semana (R$ mi)</h3>{ch}</div><div class=p><h3>Calendário de pagamentos</h3>{hm}</div></div><div class=p><h3>Maiores saídas do período</h3>{top}</div>"""
    return doc(body, css, 1400, 860)

# 5 · Contingências (dark purple)
def d_conting():
    css = """body{background:#12081f;color:#ede9fe;padding:28px 36px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#c4b5fd;opacity:.8;margin:4px 0 18px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:linear-gradient(160deg,#1e1038,#160a2b);border:1px solid #3b1f6b;border-radius:16px;padding:14px 16px}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#a78bfa}.kc b{display:block;font-size:26px;margin-top:4px;color:#f5d0fe}
.g{display:grid;grid-template-columns:1fr 1fr;gap:16px}.p{background:#1a0d30;border:1px solid #3b1f6b;border-radius:18px;padding:18px}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:#c4b5fd;margin-bottom:12px}"""
    R = random.Random(6); M = [[R.randint(0, 9) for _ in range(5)] for _ in range(5)]
    pal = ["#4c1d95", "#6d28d9", "#7c3aed", "#a21caf", "#be185d", "#9f1239"]
    hm = heat(M, ["Muito alto", "Alto", "Médio", "Baixo", "Muito baixo"], ["Remota", "Pouco prov.", "Possível", "Provável", "Quase certa"], 620, 340, lambda i, j, v: pal[min(5, (4 - i + j) // 2 + (1 if v > 5 else 0))], "#c4b5fd", 15)
    tm = treemap([("Tributária", 9450, "#7c3aed", "R$ 9,5 mi"), ("Trabalhista", 6120, "#a21caf", "R$ 6,1 mi"), ("Cível", 3210, "#be185d", "R$ 3,2 mi"), ("Regulatória", 1240, "#4c1d95", "R$ 1,2 mi")], 620, 340, 6, 14)
    body = f"""<h1>Contingências · mapa de risco</h1><div class=s>Probabilidade × impacto e exposição por natureza · dados fictícios</div><div class=k><div class=kc><span>Processos</span><b>412</b></div><div class=kc><span>Provisão (provável)</span><b>R$ 20,0 mi</b></div><div class=kc><span>Divulgação (possível)</span><b>R$ 58,4 mi</b></div><div class=kc><span>Reclassificações</span><b>7</b></div></div>
<div class=g><div class=p><h3>Mapa de calor</h3>{hm}</div><div class=p><h3>Exposição por natureza</h3>{tm}</div></div>"""
    return doc(body, css, 1400, 780)

# 6 · CAPEX minimal
def d_capex():
    css = """body{background:#fff;color:#111827;padding:44px 64px;font-family:'Liberation Sans',Arial}h1{font-size:34px;font-weight:300;letter-spacing:-1px}h1 b{font-weight:700}.s{font-size:13px;color:#9ca3af;margin:6px 0 34px}
.g{display:grid;grid-template-columns:230px 1fr;gap:60px}.k{margin-bottom:30px}.k b{display:block;font-size:44px;font-weight:300;letter-spacing:-2px}.k span{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#9ca3af}.k.b b{color:#2563eb}
.r{display:grid;grid-template-columns:130px 1fr 70px;gap:16px;align-items:center;padding:13px 0;border-bottom:1px solid #f3f4f6;font-size:13px}.t{height:6px;background:#f3f4f6;border-radius:6px;position:relative}.t i{position:absolute;left:0;top:0;bottom:0;background:#111827;border-radius:6px}.t u{position:absolute;top:-5px;width:2px;height:16px;background:#2563eb}.v{text-align:right;font-weight:700}.v.x{color:#dc2626}"""
    rows = ""
    for n, o, r in [("PRJ-301 Rede", 92, 100), ("PRJ-305 Datacenter", 88, 82), ("PRJ-312 Licenças", 120, 100), ("PRJ-318 Imóveis", 64, 70), ("PRJ-322 Segurança", 97, 100), ("PRJ-327 Integração", 54, 60), ("PRJ-333 Dados", 108, 100), ("PRJ-341 Plataforma", 75, 80)]:
        d = o - r; rows += f"<div class=r><span>{n}</span><div class=t><i style='width:{min(o,100)}%'></i><u style='left:{r}%'></u></div><span class='v {'x' if d>5 else ''}'>{o}%</span></div>"
    body = f"""<h1>CAPEX <b>por projeto</b></h1><div class=s>Realizado (barra) × orçado (marcador azul) · % do orçamento · dados fictícios</div><div class=g><div><div class=k><b>R$ 104 mi</b><span>Realizado</span></div><div class=k><b>R$ 100 mi</b><span>Orçado</span></div><div class="k b"><b>+4,0%</b><span>Variação</span></div><div class=k><b>3</b><span>Justificativas pendentes</span></div></div><div>{rows}</div></div>"""
    return doc(body, css, 1400, 780)

# 7 · Reforma tributária (gradiente)
def d_reforma():
    css = """body{background:linear-gradient(120deg,#052e16,#14532d 45%,#1e3a8a);color:#fff;padding:30px 40px}h1{font-size:28px;letter-spacing:-.5px}.s{font-size:13px;opacity:.8;margin:4px 0 20px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:16px;padding:14px 16px;backdrop-filter:blur(6px)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#bbf7d0}.kc b{display:block;font-size:25px;margin-top:4px;color:#fef08a}
.g{display:grid;grid-template-columns:1.6fr 1fr;gap:16px}.p{background:rgba(255,255,255,.95);color:#14532d;border-radius:18px;padding:18px}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#15803d;margin-bottom:10px}.c{display:flex;justify-content:space-between;font-size:13px;padding:9px 0;border-bottom:1px solid #dcfce7}.c b{color:#1e3a8a}"""
    yrs = [str(y) for y in range(2026, 2034)]
    ch = bars([(y, a, b) for y, a, b in zip(yrs, [100, 100, 100, 90, 80, 70, 60, 0], [0, 0, 0, 10, 20, 30, 40, 100])], ["#94a3b8", "#facc15"], 760, 300, "#14532d", "#dcfce7", stacked=True, series=["ICMS/ISS", "IBS"], bw=.55)
    body = f"""<h1>Reforma tributária · acompanhamento da transição</h1><div class=s>CBS, IBS e Imposto Seletivo × tributos atuais · calendário 2026–2033</div><div class=k><div class=kc><span>2026</span><b>CBS 0,9% · IBS 0,1%</b></div><div class=kc><span>2027</span><b>PIS/Cofins extintos</b></div><div class=kc><span>2029–2032</span><b>ICMS/ISS 90→60%</b></div><div class=kc><span>2033</span><b>Regime pleno</b></div></div>
<div class=g><div class=p><h3>Participação dos sistemas por ano (%)</h3>{ch}</div><div class=p><h3>Itens monitorados na base</h3><div class=c><span>Documentos com campos CBS/IBS</span><b>98,2%</b></div><div class=c><span>Produtos com NCM validado</span><b>94,7%</b></div><div class=c><span>Serviços com NBS</span><b>88,1%</b></div><div class=c><span>Operações com regra de crédito</span><b>91,0%</b></div><div class=c><span>Pendências de cadastro</span><b>1.204</b></div></div></div>"""
    return doc(body, css, 1400, 780)

# 8 · Aging contas a pagar (azul claro)
def d_aging():
    css = """body{background:#eff6ff;color:#1e3a8a;padding:28px 36px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#3b82f6;margin:4px 0 16px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:16px;padding:14px 16px;box-shadow:0 8px 22px rgba(37,99,235,.10);border-left:6px solid var(--c)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#3b82f6}.kc b{display:block;font-size:24px;margin-top:4px}
.g{display:grid;grid-template-columns:1.8fr 1fr;gap:16px}.p{background:#fff;border-radius:18px;padding:18px;box-shadow:0 8px 22px rgba(37,99,235,.10)}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#2563eb;margin-bottom:12px}.row{display:grid;grid-template-columns:120px 1fr 70px;gap:10px;align-items:center;margin-bottom:11px;font-size:12px}.st{display:flex;height:22px;border-radius:6px;overflow:hidden}.st i{display:block;height:100%}"""
    cols = ["#22c55e", "#facc15", "#fb923c", "#ef4444", "#7f1d1d"]
    R = random.Random(2); rows = ""
    for n in ["Fornecedor A", "Fornecedor B", "Fornecedor C", "Fornecedor D", "Fornecedor E", "Fornecedor F", "Fornecedor G", "Fornecedor H"]:
        vs = [R.randint(20, 60), R.randint(5, 25), R.randint(2, 15), R.randint(0, 10), R.randint(0, 6)]; t = sum(vs)
        rows += f"<div class=row><span>{n}</span><div class=st>{''.join(f'<i style=width:{v/t*100:.1f}%;background:{c}></i>' for v, c in zip(vs, cols))}</div><b>R$ {t/10:.1f} mi</b></div>".replace(".", ",", 1) if False else f"<div class=row><span>{n}</span><div class=st>{''.join(f'<i style=width:{v/t*100:.1f}%;background:{c}></i>' for v, c in zip(vs, cols))}</div><b>R$ {t/10:.1f} mi</b></div>"
    dn = donut([("A vencer", 58), ("1–30 dias", 21), ("31–60", 11), ("61–90", 6), ("> 90", 4)], cols, 200, .6, "#1e3a8a", "R$ 38 mi", 360)
    lg = "".join(f"<span style='font-size:11px;margin-right:14px'><i style='display:inline-block;width:10px;height:10px;border-radius:3px;background:{c};margin-right:5px'></i>{l}</span>" for l, c in zip(["A vencer", "1–30", "31–60", "61–90", "> 90"], cols))
    body = f"""<h1>Contas a pagar · aging</h1><div class=s>Saldo em aberto por faixa de vencimento · dados fictícios</div><div class=k><div class=kc style="--c:#2563eb"><span>Saldo em aberto</span><b>R$ 38,2 mi</b></div><div class=kc style="--c:#22c55e"><span>A vencer</span><b>R$ 22,1 mi</b></div><div class=kc style="--c:#fb923c"><span>Vencido até 60 dias</span><b>R$ 12,2 mi</b></div><div class=kc style="--c:#ef4444"><span>Vencido &gt; 60 dias</span><b>R$ 3,9 mi</b></div></div>
<div class=g><div class=p><h3>Top fornecedores por faixa</h3>{lg}<div style="margin-top:14px">{rows}</div></div><div class=p><h3>Distribuição</h3>{dn}</div></div>"""
    return doc(body, css, 1400, 780)

# 9 · Orçamento por centro de custo (treemap pastel)
def d_orc():
    css = """body{background:#fdf4ff;color:#581c87;padding:28px 36px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#a21caf;margin:4px 0 16px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:18px;padding:14px 16px;box-shadow:0 8px 22px rgba(162,28,175,.10)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#a21caf}.kc b{display:block;font-size:24px;margin-top:4px}
.g{display:grid;grid-template-columns:1.4fr 1fr;gap:16px}.p{background:#fff;border-radius:18px;padding:16px;box-shadow:0 8px 22px rgba(162,28,175,.10)}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#a21caf;margin-bottom:10px}"""
    tm = treemap([("Operações", 31, "#f0abfc", "R$ 31 mi · 96%"), ("Tecnologia", 22, "#c4b5fd", "R$ 22 mi · 104%"), ("Comercial", 17, "#fda4af", "R$ 17 mi · 91%"), ("Financeiro", 11, "#a5f3fc", "R$ 11 mi · 99%"), ("RH", 8, "#fde68a", "R$ 8 mi · 88%"), ("Jurídico", 6, "#bbf7d0", "R$ 6 mi · 102%"), ("Marketing", 5, "#fed7aa", "R$ 5 mi · 93%")], 760, 420, 6, 15, "#4a044e")
    mo = ["Abr", "Mai", "Jun", "Jul", "Ago", "Set"]
    ch = line([(m, a, b) for m, a, b in zip(mo, [14, 15.2, 15.9, 17.1, 18.0, 19.1], [14.5, 15.5, 16.5, 17.5, 18.5, 19.5])], ["#c026d3", "#94a3b8"], 520, 250, "#a21caf", "#f5d0fe", dashed=(1,), series=["Realizado", "Orçado"], mfill="#fff")
    body = f"""<h1>Orçamento por centro de custo</h1><div class=s>Peso de cada área e consumo do orçamento · dados fictícios</div><div class=k><div class=kc><span>Orçamento anual</span><b>R$ 100 mi</b></div><div class=kc><span>Consumido</span><b>R$ 96,6 mi</b></div><div class=kc><span>Acima do orçado</span><b style="color:#be123c">2 áreas</b></div><div class=kc><span>Saldo</span><b>R$ 3,4 mi</b></div></div>
<div class=g><div class=p><h3>Tamanho = orçamento · texto = consumo</h3>{tm}</div><div class=p><h3>Realizado × orçado (R$ mi)</h3>{ch}</div></div>"""
    return doc(body, css, 1400, 780)

# IA 1 · cenários de teste
def ia_testes():
    css = """body{background:#faf5ff;color:#3b0764;padding:30px 40px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#7e22ce;margin:4px 0 18px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:16px;padding:14px 16px;border-top:5px solid var(--c);box-shadow:0 8px 22px rgba(126,34,206,.10)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#7e22ce}.kc b{display:block;font-size:26px;margin-top:4px}
.p{background:#fff;border-radius:18px;padding:16px;box-shadow:0 8px 22px rgba(126,34,206,.10)}table{width:100%;font-size:12.5px}th{background:#f3e8ff;color:#6b21a8;text-align:left;padding:8px 10px;font-size:10.5px;text-transform:uppercase;letter-spacing:.6px}td{padding:8px 10px;border-bottom:1px solid #f5f3ff}.m{font-family:'Liberation Mono',monospace;font-size:11.5px;color:#6b21a8}
.fl{display:flex;gap:10px;align-items:center;margin-bottom:16px;font-size:13px}.fl div{background:#fff;border:1.5px solid #e9d5ff;border-radius:30px;padding:8px 16px;font-weight:700;color:#6b21a8}.fl span{color:#a855f7;font-size:18px}"""
    rows = [("Item no SAP sem par no controle", "1 linha SAP sem processo", "Alerta 4A", "Alerta 4A", "g"), ("Item do controle sem par no SAP", "1 processo sem lançamento", "Alerta 4B", "Alerta 4B", "g"), ("Diferença de R$ 0,01", "valores quase iguais", "Conciliado (tolerância)", "Divergente", "a"), ("Documento duplicado", "2 linhas idênticas", "1 linha + aviso", "1 linha + aviso", "g"), ("Data fora da competência", "31/10 em base de 09/2025", "Erro com a linha", "Erro com a linha", "g"),
            ("Selic na virada do mês", "depósito em 30/09", "juros pro rata", "juros pro rata", "g"), ("Estorno com valor negativo", "−R$ 4.500,00", "sinal preservado", "sinal preservado", "g"), ("Coluna obrigatória ausente", "sem centro de custo", "mensagem clara", "KeyError", "a"), ("Número com vírgula e ponto", "1.234,56 e 1,234.56", "1234,56", "1234,56", "g"), ("Planilha vazia", "0 linhas", "aviso ao usuário", "tela em branco", "a")]
    tr = "".join(f"<tr><td>{i+1:02d}</td><td><b>{a}</b></td><td class=m>{b}</td><td class=m>{c}</td><td class=m>{d}</td><td>{tg({'g':'Aprovado','a':'Ajustado'}[k], k)}</td></tr>" for i, (a, b, c, d, k) in enumerate(rows))
    body = f"""<h1>Cenários de teste gerados com IA</h1><div class=s>Casos sintéticos para validar a lógica antes de usar nos dados reais · exemplo ilustrativo</div>
<div class=fl><div>Descrevo a regra</div><span>→</span><div>IA propõe cenários e testes</div><span>→</span><div>Executo e comparo</div><span>→</span><div>Ajusto o código</div><span>→</span><div>Revisão humana</div></div>
<div class=k><div class=kc style="--c:#7c3aed"><span>Cenários</span><b>48</b></div><div class=kc style="--c:#16a34a"><span>Aprovados de início</span><b>45</b></div><div class=kc style="--c:#f59e0b"><span>Ajustados no código</span><b>3</b></div><div class=kc style="--c:#ef4444"><span>Pendentes</span><b>0</b></div></div>
<div class=p><table><tr><th>#</th><th>Cenário</th><th>Entrada sintética</th><th>Esperado</th><th>Obtido</th><th>Status</th></tr>{tr}</table></div>"""
    return doc(body, css, 1400, 820)

# IA 2 · assistente dentro do dashboard
def ia_copilot():
    css = """body{background:#f1f5f9;display:flex;color:#0f172a}.d{flex:1;padding:28px 30px}.d h1{font-size:24px;letter-spacing:-.4px}.d .s{font-size:12.5px;color:#64748b;margin:4px 0 16px}.k{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:14px}.kc{background:#fff;border-radius:14px;padding:12px 14px;box-shadow:0 4px 14px rgba(15,23,42,.07)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;color:#64748b}.kc b{display:block;font-size:22px;margin-top:3px}
.p{background:#fff;border-radius:16px;padding:16px;box-shadow:0 4px 14px rgba(15,23,42,.07);margin-bottom:14px}.p h3{font-size:12px;color:#334155;text-transform:uppercase;letter-spacing:.8px;margin-bottom:8px}
.ch{width:440px;background:#fff;border-left:1px solid #e2e8f0;display:flex;flex-direction:column}.chh{padding:16px 20px;border-bottom:1px solid #e2e8f0;display:flex;gap:10px;align-items:center}.chh i{width:30px;height:30px;border-radius:10px;background:linear-gradient(135deg,#7c3aed,#3b82f6)}.chh b{font-size:14px}.chh span{font-size:11px;color:#64748b;display:block}
.ms{flex:1;padding:18px 20px;overflow:hidden}.u{background:#eef2ff;color:#312e81;border-radius:16px 16px 4px 16px;padding:11px 14px;font-size:13px;margin:0 0 14px 70px}.a{background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px 16px 16px 4px;padding:13px 15px;font-size:12.5px;line-height:1.55;margin-bottom:12px}.a b{color:#1e293b}.a ul{margin:6px 0 6px 18px}.src{font-size:10.5px;color:#64748b;margin-top:8px}
.sg{display:flex;flex-wrap:wrap;gap:8px;padding:0 20px 12px}.sg span{border:1.5px solid #c7d2fe;border-radius:20px;padding:6px 12px;font-size:11.5px;color:#4338ca}.in{margin:0 20px 18px;border:1.5px solid #c7d2fe;border-radius:14px;padding:11px 14px;font-size:12.5px;color:#94a3b8}"""
    ch = line([(m, a, b) for m, a, b in zip(["Abr", "Mai", "Jun", "Jul", "Ago", "Set"], [8.4, 8.9, 9.1, 9.4, 10.0, 11.2], [8.5, 8.8, 9.2, 9.6, 9.9, 10.4])], ["#3b82f6", "#94a3b8"], 590, 230, "#64748b", "#e5e7eb", dashed=(1,), series=["Provisão", "Orçado"])
    body = f"""<div class=d><h1>Provisões · visão mensal</h1><div class=s>Painel com assistente integrado · dados fictícios</div><div class=k><div class=kc><span>Provisão em setembro</span><b>R$ 11,2 mi</b></div><div class=kc><span>Variação vs agosto</span><b style="color:#dc2626">+R$ 1,2 mi</b></div><div class=kc><span>Itens a revisar</span><b>6</b></div></div><div class=p><h3>Provisão × orçado (R$ mi)</h3>{ch}</div>
<div class=p><h3>Maiores variações</h3><table style="width:100%;font-size:12px"><tr><td>Serviços de TI</td><td style="text-align:right">+R$ 0,8 mi</td></tr><tr><td>Manutenção</td><td style="text-align:right">+R$ 0,3 mi</td></tr><tr><td>Energia</td><td style="text-align:right">+R$ 0,1 mi</td></tr></table></div></div>
<div class=ch><div class=chh><i></i><div><b>Assistente de análise</b><span>consulta a base do painel</span></div></div><div class=ms><div class=u>Por que a provisão de setembro subiu em relação a agosto?</div>
<div class=a><b>A provisão subiu R$ 1,2 mi (+12%).</b> Três itens explicam 92% da variação:<ul><li><b>Serviços de TI:</b> +R$ 0,8 mi, 3 contratos com serviço prestado e sem nota fiscal.</li><li><b>Manutenção:</b> +R$ 0,3 mi, ordem concluída em 29/09.</li><li><b>Energia:</b> +R$ 0,1 mi, ajuste de consumo.</li></ul>Seis itens ainda estão sem pedido e precisam de revisão antes do fechamento.<div class=src>Fonte: tabela de provisões · atualizada hoje às 08:10</div></div></div>
<div class=sg><span>Mostrar os 6 itens sem pedido</span><span>Gerar justificativa</span><span>Exportar para Excel</span></div><div class=in>Pergunte sobre os números do painel…</div></div>"""
    return doc(body, css, 1400, 780)

DASH = {"forecast-budget": ("Forecast × Budget", "Neon escuro", "Planejamento"), "dre-executiva": ("DRE executiva", "Editorial", "Contabilidade"), "apuracao-tributos": ("Apuração de tributos", "Laranja claro", "Fiscal"),
        "fluxo-de-caixa": ("Fluxo de caixa", "Verde menta", "Financeiro"), "contingencias-risco": ("Contingências · mapa de risco", "Roxo escuro", "Jurídico"), "capex-projetos": ("CAPEX por projeto", "Minimalista", "Investimentos"),
        "reforma-tributaria": ("Reforma tributária", "Gradiente", "Fiscal"), "contas-a-pagar-aging": ("Contas a pagar · aging", "Azul claro", "Financeiro"), "orcamento-centro-custo": ("Orçamento por centro de custo", "Pastel", "Planejamento")}
SCREENS_C = {"dash__forecast-budget": d_forecast(), "dash__dre-executiva": d_dre(), "dash__apuracao-tributos": d_tributos(), "dash__fluxo-de-caixa": d_caixa(), "dash__contingencias-risco": d_conting(),
             "dash__capex-projetos": d_capex(), "dash__reforma-tributaria": d_reforma(), "dash__contas-a-pagar-aging": d_aging(), "dash__orcamento-centro-custo": d_orc(), "ia__testes": ia_testes(), "ia__assistente": ia_copilot()}
