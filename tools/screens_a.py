# -*- coding: utf-8 -*-
"""Telas dos projetos 01 a 09. Cada projeto tem estilo próprio. Todos os dados são fictícios."""
import random
from kit import *

UFS = ["SP", "RJ", "MG", "BA", "RS", "PR", "PE", "CE"]
def tg(t, k):
    c = {"g": ("#d1fae5", "#047857"), "a": ("#fef3c7", "#92400e"), "r": ("#fee2e2", "#b91c1c"), "b": ("#dbeafe", "#1d4ed8"), "x": ("#e5e7eb", "#374151")}[k]
    return f'<span style="background:{c[0]};color:{c[1]};padding:3px 9px;border-radius:20px;font-size:10.5px;font-weight:700;white-space:nowrap">{E(t)}</span>'

# ---------------------------------------------------------------- 01 Streamlit navy
def s01(key, nome, seed):
    R = random.Random(seed)
    css = """
body{background:radial-gradient(1000px 420px at 85% -10%,#e0e9ff,transparent 60%),#f4f6fb;display:flex;color:#0f172a}
.side{width:244px;background:linear-gradient(180deg,#0b1b3a,#0e2554);color:#cbd5e1;padding:22px 16px;flex-shrink:0}
.logo{display:flex;gap:10px;align-items:center;margin-bottom:24px}.logo i{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#3b82f6,#22d3ee)}
.logo b{display:block;color:#fff;font-size:14px}.logo span{font-size:10.5px;color:#8ea4c8}
.lbl{font-size:10px;letter-spacing:1.2px;text-transform:uppercase;color:#7f95ba;margin:18px 0 8px 6px}
.opt{padding:9px 12px;border-radius:10px;font-size:13px;margin-bottom:4px;color:#b7c6df}.opt.on{background:linear-gradient(90deg,rgba(59,130,246,.35),rgba(59,130,246,.08));color:#fff;font-weight:bold}
.file{background:rgba(255,255,255,.06);border:1px dashed rgba(255,255,255,.22);border-radius:10px;padding:8px 10px;font-size:11px;margin-bottom:6px}.file b{color:#6ee7b7}
.main{flex:1;padding:20px 28px}
.crumb{display:flex;justify-content:space-between;font-size:12px;color:#64748b;margin-bottom:12px}.crumb b{color:#0f172a}
.pill{background:#e0ecff;color:#1e40af;border-radius:20px;padding:5px 12px;font-size:11px;font-weight:700}
h1{font-size:26px;color:#0b1b3a;letter-spacing:-.3px}.sub{font-size:12.5px;color:#64748b;margin:3px 0 12px}
.ban{background:#fffbeb;border:1px solid #fde68a;color:#92400e;border-radius:12px;padding:10px 14px;font-size:12px;margin-bottom:12px}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:14px}
.card{background:#fff;border-radius:16px;padding:14px 16px;box-shadow:0 1px 2px rgba(15,23,42,.05),0 8px 24px rgba(15,23,42,.06);border:1px solid #eef2f8;position:relative}
.card:after{content:'';position:absolute;left:0;bottom:0;height:3px;width:100%;background:var(--c,#3b82f6);border-radius:0 0 16px 16px}
.card .k{font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:.6px}.card .v{font-size:24px;font-weight:700;color:#0b1b3a;margin-top:5px}.card .d{font-size:11px;color:#64748b;margin-top:3px}
.card svg{position:absolute;right:12px;top:14px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}
.panel{background:#fff;border-radius:16px;padding:14px 16px;border:1px solid #eef2f8;box-shadow:0 8px 24px rgba(15,23,42,.06)}
.panel h3{font-size:13px;color:#0b1b3a;margin-bottom:10px}
table{width:100%;font-size:11.5px}th{background:#f1f5fb;color:#475569;text-align:left;padding:8px 10px;font-size:10.5px;text-transform:uppercase;letter-spacing:.5px}td{padding:7px 10px;border-bottom:1px solid #eef2f8}.n{text-align:right}
"""
    pre = {"civel": "PROC-C", "trabalhista": "PROC-T", "regulatorio": "PROC-R", "tributario": "PROC-X"}[key]
    rows = ""; cont = ext = 0
    for i in range(9):
        c = R.uniform(2e4, 2.4e5); e = c if i not in (4,) else c * R.uniform(.95, 1.05); st = tg("Conciliado", "g") if abs(c - e) < 1 else tg("Divergente", "a")
        if i == 7: e = 0; st = tg("SAP sem par no extra", "r")
        if i == 8: c = 0; e = R.uniform(2e4, 6e4); st = tg("Extra sem par no SAP", "r")
        cont += c; ext += e
        rows += f"<tr><td>{pre}-{1000+i*37}</td><td>49000{R.randint(10000,99999)}</td><td>{R.choice(UFS)}</td><td class=n>{brl(c)}</td><td class=n>{brl(e)}</td><td class=n>{brl(c*1.11)}</td><td>{st}</td></tr>"
    cards = "".join(f'<div class="card" style="--c:{c}"><div class="k">{k}</div><div class="v">{v}</div><div class="d">{d}</div>{spark(c, seed=i+seed)}</div>' for i, (k, v, d, c) in enumerate([
        ("Saldo contábil", mi(cont / 1e6), "extraído do razão", "#3b82f6"), ("Saldo extra-contábil", mi(ext / 1e6), "controle da área", "#3b82f6"),
        ("Diferença", mi((cont - ext) / 1e6), "contábil − extra", "#f59e0b"), ("Itens sem par", "2", "nos dois sentidos", "#ef4444")]))
    items = ["Cível", "Trabalhista", "Regulatório", "Tributário"]; items.remove(nome); items = [nome] + items
    side = "".join(f'<div class="opt {"on" if i==0 else ""}">{o}</div>' for i, o in enumerate(items))
    body = f"""<div class=side><div class=logo><i></i><div><b>Conciliação de Depósitos</b><span>App Streamlit · demo</span></div></div><div class=lbl>Tipo de depósito</div>{side}
<div class=lbl>Arquivos</div><div class=file><b>✔</b> Razão contábil (.xlsx)</div><div class=file><b>✔</b> Controle da área (.xlsx)</div><div class=file><b>✔</b> Tabela Selic (PDF)</div></div>
<div class=main><div class=crumb><div>Início / Depósitos / <b>{nome}</b></div><span class=pill>DADOS FICTÍCIOS</span></div><h1>Depósito Judicial · {nome}</h1><div class=sub>Conciliação SAP × controle da área · atualização pela Selic</div>
<div class=ban>⚠ 1 item do SAP sem par no controle e 1 item do controle sem par no SAP. Veja as seções 4A e 4B do resumo.</div><div class=cards>{cards}</div>
<div class=row><div class=panel><h3>Diferença por UF</h3>{hbars([(u, R.choice([-1,1])*R.uniform(5e3,9e4)) for u in UFS[:6]], 490, fmt=mil_)}</div>
<div class=panel><h3>Atualização monetária (Selic)</h3>{line([(m, R.uniform(1.2,1.6), R.uniform(1.1,1.5)) for m in ["Jan","Fev","Mar","Abr","Mai","Jun"]], ["#3b82f6","#f59e0b"], 490, 190, series=["Contábil","Extra"])}</div></div>
<div class=panel><h3>Conciliação detalhada · {nome}</h3><table><tr><th>Processo</th><th>Doc. contábil</th><th>UF</th><th class=n>Contábil</th><th class=n>Extra</th><th class=n>Contábil atualizado</th><th>Status</th></tr>{rows}</table></div></div>"""
    return doc(body, css, 1400, 900)
def mil_(v): return f"R$ {v/1000:,.0f} mil".replace(",", ".")

# ---------------------------------------------------------------- 02 Contingências: documento + matriz de risco
def s02_nota():
    css = """
body{background:#d8dce3;font-family:'Liberation Sans',Arial}
.top{height:42px;background:#2b579a;color:#fff;display:flex;align-items:center;padding:0 18px;font-size:13px;gap:18px}.top span{opacity:.8}
.rib{height:34px;background:#f3f3f3;border-bottom:1px solid #d0d0d0;display:flex;gap:22px;align-items:center;padding:0 22px;font-size:12px;color:#444}
.page{position:absolute;left:150px;top:92px;width:830px;height:880px;background:#fff;box-shadow:0 10px 34px rgba(0,0,0,.2);padding:54px 62px;font-family:'Liberation Serif',Georgia,serif;color:#1a1a1a}
h1{font-size:23px;border-bottom:3px solid #be123c;padding-bottom:8px;margin-bottom:14px}
p{font-size:12.5px;line-height:1.55;margin-bottom:14px;text-align:justify}
h2{font-size:14px;color:#9f1239;margin:18px 0 8px;font-family:'Liberation Sans',Arial;text-transform:uppercase;letter-spacing:.8px}
table{width:100%;font-size:12px;font-family:'Liberation Sans',Arial}th{background:#fdf2f4;color:#9f1239;padding:7px 9px;text-align:right;border-bottom:2px solid #be123c;font-size:11px}th:first-child,td:first-child{text-align:left}
td{padding:6px 9px;border-bottom:1px solid #eee;text-align:right}tr.t td{font-weight:700;border-top:2px solid #333;background:#fafafa}
.fn{font-size:10.5px;color:#666;margin-top:10px;font-family:'Liberation Sans',Arial}
.cm{position:absolute;left:1010px;width:330px;background:#fff;border-left:4px solid #be123c;border-radius:6px;padding:12px 14px;font-size:12px;box-shadow:0 4px 14px rgba(0,0,0,.14);font-family:'Liberation Sans',Arial;line-height:1.45}
.cm b{color:#9f1239;display:block;margin-bottom:3px;font-size:11px}
.stat{position:absolute;left:0;right:0;bottom:0;height:24px;background:#2b579a;color:#dbe6f7;font-size:11px;padding:4px 16px}
"""
    t1 = [("Tributária", 9450, 31800, 12100), ("Trabalhista", 6120, 12400, 4900), ("Cível", 3210, 8950, 3300), ("Regulatória", 1240, 5300, 1700)]
    r1 = "".join(f"<tr><td>{a}</td><td>{n0(b)}</td><td>{n0(c)}</td><td>{n0(d)}</td></tr>" for a, b, c, d in t1) + f"<tr class=t><td>Total</td><td>{n0(20020)}</td><td>{n0(58450)}</td><td>{n0(22000)}</td></tr>"
    r2 = [("Saldo em 31/08", "18.420"), ("(+) Constituições", "3.150"), ("(−) Reversões", "(1.280)"), ("(+) Atualização monetária", "640"), ("(−) Pagamentos", "(910)")]
    rr = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in r2) + "<tr class=t><td>Saldo em 30/09</td><td>20.020</td></tr>"
    body = f"""<div class=top><b>Nota_Explicativa_Contingencias.docx</b><span>· Salvo</span></div><div class=rib><span>Arquivo</span><span><b>Página Inicial</b></span><span>Inserir</span><span>Layout</span><span>Revisão</span><span>Exibir</span></div>
<div class=page><h1>Nota 14 — Provisões para contingências</h1>
<p>A Companhia é parte em processos de natureza tributária, trabalhista, cível e regulatória. Com base na opinião de seus assessores jurídicos, a Administração constitui provisão para as causas com perda provável e cuja saída de recursos é estimável, e divulga as de perda possível.</p>
<h2>Exposição por prognóstico (R$ mil)</h2><table><tr><th>Natureza</th><th>Provável (provisão)</th><th>Possível (divulgação)</th><th>Remota</th></tr>{r1}</table>
<h2>Movimentação da provisão (R$ mil)</h2><table><tr><th>Movimento</th><th>Setembro</th></tr>{rr}</table>
<div class=fn>Valores fictícios gerados para demonstração.</div></div>
<div class=cm style="top:300px"><b>Comentário · Revisão</b>Variação de +R$ 1,6 mi no mês explicada por 2 reclassificações para perda provável.</div>
<div class=cm style="top:520px"><b>Conferência</b>Total da tabela bate com a base do jurídico e com o razão contábil.</div>
<div class=stat>Página 1 de 2 · 412 palavras · Português (Brasil)</div>"""
    return doc(body, css, 1400, 980)

def s02_matriz():
    css = """body{background:#14090e;color:#fce7f3;padding:30px 36px}h1{font-size:26px;letter-spacing:-.4px}.sub{color:#f9a8d4;opacity:.75;font-size:13px;margin:4px 0 20px}
.k{display:flex;gap:14px;margin-bottom:18px}.kc{flex:1;background:#1f0d17;border:1px solid #3b1328;border-radius:14px;padding:14px 16px}.kc b{display:block;font-size:24px;color:#fff;margin-top:4px}.kc span{font-size:11px;color:#f9a8d4;text-transform:uppercase;letter-spacing:.8px}
.g{display:grid;grid-template-columns:1.35fr 1fr;gap:18px}.p{background:#1a0b13;border:1px solid #3b1328;border-radius:16px;padding:18px}.p h3{font-size:13px;color:#fbcfe8;margin-bottom:12px}"""
    R = random.Random(5); M = [[R.randint(0, 6) + (i + j) // 2 for j in range(5)] for i in range(5)]
    def cf(i, j, v):
        s = (i + (4 - j)); return ["#365314", "#4d7c0f", "#a16207", "#c2410c", "#be123c", "#881337", "#881337", "#881337", "#881337"][min(s, 8)] if v else "#2a1420"
    def cf(i, j, v):
        sev = (4 - i) + j   # i=0 impacto muito alto; j=4 quase certa
        pal = ["#365314", "#3f6212", "#4d7c0f", "#a16207", "#c2410c", "#be123c", "#9f1239", "#881337", "#7f1d1d"]
        return pal[min(sev, 8)] if v else "#2a1420"
    hm = heat(M, ["Muito alto", "Alto", "Médio", "Baixo", "Muito baixo"], ["Remota", "Pouco prov.", "Possível", "Provável", "Quase certa"], 780, 420, cf, "#fbcfe8")
    body = f"""<h1>Matriz de risco · Contingências</h1><div class=sub>Probabilidade de perda × impacto financeiro · quantidade de processos por célula · dados fictícios</div>
<div class=k><div class=kc><span>Processos ativos</span><b>412</b></div><div class=kc><span>Exposição provável</span><b>R$ 20,0 mi</b></div><div class=kc><span>Exposição possível</span><b>R$ 58,4 mi</b></div><div class=kc><span>Reclassificações no mês</span><b>7</b></div></div>
<div class=g><div class=p><h3>Mapa de calor — probabilidade × impacto</h3>{hm}</div>
<div class=p><h3>Provisão por natureza (R$ mil)</h3>{hbars([("Tributária",9450),("Trabalhista",6120),("Cível",3210),("Regulatória",1240)],520,"#f43f5e","#fbcfe8","#2a1420",fmt=lambda v:n0(v),rowh=40,barh=18,labw=100)}
<h3 style="margin-top:22px">Evolução do prognóstico</h3>{line([(m,a,b) for m,a,b in [("Abr",15,48),("Mai",16,50),("Jun",17,53),("Jul",17,55),("Ago",18,57),("Set",20,58)]],["#fb7185","#c084fc"],520,200,"#f9a8d4","#3b1328",series=["Provável","Possível"],mfill="#14090e")}</div></div>"""
    return doc(body, css, 1400, 860)

# ---------------------------------------------------------------- 03 Excel
def excel(file, tabs, active, title, headers, rows, formula, sel, widths, w=1400, h=860):
    cols = "ABCDEFGHIJ"; css = """
body{background:#fff;font-family:'Liberation Sans',Arial}
.t{height:38px;background:#217346;color:#fff;display:flex;align-items:center;padding:0 16px;gap:16px;font-size:13px}.t b{font-weight:600}
.rb{height:62px;background:#f3f3f3;border-bottom:1px solid #d0d0d0;padding:8px 18px;font-size:12px;color:#333;display:flex;gap:26px}.rb span.on{color:#217346;font-weight:700;border-bottom:3px solid #217346;padding-bottom:4px;height:max-content}
.fx{height:30px;border-bottom:1px solid #d0d0d0;display:flex;align-items:center;font-size:12.5px;color:#222}.nb{width:80px;border-right:1px solid #d0d0d0;padding:0 10px;height:100%;display:flex;align-items:center;font-weight:600}.fxl{padding:0 12px;color:#217346;font-style:italic;font-weight:700}.fxv{font-family:'Liberation Mono',monospace;color:#111}
table{table-layout:fixed;font-size:12px}td,th{border:1px solid #e1e1e1;height:25px;padding:0 8px;white-space:nowrap;overflow:hidden}th{background:#f0f0f0;color:#555;font-weight:400;text-align:center}
td.rn{background:#f0f0f0;color:#666;text-align:center;width:42px}.hd{background:#1e6e43;color:#fff;font-weight:700}.num{text-align:right}.sel{outline:2px solid #217346;outline-offset:-2px;background:#f2faf5}
.ok{background:#e2f0d9;color:#375623;text-align:center}.rev{background:#fff2cc;color:#7f6000;text-align:center}.tot td{font-weight:700;background:#eaf3ee;border-top:2px solid #217346}
.sh{position:absolute;left:0;right:0;bottom:24px;height:30px;background:#f3f3f3;border-top:1px solid #d0d0d0;display:flex;align-items:flex-end;padding-left:42px;gap:2px}.sh span{padding:5px 16px;font-size:12px;color:#444}.sh span.on{background:#fff;color:#217346;font-weight:700;border-top:2px solid #217346}
.sb{position:absolute;left:0;right:0;bottom:0;height:24px;background:#217346;color:#e8f5ec;font-size:11px;padding:4px 16px;display:flex;gap:30px}
"""
    wd = "".join(f'<col style="width:{x}px">' for x in widths)
    hdr = '<tr><th style="width:42px"></th>' + "".join(f"<th>{cols[i]}</th>" for i in range(len(headers))) + "</tr>"
    allrows = [[title] + [""] * (len(headers) - 1), [""] * len(headers), headers] + rows
    body_rows = ""
    nr = 24
    for ri in range(nr):
        r = allrows[ri] if ri < len(allrows) else [""] * len(headers)
        tds = ""
        for ci, v in enumerate(r):
            cl = ""
            s = str(v)
            if ri == 2: cl = "hd"
            elif ri == 0 and ci == 0: tds += f'<td colspan="{len(headers)}" style="font-size:15px;font-weight:700;color:#1e6e43;border:0">{E(s)}</td>'; break
            elif s.startswith("R$"): cl = "num"
            if s == "OK": cl = "ok"
            if s in ("Revisar", "Sem pedido"): cl = "rev"
            if (ri + 1, ci) == sel: cl += " sel"
            tds += f'<td class="{cl}">{E(s)}</td>'
        istot = ri < len(allrows) and str(r[0]).startswith("TOTAL")
        body_rows += f'<tr class="{"tot" if istot else ""}"><td class="rn">{ri+1}</td>{tds}</tr>'
    tb = "".join(f"<span class={'on' if i==active else ''}>{t}</span>" for i, t in enumerate(tabs))
    html_ = f"""<div class=t><b>{file}</b><span style="opacity:.8">Salvo em OneDrive</span></div><div class=rb><span>Arquivo</span><span class=on>Página Inicial</span><span>Inserir</span><span>Fórmulas</span><span>Dados</span><span>Revisão</span></div>
<div class=fx><div class=nb>{cols[sel[1]]}{sel[0]+1}</div><div class=fxl>fx</div><div class=fxv>{E(formula)}</div></div>
<table><colgroup><col style="width:42px">{wd}</colgroup>{hdr}{body_rows}</table><div class=sh>{tb}</div><div class=sb><span>Pronto</span><span>Média: R$ 118.420,55</span><span>Contagem: 14</span><span>Soma: R$ 1.657.887,70</span></div>"""
    return doc(html_, css, w, h)

def s03_opex():
    R = random.Random(21); rows = []; tot = 0
    for i in range(14):
        v = R.uniform(2e4, 3.2e5); f = R.choice([0, 0, .3, .6, 0]); prov = v * (1 - f); tot += prov
        rows.append([f"Fornecedor {chr(65+i)}", f"CC-{R.randint(100,140)}", R.choice(["Manutenção", "Serviços TI", "Energia", "Consultoria", "Locação"]), f"PED-{4500+i*7}", brl(v), f"{int(f*100)}%", brl(prov), "OK" if i % 5 else "Revisar"])
    rows.append(["TOTAL", "", "", "", "", "", brl(tot), ""])
    return excel("Provisao_OPEX_Set2025.xlsx", ["Provisão OPEX", "Estorno", "CAPEX", "Resumo"], 0, "Provisão OPEX · Setembro/2025",
                 ["Fornecedor", "C. Custo", "Natureza", "Pedido", "Valor recebido", "% Faturado", "Provisão", "Status"], rows, "=SE(F5>=1;0;E5*(1-F5))", (4, 6), [170, 80, 120, 100, 130, 90, 130, 90])

def s03_capex():
    R = random.Random(22); rows = []; tot = 0
    for i in range(12):
        v = R.uniform(8e4, 1.9e6); fa = v * R.choice([0, .25, .5]); prov = v - fa; tot += prov
        rows.append([f"PRJ-{300+i*7}", f"ORD-{R.randint(5000,9999)}", R.choice(["Expansão de rede", "Modernização de TI", "Infraestrutura", "Licenças"]), f"Fornecedor {chr(75+i%8)}", brl(v), brl(fa), brl(prov), "OK" if i != 4 and i != 9 else "Sem pedido"])
    rows.append(["TOTAL", "", "", "", "", "", brl(tot), ""])
    return excel("Provisao_CAPEX_Set2025.xlsx", ["CAPEX", "Estorno", "OPEX", "Resumo"], 0, "Provisão CAPEX · por projeto",
                 ["Projeto", "Ordem invest.", "Descrição", "Fornecedor", "Valor recebido", "Faturado", "Provisão CAPEX", "Status"], rows, "=PROCV(B5;Ordens!A:C;3;0)*(E5-F5)/E5", (4, 6), [100, 110, 160, 120, 130, 120, 140, 100])

# ---------------------------------------------------------------- 04 Waterfall + Kanban
def s04_fech():
    css = """body{background:#fff7ed;padding:34px 44px;color:#431407}h1{font-size:30px;letter-spacing:-.6px}.s{color:#9a3412;margin:4px 0 22px;font-size:14px}
.g{display:grid;grid-template-columns:1fr 330px;gap:26px}.p{background:#fff;border-radius:20px;padding:22px;box-shadow:0 10px 30px rgba(194,65,12,.12);border:1px solid #fed7aa}
.k{background:#fff;border-radius:18px;padding:18px 20px;margin-bottom:14px;border:1px solid #fed7aa;border-left:8px solid #f97316}.k span{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#9a3412}.k b{display:block;font-size:30px;margin-top:4px}.k i{font-style:normal;font-size:12px;color:#9a3412}
.fn{margin-top:14px;background:#ffedd5;border-radius:14px;padding:12px 14px;font-size:12.5px;color:#7c2d12;line-height:1.5}"""
    wf = waterfall([("Orçado", 100, "t"), ("Reforço", 8, "d"), ("Cortes", -6, "d"), ("Escopo", 11, "d"), ("Atrasos", -9, "d"), ("Realizado", 104, "t"), ("Capitalizado", 71, "t")], 800, 400, "#16a34a", "#dc2626", "#ea580c", "#7c2d12", "#fed7aa", lambda v: f"{v:g}".replace(".", ","), 12)
    body = f"""<h1>CAPEX 2025 · do orçado ao realizado</h1><div class=s>Fechamento acumulado · R$ milhões · dados fictícios</div><div class=g><div class=p>{wf}</div>
<div><div class=k><span>Orçado</span><b>R$ 100,0 mi</b><i>aprovado no ciclo</i></div><div class=k style="border-left-color:#16a34a"><span>Realizado</span><b>R$ 104,0 mi</b><i>+4,0% sobre o orçado</i></div><div class=k style="border-left-color:#7c2d12"><span>Capitalizado</span><b>R$ 71,0 mi</b><i>obras em andamento: R$ 33,0 mi</i></div>
<div class=fn><b>Leitura:</b> a variação líquida de +R$ 4,0 mi vem de escopo (+11) e reforço (+8), compensados por cortes (−6) e atrasos (−9).</div></div></div>"""
    return doc(body, css, 1400, 780)

def s04_just():
    css = """body{background:#fffbf5;padding:28px 34px;color:#431407}h1{font-size:26px;letter-spacing:-.4px}.s{color:#9a3412;font-size:13px;margin:4px 0 20px}
.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.col{background:#fff1e0;border-radius:18px;padding:14px;min-height:640px}.col h3{font-size:13px;display:flex;justify-content:space-between;margin-bottom:12px;color:#7c2d12}.col h3 b{background:#fff;border-radius:20px;padding:2px 10px;font-size:12px}
.c{background:#fff;border-radius:14px;padding:13px 14px;margin-bottom:12px;box-shadow:0 4px 14px rgba(124,45,18,.10);border-top:4px solid var(--c)}.c .i{font-size:11px;color:#9a3412;font-weight:700}.c .v{font-size:19px;font-weight:700;margin:3px 0}.c p{font-size:12px;color:#57534e;line-height:1.4}.c .f{display:flex;justify-content:space-between;align-items:center;margin-top:10px;font-size:11px;color:#78716c}
.av{width:24px;height:24px;border-radius:50%;background:#ea580c;color:#fff;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700}"""
    cols = [("Pendente", "#ef4444", [("PRJ-312", "+18,2%", "Aguardando justificativa da área de Engenharia.", "EN"), ("PRJ-327", "−14,5%", "Sem retorno há 5 dias.", "TI"), ("PRJ-341", "+22,0%", "Cobrança enviada automaticamente.", "FA")]),
            ("Em análise", "#f59e0b", [("PRJ-305", "+11,3%", "Contrato renegociado, validando valores.", "CO"), ("PRJ-318", "−12,1%", "Mudança de cronograma em avaliação.", "EN")]),
            ("Justificada", "#3b82f6", [("PRJ-309", "+15,0%", "Escopo ampliado após vistoria técnica.", "EN"), ("PRJ-333", "−10,8%", "Antecipação de compras do trimestre.", "CO"), ("PRJ-350", "+13,4%", "Reajuste contratual previsto em cláusula.", "TI")]),
            ("Aprovada", "#16a34a", [("PRJ-301", "+12,2%", "Aprovada pelo gestor e arquivada.", "GE"), ("PRJ-322", "−11,0%", "Aprovada com ressalva de prazo.", "GE")])]
    html_ = ""
    for t, c, cs in cols:
        cards = "".join(f'<div class=c style="--c:{c}"><div class=i>{a}</div><div class=v>{b}</div><p>{d}</p><div class=f><span>Variação vs orçado</span><div class=av>{e}</div></div></div>' for a, b, d, e in cs)
        html_ += f"<div class=col><h3>{t}<b>{len(cs)}</b></h3>{cards}</div>"
    return doc(f"<h1>Justificativas de variação · CAPEX</h1><div class=s>Variações acima da faixa de ±10% · acompanhamento por status · dados fictícios</div><div class=cols>{html_}</div>", css, 1400, 780)

# ---------------------------------------------------------------- 05 Audit dark
def s05():
    css = """body{background:#0b0e13;color:#e5e7eb;display:flex}.rail{width:84px;background:#0f141b;border-right:1px solid #1e2631;padding:20px 0;display:flex;flex-direction:column;align-items:center;gap:18px}.rail i{width:38px;height:38px;border-radius:11px;background:#1b2330;display:block}.rail i.on{background:#ef4444;box-shadow:0 0 22px rgba(239,68,68,.5)}
.m{flex:1;padding:24px 30px}.h{display:flex;justify-content:space-between;align-items:center}h1{font-size:24px;letter-spacing:-.3px}.tags span{font-size:11px;background:#1b2330;border:1px solid #2a3544;border-radius:20px;padding:5px 12px;margin-left:8px;color:#9ca3af}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:18px 0}.kc{background:#111823;border:1px solid #1e2631;border-radius:14px;padding:14px 16px}.kc span{font-size:10.5px;color:#9ca3af;text-transform:uppercase;letter-spacing:1px}.kc b{display:block;font-size:26px;margin-top:6px;font-family:'Liberation Mono',monospace}
.g{display:grid;grid-template-columns:1.6fr 1fr;gap:14px;margin-bottom:14px}.p{background:#111823;border:1px solid #1e2631;border-radius:14px;padding:16px}.p h3{font-size:12px;color:#9ca3af;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px}
table{width:100%;font-size:12px;font-family:'Liberation Mono',monospace}th{color:#6b7280;text-align:left;padding:8px;border-bottom:1px solid #263041;font-size:10.5px;text-transform:uppercase}td{padding:8px;border-bottom:1px solid #182030}.r{text-align:right}
.s{padding:2px 9px;border-radius:5px;font-size:10.5px;font-weight:700}.c{background:#7f1d1d;color:#fecaca}.a{background:#7c2d12;color:#fed7aa}.m2{background:#713f12;color:#fde68a}"""
    R = random.Random(9); days = [(str(d), max(3, int(R.gauss(40 if d > 25 else 22, 8)))) for d in range(1, 31, 2)]
    days = [(d, v) for d, v in days]
    ch = bars([(d, v) for d, v in days], ["#ef4444"], 780, 220, "#9ca3af", "#1e2631", r=3, bw=.7)
    rows = "".join(f"<tr><td>{a}</td><td>USR{b:02d}</td><td>{c}</td><td class=r>{brl(v)}</td><td>{m}</td><td><span class='s {k}'>{s}</span></td></tr>" for a, b, c, v, m, k, s in [
        ("1000482211", 7, "29/09 23:41", 912480.50, "sem texto", "c", "CRÍTICO"), ("1000482305", 3, "30/09 08:12", 640200.00, "acima da alçada", "c", "CRÍTICO"), ("1000481977", 11, "28/09 18:02", 288900.10, "fim de período", "a", "ALTO"),
        ("1000481420", 5, "26/09 17:44", 154300.00, "sem justificativa", "a", "ALTO"), ("1000480912", 2, "24/09 10:30", 72110.30, "reclassificação", "m2", "MÉDIO"), ("1000480655", 9, "22/09 14:05", 55890.00, "ajuste de provisão", "m2", "MÉDIO")])
    body = f"""<div class=rail><i class=on></i><i></i><i></i><i></i><i></i></div><div class=m><div class=h><h1>Console de lançamentos manuais</h1><div class=tags><span>Período 09/2025</span><span>Alçada &gt; R$ 100 mil</span><span style="color:#fca5a5">DADOS FICTÍCIOS</span></div></div>
<div class=k><div class=kc><span>Lançamentos</span><b>1.284</b></div><div class=kc><span>Valor total</span><b>R$ 67,7 mi</b></div><div class=kc><span>Sem justificativa</span><b style="color:#fca5a5">37</b></div><div class=kc><span>Acima da alçada</span><b style="color:#fdba74">14</b></div></div>
<div class=g><div class=p><h3>Lançamentos por dia do mês · concentração no fechamento</h3>{ch}</div><div class=p style="text-align:center"><h3>Índice de risco do período</h3>{gauge(68,300,"#ef4444","#1e2631","#f3f4f6","risco médio-alto")}<div style="font-size:12px;color:#9ca3af;margin-top:8px">valor × justificativa × horário × alçada</div></div></div>
<div class=p><h3>Alertas para revisão</h3><table><tr><th>Documento</th><th>Usuário</th><th>Data e hora</th><th class=r>Valor</th><th>Motivo</th><th>Severidade</th></tr>{rows}</table></div></div>"""
    return doc(body, css, 1400, 860)

# ---------------------------------------------------------------- 06 Despesa antecipada (calculadora / gantt / trimestral)
def s06_calc():
    css = """body{background:#f0fdfa;padding:30px 38px;color:#134e4a}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#0f766e;margin:4px 0 20px}.g{display:grid;grid-template-columns:400px 1fr;gap:22px}
.p{background:#fff;border-radius:20px;padding:22px;border:1px solid #99f6e4;box-shadow:0 10px 28px rgba(13,148,136,.12)}.p h3{font-size:13px;margin-bottom:14px;color:#0f766e;text-transform:uppercase;letter-spacing:1px}
.f{margin-bottom:13px}.f small{display:block;font-size:11px;color:#5eaaa0;margin-bottom:4px}.f div{border:1.5px solid #99f6e4;border-radius:12px;padding:10px 14px;font-size:14px;background:#f7fffd;font-weight:600}
.rd{display:flex;gap:10px;margin-bottom:16px}.rd span{flex:1;text-align:center;padding:10px;border-radius:12px;font-size:12.5px;border:1.5px solid #99f6e4;color:#0f766e}.rd span.on{background:#0d9488;color:#fff;border-color:#0d9488;font-weight:700}
.b{background:linear-gradient(135deg,#0d9488,#22d3ee);color:#fff;text-align:center;border-radius:14px;padding:13px;font-weight:700}
.kk{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}.kk div{background:#ecfeff;border-radius:14px;padding:12px 14px}.kk span{font-size:10.5px;color:#0f766e;text-transform:uppercase;letter-spacing:.8px}.kk b{display:block;font-size:20px;margin-top:3px}
table{width:100%;font-size:12px;margin-top:10px}th{background:#ccfbf1;color:#115e59;padding:7px 10px;text-align:right;font-size:10.5px;text-transform:uppercase}th:first-child,td:first-child{text-align:left}td{padding:6px 10px;border-bottom:1px solid #e6fffa;text-align:right}"""
    mo = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    data = [(m, 10000 if i < 6 else 0, 0 if i < 6 else 10000) for i, m in enumerate(mo)]
    ch = bars(data, ["#0d9488", "#99f6e4"], 760, 230, "#0f766e", "#ccfbf1", stacked=True, series=["Apropriado", "A apropriar"])
    rows = "".join(f"<tr><td>{i:02d}/2025</td><td>{brl(10000)}</td><td>{brl(10000*i)}</td><td>{brl(120000-10000*i)}</td></tr>" for i in range(1, 6))
    body = f"""<h1>Calculadora de vigência</h1><div class=s>Cronograma de apropriação mensal proporcional aos dias de vigência</div><div class=g>
<div class=p><h3>Parâmetros</h3><div class=f><small>Valor total do contrato</small><div>R$ 120.000,00</div></div><div class=f><small>Início da vigência</small><div>01/01/2025</div></div><div class=f><small>Fim da vigência</small><div>31/12/2025</div></div>
<div class=rd><span class=on>Pro rata dia</span><span>Mensal fixo</span></div><div class=b>Gerar cronograma</div></div>
<div class=p><div class=kk><div><span>Apropriação mensal</span><b>R$ 10.000,00</b></div><div><span>Apropriado até jun</span><b>R$ 60.000,00</b></div><div><span>Saldo a apropriar</span><b>R$ 60.000,00</b></div></div>{ch}
<table><tr><th>Competência</th><th>Apropriação</th><th>Acumulado</th><th>Saldo a apropriar</th></tr>{rows}</table></div></div>"""
    return doc(body, css, 1400, 780)

def s06_gantt():
    css = """body{background:#f8fffe;padding:28px 36px;color:#134e4a}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#0f766e;margin:4px 0 18px}
.gt{background:#fff;border:1px solid #99f6e4;border-radius:18px;padding:18px;box-shadow:0 10px 28px rgba(13,148,136,.10)}
.hd{display:grid;grid-template-columns:230px repeat(12,1fr);font-size:11px;color:#0f766e;font-weight:700;margin-bottom:6px;text-align:center}.hd div:first-child{text-align:left}
.r{display:grid;grid-template-columns:230px 1fr;align-items:center;border-top:1px solid #ecfdf5;padding:9px 0;font-size:12.5px}.tr{position:relative;height:24px;background:repeating-linear-gradient(90deg,#f0fdfa 0,#f0fdfa calc(100%/12 - 1px),#d9f5ef calc(100%/12 - 1px),#d9f5ef calc(100%/12))}
.bar{position:absolute;top:3px;height:18px;border-radius:9px;background:#99f6e4}.fill{position:absolute;top:3px;height:18px;border-radius:9px;background:linear-gradient(90deg,#0d9488,#14b8a6)}.now{position:absolute;top:-4px;bottom:-4px;width:2px;background:#f43f5e}
.dv{position:absolute;top:-1px;right:-6px;background:#f59e0b;color:#fff;border-radius:50%;width:16px;height:16px;font-size:10px;text-align:center;line-height:16px;font-weight:700}
.lg{display:flex;gap:20px;font-size:12px;margin-top:14px;color:#0f766e}.lg i{display:inline-block;width:12px;height:12px;border-radius:4px;margin-right:6px;vertical-align:-1px}"""
    cs = [("CTR-4001 · Seguro patrimonial", 0, 12, 8.5, 0), ("CTR-4013 · Licença de software", 2, 14, 8.5, 1), ("CTR-4026 · Aluguel de espaço", 0, 6, 6, 0), ("CTR-4039 · Manutenção anual", 3, 12, 8.5, 0), ("CTR-4052 · Licença de BI", 1, 13, 8.5, 0), ("CTR-4065 · Seguro de frota", 4, 12, 8.5, 1), ("CTR-4078 · Suporte técnico", 6, 12, 8.5, 0), ("CTR-4091 · Assinatura de dados", 5, 12, 8.5, 0)]
    rows = ""
    for n, s, e, now, dv in cs:
        s_ = max(s, 0) / 12 * 100; w = (min(e, 12) - s_ * .12) / 12 * 100; done = max(0, (min(now, e) - s)) / 12 * 100
        rows += f'<div class=r><div>{n}</div><div class=tr><div class=bar style="left:{s/12*100}%;width:{(min(e,12)-s)/12*100}%"></div><div class=fill style="left:{s/12*100}%;width:{done}%"></div>{"<div class=dv>!</div>" if dv else ""}<div class=now style="left:{now/12*100}%"></div></div></div>'
    mo = "".join(f"<div>{m}</div>" for m in ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"])
    body = f"""<h1>Cronograma de apropriação · contratos</h1><div class=s>Vigência × apropriado até o fechamento · ! indica divergência entre saldo contábil e recalculado</div><div class=gt><div class=hd><div>Contrato</div>{mo}</div>{rows}
<div class=lg><span><i style="background:#99f6e4"></i>Vigência</span><span><i style="background:#0d9488"></i>Apropriado</span><span><i style="background:#f43f5e"></i>Fechamento</span><span><i style="background:#f59e0b"></i>Divergência</span></div></div>"""
    return doc(body, css, 1400, 700)

def s06_tri():
    css = """body{background:#f0fdfa;padding:28px 36px;color:#134e4a}h1{font-size:26px}.s{font-size:13px;color:#0f766e;margin:4px 0 18px}.g{display:grid;grid-template-columns:1fr 1fr;gap:18px}.p{background:#fff;border:1px solid #99f6e4;border-radius:18px;padding:16px 18px;box-shadow:0 10px 28px rgba(13,148,136,.10)}.p h3{font-size:13px;color:#0f766e;margin-bottom:6px}"""
    qs = [("T1", 8.4, 3.1, -3.6), ("T2", 7.9, 4.2, -3.3), ("T3", 8.8, 3.6, -3.9), ("T4", 8.5, 4.4, -3.5)]
    ps = ""
    for q, i, a, ap in qs:
        wf = waterfall([("Inicial", i, "t"), ("Adições", a, "d"), ("Apropriações", ap, "d"), ("Final", round(i + a + ap, 1), "t")], 600, 230, "#0d9488", "#f43f5e", "#134e4a", "#0f766e", "#ccfbf1", lambda v: f"{v:.1f}".replace(".", ","), 11)
        ps += f"<div class=p><h3>{q} · R$ milhões</h3>{wf}</div>"
    return doc(f"<h1>Relatório trimestral · despesa antecipada</h1><div class=s>Movimentação do saldo: inicial + adições − apropriações = final · dados fictícios</div><div class=g>{ps}</div>", css, 1400, 700)

# ---------------------------------------------------------------- 07 Cartões de contratos (caução)
def s07():
    css = """body{background:#faf5ff;padding:28px 36px;color:#3b0764}.h{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#7e22ce}
.q{background:#fff;border:1.5px solid #e9d5ff;border-radius:30px;padding:9px 20px;font-size:13px;color:#7e22ce;width:340px}.ch{display:flex;gap:10px;margin-bottom:20px}.ch span{background:#fff;border:1.5px solid #e9d5ff;border-radius:30px;padding:7px 16px;font-size:12.5px;color:#6b21a8}.ch span.on{background:#7c3aed;color:#fff;border-color:#7c3aed;font-weight:700}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.c{background:#fff;border-radius:20px;padding:18px 20px;box-shadow:0 10px 26px rgba(124,58,237,.12);border:1px solid #f3e8ff;position:relative;overflow:hidden}.c:before{content:'';position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--c)}
.c .t{display:flex;justify-content:space-between;align-items:center}.c .id{font-size:12px;color:#7e22ce;font-weight:700}.c .uf{background:#f3e8ff;color:#6b21a8;font-size:11px;font-weight:700;border-radius:8px;padding:3px 9px}
.c h4{font-size:16px;margin:8px 0 2px}.c .v{font-size:24px;font-weight:700;margin:8px 0;color:#2e1065}.c .p{height:8px;border-radius:8px;background:#f3e8ff;overflow:hidden}.c .p i{display:block;height:100%;background:var(--c);border-radius:8px}
.c .f{display:flex;justify-content:space-between;font-size:11.5px;color:#6b7280;margin-top:8px}.st{display:inline-block;font-size:11px;font-weight:700;border-radius:20px;padding:3px 10px;margin-top:10px;background:var(--b);color:var(--t)}"""
    R = random.Random(14); cs = ""
    stt = [("Vigente", "#8b5cf6", "#ede9fe", "#5b21b6", 70, "vence em 412 dias"), ("Vence em 90 dias", "#f59e0b", "#fef3c7", "#92400e", 92, "vence em 47 dias"), ("Devolução pendente", "#f43f5e", "#ffe4e6", "#be123c", 100, "venceu há 12 dias")]
    for i in range(9):
        s = stt[[0, 0, 1, 0, 2, 0, 1, 0, 0][i]]
        cs += f"<div class=c style='--c:{s[1]}'><div class=t><span class=id>CTR-{600+i*11}</span><span class=uf>{R.choice(UFS)}</span></div><h4>Locador {chr(65+i)}</h4><div style='font-size:12px;color:#6b7280'>Loja / Escritório {R.randint(10,99)}</div><div class=v>{brl(R.uniform(1.5e4,2.6e5))}</div><div class=p><i style='width:{s[4]}%'></i></div><div class=f><span>Vigência {s[4]}%</span><span>{s[5]}</span></div><span class=st style='--b:{s[2]};--t:{s[3]}'>{s[0]}</span></div>"
    body = f"""<div class=h><div><h1>Depósitos caução · contratos</h1><div class=s>Saldo contábil × contrato · prazos de devolução · dados fictícios</div></div><div class=q>🔍 Buscar contrato ou locador</div></div><div class=ch><span class=on>Todos (64)</span><span>Vence em 90 dias (7)</span><span>Devolução pendente (2)</span><span>Divergência de saldo (3)</span></div><div class=g>{cs}</div>"""
    return doc(body, css, 1400, 860)

# ---------------------------------------------------------------- 08 PDF -> dados
def s08():
    css = """body{background:#e0f2fe;display:flex;gap:0;color:#0c4a6e}.pdf{width:560px;background:#94a3b8;padding:26px;position:relative}.page{background:#fff;height:808px;box-shadow:0 12px 30px rgba(0,0,0,.35);padding:34px 34px;font-family:'Liberation Mono',monospace;font-size:11px;color:#1f2937;position:relative}
.bk{display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #0369a1;padding-bottom:10px;margin-bottom:12px}.bk b{font-family:'Liberation Sans',Arial;font-size:18px;color:#0369a1}
.l{display:grid;grid-template-columns:60px 1fr 100px 110px;gap:6px;padding:5px 0;border-bottom:1px dotted #d1d5db}.l span:nth-child(3),.l span:nth-child(4){text-align:right}.hl{background:#fde047;padding:7px 6px;margin-top:10px;font-weight:700;display:flex;justify-content:space-between;border-radius:3px;box-shadow:0 0 0 3px rgba(250,204,21,.4)}
.call{position:absolute;right:-18px;top:600px;background:#0284c7;color:#fff;font-family:'Liberation Sans',Arial;border-radius:10px;padding:8px 12px;font-size:12px;font-weight:700;box-shadow:0 8px 20px rgba(2,132,199,.5)}
.arrow{width:46px;display:flex;align-items:center;justify-content:center;font-size:34px;color:#0284c7}
.out{flex:1;padding:28px 30px 28px 6px}h1{font-size:25px;letter-spacing:-.4px}.s{font-size:13px;color:#0369a1;margin:4px 0 16px}.k{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}.kc{background:#fff;border-radius:14px;padding:12px 14px;border-left:6px solid #0ea5e9}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;color:#0369a1}.kc b{display:block;font-size:22px;margin-top:3px}
.p{background:#fff;border-radius:16px;padding:14px 16px;box-shadow:0 8px 24px rgba(3,105,161,.12)}table{width:100%;font-size:11.5px}th{background:#e0f2fe;color:#075985;text-align:left;padding:8px;font-size:10.5px;text-transform:uppercase}td{padding:7px 8px;border-bottom:1px solid #f0f9ff}.n{text-align:right}
.cf{padding:2px 9px;border-radius:20px;font-size:10.5px;font-weight:700}.h{background:#dcfce7;color:#166534}.m{background:#fef9c3;color:#854d0e}.b{background:#fee2e2;color:#991b1b}"""
    R = random.Random(8); tx = ""
    for d, hst, v in [("26/09", "PIX RECEBIDO CLIENTE 0381", 12480.55), ("26/09", "TARIFA PACOTE SERVICOS", -184.90), ("27/09", "TED ENVIADA FORNECEDOR", -45210.00), ("29/09", "DEPOSITO IDENTIFICADO", 88320.10), ("29/09", "PAGTO TITULO 99211", -12090.35), ("30/09", "APLICACAO AUTOMATICA", -50000.00)]:
        tx += f"<div class=l><span>{d}</span><span>{hst}</span><span>{brl(v,False)}</span><span></span></div>"
    pdf = f"""<div class=pdf><div class=page><div class=bk><b>BANCO A</b><span>EXTRATO CONTA CORRENTE</span></div><div style="margin-bottom:10px">Ag 0001 · Conta 12345-6 · Período 01/09 a 30/09/2025</div>{tx}<div class=l style="color:#6b7280"><span>...</span><span>demais lançamentos</span><span></span><span></span></div>
<div class=hl><span>SALDO FINAL EM 30/09/2025</span><span>4.382.910,55</span></div><div style="margin-top:14px;color:#6b7280;line-height:1.6">SALDO DO DIA 29/09 ........ 4.382.910,55<br>SALDO ANTERIOR ............ 4.241.003,10</div><div class=call>saldo localizado ✔</div></div></div>"""
    rows = ""
    for i, (a, b, c, s, cf, g) in enumerate([("extrato_a_001.pdf", "Banco A", "12345-6", 4382910.55, "Alta", 0), ("extrato_a_002.pdf", "Banco A", "88120-1", 1204330.00, "Alta", 0), ("extrato_b_014.pdf", "Banco B", "30211-9", 902115.80, "Média", 0), ("extrato_c_007.pdf", "Banco C", "5567-2", 7310440.12, "Alta", 1), ("extrato_d_020.pdf", "Banco D", "9117-4", 245008.90, "Baixa", 1), ("extrato_e_003.pdf", "Banco E", "7720-0", 3318200.00, "Alta", 0), ("extrato_f_011.pdf", "Banco F", "1456-3", 689330.45, "Média", 0), ("extrato_g_002.pdf", "Banco G", "9004-8", 156002.00, "Alta", 0)]):
        rz = s + (320.0 if g else 0)
        cls = {"Alta": "h", "Média": "m", "Baixa": "b"}[cf]
        rows += f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class=n>{brl(s)}</td><td><span class='cf {cls}'>{cf}</span></td><td class=n>{brl(rz)}</td><td class=n style='color:{'#b91c1c' if g else '#166534'};font-weight:700'>{brl(rz-s) if g else '—'}</td></tr>"
    out = f"""<div class=arrow>➜</div><div class=out><h1>Extração de saldos · extratos em PDF</h1><div class=s>Saldo do último dia do mês lido de cada PDF e comparado ao balanço · dados fictícios</div>
<div class=k><div class=kc><span>PDFs lidos</span><b>92</b></div><div class=kc><span>Confiança alta</span><b>81</b></div><div class=kc style="border-color:#f59e0b"><span>Conferir</span><b>9</b></div><div class=kc style="border-color:#ef4444"><span>Com diferença</span><b>4</b></div></div>
<div class=p><table><tr><th>Arquivo</th><th>Banco</th><th>Conta</th><th class=n>Saldo no extrato</th><th>Confiança</th><th class=n>Saldo no balanço</th><th class=n>Diferença</th></tr>{rows}</table></div></div>"""
    return doc(pdf + out, css, 1400, 860)

# ---------------------------------------------------------------- 09 Terminal / wizard
def s09():
    css = """body{background:#05090a;color:#d1fae5;display:flex;font-family:'Liberation Mono',monospace}.st{width:300px;background:#071013;border-right:1px solid #12332a;padding:28px 24px}.st h2{font-family:'Liberation Sans',Arial;font-size:15px;color:#86efac;margin-bottom:22px;letter-spacing:.5px}
.sp{display:flex;gap:14px;margin-bottom:26px;position:relative}.sp:not(:last-child):after{content:'';position:absolute;left:14px;top:32px;height:26px;width:2px;background:#14532d}.dot{width:30px;height:30px;border-radius:50%;border:2px solid #166534;display:flex;align-items:center;justify-content:center;font-size:13px;color:#4ade80;flex-shrink:0}.dot.ok{background:#16a34a;color:#04130a;border-color:#16a34a}.dot.cur{border-color:#a3e635;color:#a3e635;box-shadow:0 0 14px rgba(163,230,53,.5)}
.sp b{display:block;font-family:'Liberation Sans',Arial;font-size:14px;color:#ecfdf5}.sp span{font-size:11px;color:#6b8f7d}
.term{flex:1;padding:26px 28px}.tb{background:#0a1412;border:1px solid #14532d;border-radius:14px;overflow:hidden}.tbh{background:#0f1f1a;padding:10px 16px;font-size:12px;color:#86efac;display:flex;gap:7px;align-items:center}.tbh i{width:10px;height:10px;border-radius:50%;background:#166534}.tbh span{margin-left:10px;color:#6b8f7d}
.ln{padding:0 20px;font-size:12.5px;line-height:1.95}.i{color:#22c55e}.w{color:#facc15}.e{color:#f87171}.d{color:#6b8f7d}.pb{margin:10px 20px 0;height:10px;background:#0f2a1f;border-radius:10px;overflow:hidden}.pb i{display:block;width:100%;height:100%;background:linear-gradient(90deg,#16a34a,#a3e635)}
.sm{width:330px;padding:26px 26px 26px 0}.sc{background:#0a1412;border:1px solid #14532d;border-radius:14px;padding:18px;margin-bottom:14px}.sc span{font-family:'Liberation Sans',Arial;font-size:11px;color:#6b8f7d;text-transform:uppercase;letter-spacing:1px}.sc b{display:block;font-size:26px;color:#a3e635;margin-top:4px}.ok2{background:#052e16;border:1px solid #16a34a;color:#86efac;border-radius:14px;padding:16px;font-family:'Liberation Sans',Arial;font-size:13px;line-height:1.5}"""
    steps = [("Carregar planilha base", "docas_set25.xlsx · 412 linhas", "ok"), ("Validar regras", "4 erros apontados", "ok"), ("Gerar arquivo de lançamento", "em execução", "cur"), ("Conferir débito = crédito", "aguardando", "")]
    st = "".join(f'<div class=sp><div class="dot {c}">{"✓" if c=="ok" else i+1}</div><div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b, c) in enumerate(steps))
    log = ["<span class=d>[19:42:01]</span> <span class=i>INFO</span>  lendo planilha base ...... 412 linhas", "<span class=d>[19:42:02]</span> <span class=i>INFO</span>  plano de contas carregado .. 1.184 contas", "<span class=d>[19:42:03]</span> <span class=w>WARN</span>  linha 118 · centro de custo vazio", "<span class=d>[19:42:03]</span> <span class=e>ERRO</span>  linha 207 · conta inexistente no plano", "<span class=d>[19:42:03]</span> <span class=w>WARN</span>  linha 331 · valor zerado (ignorada)", "<span class=d>[19:42:03]</span> <span class=w>WARN</span>  linha 402 · data fora da competência", "<span class=d>[19:42:04]</span> <span class=i>INFO</span>  408 linhas válidas · 4 com pendência", "<span class=d>[19:42:05]</span> <span class=i>INFO</span>  montando layout de lançamento ...", "<span class=d>[19:42:06]</span> <span class=i>INFO</span>  débito   R$ 18.402.311,40", "<span class=d>[19:42:06]</span> <span class=i>INFO</span>  crédito  R$ 18.402.311,40", "<span class=d>[19:42:06]</span> <span class=i>OK</span>    lote balanceado ✔", "<span class=d>[19:42:07]</span> <span class=i>OK</span>    arquivo salvo: lancamento_docas_2025-09.xlsx"]
    body = f"""<div class=st><h2>▍LANÇAMENTO DE DOCAS</h2>{st}</div><div class=term><div class=tb><div class=tbh><i></i><i></i><i></i><span>processamento · log</span></div><div style="padding:14px 0">{"<br>".join(f"<div class=ln>{l}</div>" for l in log)}</div><div class=pb><i></i></div><div style="height:16px"></div></div></div>
<div class=sm><div class=sc><span>Linhas válidas</span><b>408 / 412</b></div><div class=sc><span>Débito = Crédito</span><b>R$ 18,4 mi</b></div><div class=ok2>✔ Arquivo pronto para carga no ERP.<br><span style="color:#6b8f7d">dados fictícios</span></div></div>"""
    return doc(body, css, 1400, 800)

SCREENS_A = {
    "conciliacao-depositos-judiciais__civel": s01("civel", "Cível", 3), "conciliacao-depositos-judiciais__trabalhista": s01("trabalhista", "Trabalhista", 4),
    "conciliacao-depositos-judiciais__regulatorio": s01("regulatorio", "Regulatório", 5), "conciliacao-depositos-judiciais__tributario": s01("tributario", "Tributário", 6),
    "contingencias-judiciais__nota": s02_nota(), "contingencias-judiciais__matriz": s02_matriz(),
    "provisoes-opex-capex__opex": s03_opex(), "provisoes-opex-capex__capex": s03_capex(),
    "relatorios-capex__fechamento": s04_fech(), "relatorios-capex__justificativa": s04_just(),
    "relatorio-lancamentos-manuais__console": s05(),
    "despesa-antecipada__calculadora": s06_calc(), "despesa-antecipada__gantt": s06_gantt(), "despesa-antecipada__trimestral": s06_tri(),
    "deposito-caucao__cartoes": s07(), "analise-contas-bancarias__extracao": s08(), "lancamento-docas__terminal": s09(),
}
