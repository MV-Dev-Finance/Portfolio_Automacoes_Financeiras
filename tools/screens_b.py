# -*- coding: utf-8 -*-
"""Telas dos projetos 10 a 16. Estilos distintos por projeto. Dados fictícios."""
import random
from kit import *
from screens_a import tg

# ---------------------------------------------------------------- 10 Dashboard HTML com upload (cobalt)
def s10():
    css = """body{background:#eef2ff;color:#1e1b4b}.hd{height:190px;background:linear-gradient(120deg,#1d4ed8,#6d28d9);color:#fff;padding:26px 44px}.hd small{opacity:.8;letter-spacing:1.4px;text-transform:uppercase;font-size:11px}.hd h1{font-size:30px;margin:6px 0 4px;letter-spacing:-.6px}.hd p{opacity:.85;font-size:13.5px}
.w{margin:-70px 40px 0;display:grid;grid-template-columns:340px 1fr;gap:20px}.c{background:#fff;border-radius:20px;padding:20px;box-shadow:0 14px 40px rgba(67,56,202,.18)}.c h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#4338ca;margin-bottom:12px}
.dz{border:2.5px dashed #a5b4fc;border-radius:16px;background:#f5f7ff;padding:26px 14px;text-align:center;font-size:13px;color:#4338ca;margin-bottom:14px}.dz b{display:block;font-size:30px}
.fl{display:flex;justify-content:space-between;background:#eef2ff;border-radius:10px;padding:8px 12px;font-size:12px;margin-bottom:8px}.fl i{color:#6366f1;font-style:normal}
.sl{border:1.5px solid #c7d2fe;border-radius:10px;padding:8px 12px;font-size:12.5px;margin-bottom:10px;background:#fafaff}.sl small{display:block;font-size:10px;color:#6366f1}
.bt{background:linear-gradient(120deg,#2563eb,#7c3aed);color:#fff;text-align:center;border-radius:12px;padding:11px;font-weight:700;font-size:13px}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:18px;padding:14px 16px;box-shadow:0 14px 40px rgba(67,56,202,.14)}.kc span{font-size:10.5px;color:#6366f1;text-transform:uppercase;letter-spacing:.8px}.kc b{display:block;font-size:24px;margin-top:4px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:16px}table{width:100%;font-size:12px}th{text-align:left;color:#4338ca;font-size:10.5px;text-transform:uppercase;padding:6px 8px;border-bottom:2px solid #e0e7ff}td{padding:7px 8px;border-bottom:1px solid #eef2ff}.n{text-align:right}"""
    left = """<div class=c><h3>Atualizar dados</h3><div class=dz><b>⬆</b>Arraste CSV ou Excel aqui<br><span style="font-size:11px;opacity:.7">lido no navegador · nada é enviado</span></div>
<div class=fl><span>base_julho.xlsx</span><i>✕</i></div><div class=fl><span>base_agosto.xlsx</span><i>✕</i></div><div class=fl><span>base_setembro.csv</span><i>✕</i></div>
<div class=sl><small>Agrupar por</small>Área solicitante</div><div class=sl><small>Somar a coluna</small>Montante</div><div class=bt>Exportar resumo (CSV)</div></div>"""
    R = random.Random(10)
    tb = "".join(f"<tr><td>{a}</td><td class=n>{n0(b)}</td><td class=n>{brl(c)}</td><td class=n>{pc(d)}</td></tr>" for a, b, c, d in [("Financeiro", 412, 2310440.2, 24.1), ("Operações", 388, 1980210.0, 20.6), ("Comercial", 301, 1720880.5, 17.9), ("TI", 244, 1405300.0, 14.6), ("Jurídico", 190, 980440.1, 10.2)])
    right = f"""<div><div class=k><div class=kc><span>Arquivos</span><b>3</b></div><div class=kc><span>Linhas</span><b>1.840</b></div><div class=kc><span>Montante total</span><b>R$ 9,6 mi</b></div><div class=kc><span>Maior grupo</span><b>Financeiro</b></div></div>
<div class=g><div class=c><h3>Top 5 · montante por área</h3>{hbars([("Financeiro",2310),("Operações",1980),("Comercial",1720),("TI",1405),("Jurídico",980)],460,"#6366f1","#312e81","#eef2ff",lambda v:f"R$ {v/1000:.1f} mi".replace(".",","),rowh=34,barh=16)}</div>
<div class=c><h3>Total por arquivo</h3>{bars([("Jul",3.1),("Ago",3.3),("Set",3.2)],["#6366f1"],440,170,"#4338ca","#e0e7ff",r=8,bw=.5,vals=lambda v:f"{v:.1f}".replace(".",","))}</div></div>
<div class=c style="margin-top:16px"><h3>Tabela consolidada</h3><table><tr><th>Área</th><th class=n>Linhas</th><th class=n>Montante</th><th class=n>% do total</th></tr>{tb}</table></div></div>"""
    return doc(f"""<div class=hd><small>Dashboard HTML · dados fictícios</small><h1>Painel de notas de débito</h1><p>Anexe o arquivo e os dados são somados ao painel, sem licença de BI.</p></div><div class=w>{left}{right}</div>""", css, 1400, 900)

# ---------------------------------------------------------------- 11 Power Platform
def phone(title, content, accent="#742774"):
    return f"""<div class=ph><div class=sb><span>9:41</span><span>5G ▮▮▮</span></div><div class=ah style="background:{accent}">{title}</div><div class=pc>{content}</div></div>"""

def s11_apps():
    css = """body{background:linear-gradient(135deg,#2a0a30,#4a1d6e 55%,#1e3a8a);display:flex;justify-content:center;gap:46px;padding:36px 30px;color:#fff;font-family:'Liberation Sans',Arial}
.col{width:310px}.cap{text-align:center;margin-top:16px;font-size:14px;font-weight:700;color:#f3e8ff}.cap small{display:block;font-weight:400;color:#d8b4fe;font-size:11.5px;margin-top:3px}
.ph{width:310px;height:690px;border-radius:40px;background:#f8f7fb;border:10px solid #0b0b12;box-shadow:0 30px 60px rgba(0,0,0,.5);overflow:hidden;position:relative;color:#1f1535}
.sb{display:flex;justify-content:space-between;padding:10px 22px 4px;font-size:11px;font-weight:700;background:#742774;color:#fff}.ah{padding:10px 18px 16px;color:#fff;font-weight:700;font-size:16px}.pc{padding:14px}
.bar{height:9px;background:#e9d5ee;border-radius:9px;overflow:hidden;margin:6px 0 14px}.bar i{display:block;height:100%;background:linear-gradient(90deg,#742774,#c026d3);border-radius:9px}
.in{border:2px solid #742774;border-radius:12px;padding:11px 12px;font-size:12.5px;color:#742774;background:#fff;margin-bottom:12px;font-weight:700}
.it{background:#fff;border-radius:12px;padding:10px 12px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 8px rgba(116,39,116,.1);font-size:12px}.it b{display:block;font-size:12.5px}.it span{color:#6b7280;font-size:10.5px}.x{background:#fee2e2;color:#b91c1c;border-radius:50%;width:22px;height:22px;text-align:center;line-height:22px;font-size:11px;font-weight:700}
.ok{color:#15803d;font-weight:700;font-size:11px}.pend{background:#fef3c7;color:#92400e;border-radius:20px;padding:2px 9px;font-size:10.5px;font-weight:700}
.btn{background:linear-gradient(135deg,#742774,#a21caf);color:#fff;text-align:center;border-radius:14px;padding:13px;font-weight:700;font-size:13px;margin-top:10px}.btn.o{background:#fff;color:#742774;border:2px solid #742774}
.st{display:flex;justify-content:space-between;font-size:12.5px;padding:9px 0;border-bottom:1px solid #eee}.st b{color:#742774}"""
    gal = "".join(f'<div class=it><div><b>SN{480000+i*377}</b><span>Roteador · 14:{10+i}</span></div><div style="display:flex;gap:8px;align-items:center"><span class=ok>✔</span><div class=x>✕</div></div></div>' for i in range(5))
    p1 = phone("Inventário · Loja 042", f'<div style="font-size:11px;color:#6b7280">Progresso</div><div style="font-weight:700">128 de 240 seriais</div><div class=bar><i style="width:53%"></i></div><div class=in>▥  Bipe ou digite o serial</div>{gal}<div class=btn>Ver pendências</div>')
    pend = "".join(f'<div class=it><div><b>SN{481000+i*211}</b><span>Smartphone · não encontrado</span></div><span class=pend>Pendente</span></div>' for i in range(6))
    p2 = phone("Pendências", f'<div style="font-size:12px;margin-bottom:10px;color:#6b7280">14 itens sem bipagem (Encontrado = Não)</div>{pend}<div class=btn style="margin-top:12px">Recontar selecionados</div><div class="btn o">Voltar ao inventário</div>')
    dn = donut([("Bipados", 226), ("Pendentes", 14)], ["#742774", "#e9d5ee"], 150, .64, "#1f1535", "94%", 150)
    p3 = phone("Fechamento", f'<div style="display:flex;justify-content:center;margin:6px 0 10px">{dn}</div><div class=st><span>Itens no SAP</span><b>240</b></div><div class=st><span>Bipados</span><b>226</b></div><div class=st><span>Pendentes</span><b>14</b></div><div class=st><span>Fora do SAP</span><b>2</b></div><div class=btn>Gerar relatório e enviar para assinatura</div><div style="text-align:center;font-size:11px;color:#15803d;margin-top:10px">✔ Sincronizado com o SharePoint</div>')
    cols = "".join(f"<div class=col>{p}<div class=cap>{t}<small>{s}</small></div></div>" for p, t, s in [(p1, "Bipagem em tempo real", "salva a cada bip na lista"), (p2, "Tela de pendências", "só o que não foi encontrado"), (p3, "Fechamento do inventário", "relatório e assinatura eletrônica")])
    return doc(cols, css, 1400, 860)

def s11_flow():
    css = """body{background:#f3f6fb;background-image:radial-gradient(#cbd5e1 1px,transparent 1px);background-size:22px 22px;font-family:'Liberation Sans',Arial;color:#1f2937}
.top{height:46px;background:#0066ff;color:#fff;display:flex;align-items:center;padding:0 22px;gap:16px;font-size:14px;font-weight:700}.top span{font-weight:400;opacity:.85;font-size:12px}
.fl{position:absolute;top:84px;width:380px}.fl h3{font-size:13px;text-transform:uppercase;letter-spacing:1px;color:#0050c8;margin-bottom:12px;text-align:center}
.n{background:#fff;border-radius:10px;border:1px solid #d6dde8;border-left:7px solid var(--c);padding:12px 14px;display:flex;gap:12px;align-items:center;box-shadow:0 3px 10px rgba(15,23,42,.08)}.n i{width:36px;height:36px;border-radius:9px;background:var(--c);color:#fff;font-style:normal;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}.n b{display:block;font-size:13px}.n span{font-size:11px;color:#64748b}
.cn{width:2px;height:26px;background:#94a3b8;margin:0 auto;position:relative}.cn:after{content:'';position:absolute;bottom:-3px;left:-4px;border:5px solid transparent;border-top:7px solid #94a3b8;border-bottom:0}
.in{margin-left:34px;margin-top:0}.leg{position:absolute;bottom:18px;left:40px;font-size:12px;color:#64748b}"""
    def flow(x, title, nodes):
        h = ""
        for i, (c, ic, t, s) in enumerate(nodes):
            h += f'<div class=n style="--c:{c}"><i>{ic}</i><div><b>{t}</b><span>{s}</span></div></div>'
            if i < len(nodes) - 1: h += "<div class=cn></div>"
        return f'<div class=fl style="left:{x}px"><h3>{title}</h3>{h}</div>'
    PA, AC, LP, RS = "#0066ff", "#475569", "#7c3aed", "#0f766e"
    f1 = flow(40, "ImportarSeriais", [(PA, "PA", "Power Apps (V2)", "Recebe o arquivo Excel com os seriais"), (AC, "SP", "Criar arquivo", "SharePoint · pasta /Importacoes"), (AC, "XL", "Listar linhas em uma tabela", "Excel Online · Tabela1"), (LP, "↻", "Aplicar a cada", "para cada serial da planilha"), (AC, "SP", "Atualizar item · Serial_List", "Encontrado = Sim · DataHoraBipe = utcNow()"), (RS, "↩", "Responder ao Power Apps", "retorna OK e atualiza a galeria")])
    f2 = flow(500, "Limpar_app", [(PA, "PA", "Power Apps (V2)", "botão Limpar seriais do inventário"), (AC, "SP", "Obter itens", "Serial_List · filtro por Centro"), (LP, "↻", "Aplicar a cada", "processamento em lote"), (AC, "SP", "Atualizar item", "Encontrado = Não · Status = Pendente"), (RS, "↩", "Responder ao Power Apps", "Refresh + atualização da galeria")])
    f3 = flow(960, "Relatorio_e_Assinatura", [(PA, "PA", "Power Apps (V2)", "recebe coleções: seriais, chips, fora do SAP"), (AC, "PDF", "Gerar PDFs do relatório", "um arquivo por tipo de item"), (AC, "SP", "Salvar na biblioteca", "histórico do inventário por loja"), (AC, "✎", "Enviar para assinatura", "inventariante, gerente da loja e gerente geral"), (RS, "↩", "Responder ao Power Apps", "status do envelope")])
    return doc(f"<div class=top>Power Automate <span>· Fluxos do inventário · demonstração com dados fictícios</span></div>{f1}{f2}{f3}<div class=leg>● gatilho Power Apps   ● ação SharePoint / Excel   ● laço   ● resposta</div>", css, 1400, 820)

def s11_list():
    css = """body{background:#fff;font-family:'Liberation Sans',Arial;color:#201f1e}.t{height:46px;background:#038387;color:#fff;display:flex;align-items:center;padding:0 20px;gap:16px;font-size:14px}.t b{font-size:16px}
.sn{display:flex;height:calc(100% - 46px)}.nv{width:210px;background:#f3f2f1;padding:18px 14px;font-size:13px;border-right:1px solid #e1dfdd}.nv div{padding:9px 10px;border-radius:4px;margin-bottom:2px}.nv div.on{background:#fff;border-left:3px solid #038387;font-weight:700}
.m{flex:1;padding:20px 24px}h1{font-size:22px;margin-bottom:12px}.cb{display:flex;gap:22px;border-bottom:1px solid #e1dfdd;padding-bottom:10px;margin-bottom:12px;font-size:13px;color:#323130}.cb b{color:#038387}
table{width:100%;font-size:12.5px}th{text-align:left;padding:9px 10px;border-bottom:2px solid #c8c6c4;font-weight:600;color:#605e5c;background:#faf9f8}td{padding:8px 10px;border-bottom:1px solid #edebe9}.mono{font-family:'Liberation Mono',monospace}
.p{padding:2px 10px;border-radius:12px;font-size:11px;font-weight:600}.s1{background:#dff6dd;color:#107c10}.s2{background:#fff4ce;color:#835b00}.s3{background:#fde7e9;color:#a4262c}
.ft{position:absolute;bottom:0;left:210px;right:0;height:30px;background:#faf9f8;border-top:1px solid #e1dfdd;font-size:11.5px;color:#605e5c;padding:7px 24px}"""
    R = random.Random(11); rows = ""
    for i in range(15):
        f = R.choice([1, 1, 1, 0, 1]); st = ("Finalizado", "s1") if f else ("Pendente", "s2")
        rows += f"<tr><td class=mono>SN{480000+i*377}</td><td>{R.choice(['Roteador','Smartphone','Acessório','Chip'])}</td><td>{R.choice(['MAT-10441','MAT-20318','MAT-30872'])}</td><td>Loja {R.choice([42,17,88])}</td><td>{'✔ Sim' if f else '— Não'}</td><td>{'11/09/2025 14:'+str(10+i) if f else ''}</td><td><span class='p {st[1]}'>{st[0]}</span></td></tr>"
    body = f"""<div class=t><b>▦ SharePoint</b><span>Inventário · Controles e Ativos</span></div><div class=sn><div class=nv><div>Início</div><div class=on>Serial_List</div><div>BaseSAP_Relatorio</div><div>Lojas</div><div>Relatórios</div><div>Documentos</div></div>
<div class=m><h1>Serial_List</h1><div class=cb><b>＋ Novo</b><span>✎ Editar em exibição de grade</span><span>⤓ Exportar</span><span>⚡ Automatizar</span><span>▥ Integrar</span></div>
<table><tr><th>Serial</th><th>Tipo</th><th>Material</th><th>Centro</th><th>Encontrado</th><th>DataHoraBipe</th><th>Status</th></tr>{rows}</table></div></div><div class=ft>18.240 itens (limite de exibição 5.000) · dados fictícios</div>"""
    return doc(body, css, 1400, 780)

# ---------------------------------------------------------------- 12 Saneamento (antes x depois)
def s12():
    css = """body{background:#fff5fa;padding:26px 34px;color:#500724}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#9d174d;margin:4px 0 16px}
.q{display:flex;align-items:center;gap:18px;background:#fff;border-radius:18px;padding:14px 20px;box-shadow:0 10px 26px rgba(190,24,93,.12);margin-bottom:16px;border:1px solid #fbcfe8}.q b{font-size:26px}.pr{flex:1;height:14px;background:#fce7f3;border-radius:14px;position:relative;overflow:hidden}.pr i{position:absolute;left:0;top:0;bottom:0;border-radius:14px}
.g{display:grid;grid-template-columns:1fr 250px 1fr;gap:16px}.p{background:#fff;border-radius:18px;padding:14px;border:1px solid #fbcfe8;box-shadow:0 10px 26px rgba(190,24,93,.10)}.p h3{font-size:13px;margin-bottom:10px;color:#9d174d}
table{width:100%;font-size:11.5px}th{background:#fdf2f8;color:#9d174d;text-align:left;padding:6px 8px;font-size:10px;text-transform:uppercase}td{padding:6px 8px;border-bottom:1px solid #fdf2f8;white-space:nowrap}
.e{background:#fee2e2;color:#991b1b;border-radius:5px;padding:2px 5px}.f{background:#dcfce7;color:#166534;border-radius:5px;padding:2px 5px}.d{text-decoration:line-through;color:#9ca3af}
.r{background:#fff;border-radius:18px;padding:14px;border:1px solid #fbcfe8}.r h3{font-size:13px;color:#9d174d;margin-bottom:10px}.ri{display:flex;justify-content:space-between;font-size:12px;padding:9px 0;border-bottom:1px solid #fdf2f8}.ri b{color:#be185d}"""
    before = [("1.1.01.002", "03/09/25", "1.234,50", "ACME LTDA", ""), ("1.1.01.002", "03/09/25", "1.234,50", "ACME LTDA", "dup"), ("11101003", "2025-09-04", "980.00", "acme ltda", ""), ("", "05/09/2025", "R$ 5.400,00", "Beta S.A.", ""), ("1.1.02.010", "06/9/25", "(1.200,00)", "BETA SA", ""), ("1.1.02.010", "31/02/2025", "720,10", "Gama ME", ""), ("1.3.01.007", "08/09/2025", "15000", "Delta  Ltda ", "")]
    after = [("1.1.01.002", "03/09/2025", "1.234,50", "ACME LTDA"), ("—", "—", "—", "removida (duplicada)"), ("1.1.01.003", "04/09/2025", "980,00", "ACME LTDA"), ("1.1.01.004*", "05/09/2025", "5.400,00", "BETA SA"), ("1.1.02.010", "06/09/2025", "-1.200,00", "BETA SA"), ("1.1.02.010", "pendente", "720,10", "GAMA ME"), ("1.3.01.007", "08/09/2025", "15.000,00", "DELTA LTDA")]
    def b(r):
        c = ["", "", "", ""]; x = r[4] == "dup"
        cs = [r[0] or '<span class=e>vazio</span>', r[1], r[2], r[3]]
        if "-" in r[1] and r[1][4] == "-": cs[1] = f'<span class=e>{r[1]}</span>'
        if r[2].startswith("R$") or "." in r[2] and "," not in r[2] or r[2].startswith("(") or r[2].isdigit(): cs[2] = f'<span class=e>{r[2]}</span>'
        if r[0] and "." not in r[0]: cs[0] = f'<span class=e>{r[0]}</span>'
        if r[3] != r[3].upper() or r[3] != r[3].strip(): cs[3] = f'<span class=e>{r[3]}</span>'
        if r[1] == "31/02/2025": cs[1] = f'<span class=e>{r[1]}</span>'
        return "<tr>" + "".join(f"<td class={'d' if x else ''}>{v}</td>" for v in cs) + "</tr>"
    def a(r):
        return "<tr>" + "".join(f"<td>{('<span class=f>'+v+'</span>') if ('removida' not in r[3] and k in (0,1,2,3) and v not in ('—',)) and (r[3]!='ACME LTDA' or k in (0,2) and False) else v}</td>" for k, v in enumerate(r)) + "</tr>"
    ta = "".join(b(r) for r in before)
    tb = "".join(f"<tr>{''.join(f'<td>{v}</td>' for v in r)}</tr>" for r in after).replace("1.1.01.003", '<span class=f>1.1.01.003</span>').replace("04/09/2025", '<span class=f>04/09/2025</span>').replace("980,00", '<span class=f>980,00</span>').replace("1.1.01.004*", '<span class=f>1.1.01.004</span>').replace("-1.200,00", '<span class=f>-1.200,00</span>').replace("15.000,00", '<span class=f>15.000,00</span>').replace("5.400,00", '<span class=f>5.400,00</span>').replace("DELTA LTDA", '<span class=f>DELTA LTDA</span>').replace("GAMA ME", '<span class=f>GAMA ME</span>').replace("pendente", '<span class=e>pendente</span>')
    rules = "".join(f"<div class=ri><span>{a}</span><b>{b}</b></div>" for a, b in [("Duplicados por chave", "1.206"), ("Valores como texto", "2.204"), ("Datas em formatos mistos", "389"), ("Conta sem de/para", "845"), ("Nomes padronizados", "3.918"), ("Pendente de decisão", "112")])
    body = f"""<h1>Saneamento de bases</h1><div class=s>Diagnóstico por regra e correção automática antes da carga · dados fictícios</div>
<div class=q><div><span style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#9d174d">Qualidade da base</span><br><b>94,1% → 99,6%</b></div><div class=pr><i style="width:99.6%;background:#f9a8d4"></i><i style="width:94.1%;background:#be185d"></i></div><div style="font-size:12px;color:#9d174d">182.440 linhas · 3 fontes</div></div>
<div class=g><div class=p><h3>Antes · base bruta</h3><table><tr><th>Conta</th><th>Data</th><th>Valor</th><th>Fornecedor</th></tr>{ta}</table></div>
<div class=r><h3>Regras aplicadas</h3>{rules}</div>
<div class=p><h3>Depois · base saneada</h3><table><tr><th>Conta</th><th>Data</th><th>Valor</th><th>Fornecedor</th></tr>{tb}</table></div></div>"""
    return doc(body, css, 1400, 720)

# ---------------------------------------------------------------- 13 Apuração (livro fiscal)
def s13():
    css = """body{background:#efe6d2;padding:26px 36px;color:#3b2a14;font-family:'Liberation Serif',Georgia,serif}
.g{display:grid;grid-template-columns:860px 1fr;gap:26px}.pp{background:#fffdf6;border:2px solid #b45309;outline:6px double #e7d3a7;outline-offset:-12px;padding:38px 46px;height:850px}
h1{font-size:25px;text-align:center;letter-spacing:3px;text-transform:uppercase;color:#78350f}.sub{text-align:center;font-size:12px;color:#92400e;margin:5px 0 16px;font-family:'Liberation Sans',Arial}
.hd{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;border:1px solid #d6b98a;padding:10px 14px;font-size:12px;margin-bottom:16px;font-family:'Liberation Sans',Arial}.hd b{display:block;color:#92400e;font-size:10px;text-transform:uppercase;letter-spacing:.8px}
h2{font-size:13px;background:#78350f;color:#fff;padding:6px 12px;margin:14px 0 4px;font-family:'Liberation Sans',Arial;letter-spacing:1px;text-transform:uppercase}
table{width:100%;font-size:12.5px;font-family:'Liberation Sans',Arial}td{padding:6px 10px;border-bottom:1px dotted #d6b98a}td:first-child{width:60px;color:#92400e}td.n{text-align:right;font-variant-numeric:tabular-nums}tr.t td{font-weight:700;border-top:2px solid #78350f;border-bottom:0}
.fin{margin-top:18px;border:3px double #b45309;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;background:#fef3c7;font-family:'Liberation Sans',Arial}.fin b{font-size:26px;color:#78350f}.fin span{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#92400e}
.sg{margin-top:26px;display:flex;justify-content:space-between;font-size:11px;color:#92400e;font-family:'Liberation Sans',Arial}.sg div{border-top:1px solid #92400e;padding-top:4px;width:230px;text-align:center}
.side h3{font-family:'Liberation Sans',Arial;font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:#78350f;margin-bottom:12px}.cd{background:#fffdf6;border:1px solid #d6b98a;border-left:7px solid #b45309;border-radius:6px;padding:13px 16px;margin-bottom:12px;font-family:'Liberation Sans',Arial}.cd .a{display:flex;justify-content:space-between;font-size:13px;font-weight:700}.cd .v{font-size:21px;margin:5px 0;color:#78350f}.cd .m{font-size:11.5px;color:#92400e}
.tg{background:#fde68a;color:#78350f;border-radius:20px;padding:2px 10px;font-size:10.5px;font-weight:700}.tg.ok{background:#d9f99d;color:#365314}"""
    deb = [("001", "Saídas tributadas", 2840500.00), ("002", "Outros débitos", 38200.00), ("003", "Estornos de créditos", 12400.00)]
    cre = [("004", "Entradas e aquisições", 1912300.00), ("005", "Outros créditos", 96100.00), ("006", "Estornos de débitos", 8200.00), ("007", "Saldo credor do período anterior", 150000.00)]
    td = sum(v for *_, v in deb); tc = sum(v for *_, v in cre); sal = td - tc
    r = lambda L: "".join(f"<tr><td>{c}</td><td>{d}</td><td class=n>{brl(v)}</td></tr>" for c, d, v in L)
    paper = f"""<div class=pp><h1>Apuração do ICMS</h1><div class=sub>Livro de registro · modelo demonstrativo · dados fictícios</div><div class=hd><div><b>Período</b>09/2025</div><div><b>Estabelecimento</b>Matriz · SP01</div><div><b>UF</b>SP</div></div>
<h2>Débito do imposto</h2><table>{r(deb)}<tr class=t><td></td><td>Total de débitos</td><td class=n>{brl(td)}</td></tr></table>
<h2>Crédito do imposto</h2><table>{r(cre)}<tr class=t><td></td><td>Total de créditos</td><td class=n>{brl(tc)}</td></tr></table>
<h2>Apuração do saldo</h2><table><tr><td>008</td><td>Saldo devedor (débitos − créditos)</td><td class=n>{brl(sal)}</td></tr><tr><td>009</td><td>Deduções</td><td class=n>{brl(0)}</td></tr></table>
<div class=fin><span>Imposto a recolher</span><b>{brl(sal)}</b></div><div class=sg><div>Responsável contábil</div><div>Responsável fiscal</div></div></div>"""
    side = """<div class=side><h3>Apuração por tributo · setembro</h3>
<div class=cd><div class=a><span>ICMS</span><span class=tg>A conciliar</span></div><div class=v>R$ 724.500,00</div><div class=m>vence em 10/10 · 8 estabelecimentos</div></div>
<div class=cd style="border-left-color:#16a34a"><div class=a><span>PIS</span><span class="tg ok">Apurado</span></div><div class=v>R$ 118.420,35</div><div class=m>não cumulativo · créditos de insumos</div></div>
<div class=cd style="border-left-color:#16a34a"><div class=a><span>COFINS</span><span class="tg ok">Apurado</span></div><div class=v>R$ 545.510,20</div><div class=m>não cumulativo · créditos de insumos</div></div>
<div class=cd><div class=a><span>ISS</span><span class=tg>A conciliar</span></div><div class=v>R$ 64.880,00</div><div class=m>retenções recebidas e retidas</div></div>
<div class=cd style="border-left-color:#92400e"><div class=a><span>IRPJ / CSLL</span><span class=tg>Em estimativa</span></div><div class=v>R$ 402.150,00</div><div class=m>base de cálculo e ajustes</div></div>
<div class=cd style="background:#fef3c7"><div class=a><span>Conciliação fiscal × contábil</span></div><div class=m style="margin-top:6px;font-size:12.5px">Razão de impostos a recolher: R$ 724.500,00 · diferença: <b>R$ 0,00</b> ✔</div></div></div>"""
    return doc(f"<div class=g>{paper}{side}</div>", css, 1400, 900)

# ---------------------------------------------------------------- 14 ICMS (calculadora + mapa de tiles)
def s14_calc():
    css = """body{background:#eef2ff;padding:30px 38px;color:#1e1b4b}h1{font-size:27px;letter-spacing:-.5px}.s{font-size:13px;color:#4338ca;margin:4px 0 18px}.g{display:grid;grid-template-columns:360px 1fr 330px;gap:20px}
.p{background:#fff;border-radius:20px;padding:20px;box-shadow:0 14px 36px rgba(67,56,202,.14);border:1px solid #e0e7ff}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#4338ca;margin-bottom:14px}
.f{margin-bottom:11px}.f small{display:block;font-size:10.5px;color:#6366f1;margin-bottom:3px}.f div{border:1.5px solid #c7d2fe;border-radius:10px;padding:9px 12px;font-size:13.5px;background:#fafaff;font-weight:600}.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.tb{display:flex;gap:8px;margin-bottom:14px}.tb span{flex:1;text-align:center;padding:8px;border-radius:10px;font-size:12px;border:1.5px solid #c7d2fe;color:#4338ca}.tb span.on{background:#4338ca;color:#fff;font-weight:700}
.st{display:grid;grid-template-columns:34px 1fr;gap:12px;margin-bottom:16px}.st i{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#4338ca,#0ea5e9);color:#fff;font-style:normal;font-weight:700;display:flex;align-items:center;justify-content:center}.st b{font-size:13.5px}.st code{display:block;margin-top:5px;background:#0f172a;color:#a5b4fc;border-radius:9px;padding:8px 11px;font-size:12px;font-family:'Liberation Mono',monospace}.st em{display:block;font-style:normal;color:#059669;font-weight:700;margin-top:4px;font-size:13px}
.rs{background:linear-gradient(160deg,#312e81,#4338ca);color:#fff;border-radius:20px;padding:22px;margin-bottom:16px}.rs span{font-size:11px;text-transform:uppercase;letter-spacing:1.2px;opacity:.8}.rs b{display:block;font-size:34px;margin:8px 0 4px}.rs i{font-style:normal;font-size:12px;opacity:.85}
.ln{display:flex;justify-content:space-between;font-size:13px;padding:9px 0;border-bottom:1px solid #eef2ff}.ln b{color:#312e81}.nt{margin-top:14px;font-size:11px;color:#6366f1;line-height:1.45}"""
    body = f"""<h1>Cálculo de ICMS</h1><div class=s>Operação interestadual com substituição tributária · valores e alíquotas ilustrativos</div><div class=g>
<div class=p><h3>Dados da operação</h3><div class=two><div class=f><small>UF origem</small><div>SP</div></div><div class=f><small>UF destino</small><div>MG</div></div></div><div class=f><small>NCM / CFOP</small><div>8517.62.77 · 6.102</div></div><div class=f><small>Valor da mercadoria</small><div>R$ 10.000,00</div></div>
<div class=two><div class=f><small>Alíq. interestadual</small><div>12%</div></div><div class=f><small>Alíq. interna destino</small><div>18%</div></div></div><div class=f><small>MVA (ST)</small><div>40%</div></div><div class=tb><span>Consumidor final (DIFAL)</span><span class=on>Revenda com ST</span></div></div>
<div class=p><h3>Memória de cálculo</h3>
<div class=st><i>1</i><div><b>Gross-up · ICMS “por dentro”</b><code>8.800,00 ÷ (1 − 12%) = 10.000,00</code></div></div>
<div class=st><i>2</i><div><b>ICMS próprio da operação</b><code>10.000,00 × 12% = 1.200,00</code><em>R$ 1.200,00</em></div></div>
<div class=st><i>3</i><div><b>Base de cálculo da ST</b><code>10.000,00 × (1 + 40%) = 14.000,00</code></div></div>
<div class=st><i>4</i><div><b>ICMS-ST a recolher</b><code>14.000,00 × 18% − 1.200,00 = 1.320,00</code><em>R$ 1.320,00</em></div></div>
<div class=st><i>5</i><div><b>Conferência com a nota fiscal</b><code>valor destacado = valor calculado ✔</code></div></div></div>
<div><div class=rs><span>ICMS-ST a recolher</span><b>R$ 1.320,00</b><i>carga total (próprio + ST): R$ 2.520,00 · 25,2%</i></div><div class=p><h3>Resumo</h3><div class=ln><span>ICMS próprio</span><b>R$ 1.200,00</b></div><div class=ln><span>ICMS-ST</span><b>R$ 1.320,00</b></div><div class=ln><span>Base ST</span><b>R$ 14.000,00</b></div><div class=ln><span>DIFAL (se aplicável)</span><b>R$ 600,00</b></div><div class=nt>Parâmetros (alíquotas, MVA, regras por NCM) lidos de tabelas no SQL Server. Exemplo didático, não é orientação fiscal.</div></div></div></div>"""
    return doc(body, css, 1400, 640)

def s14_mapa():
    css = """body{background:#0f172a;padding:30px 44px;color:#e0e7ff;display:flex;gap:40px}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#a5b4fc;margin:4px 0 20px}.l{flex:1}.r{width:380px;padding-top:70px}
.t{position:absolute;width:74px;height:74px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:16px}.t small{font-size:11px;font-weight:400;opacity:.9}
.lg{display:flex;gap:16px;margin-top:14px;font-size:12px}.lg i{display:inline-block;width:12px;height:12px;border-radius:4px;margin-right:6px}.c{background:#1e293b;border-radius:16px;padding:16px;margin-bottom:14px;border:1px solid #334155}.c h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#a5b4fc;margin-bottom:10px}.ln{display:flex;justify-content:space-between;font-size:13px;padding:7px 0;border-bottom:1px solid #334155}"""
    pos = {"RR": (2, 0), "AP": (4, 0), "AM": (1, 1), "PA": (3, 1), "MA": (4, 1), "CE": (5, 1), "RN": (6, 1), "AC": (0, 2), "RO": (1, 2), "MT": (2, 2), "TO": (3, 2), "PI": (4, 2), "PE": (5, 2), "PB": (6, 2), "MS": (2, 3), "GO": (3, 3), "BA": (4, 3), "AL": (5, 3), "SE": (6, 3), "DF": (3, 4), "MG": (4, 4), "ES": (5, 4), "SP": (3, 5), "RJ": (4, 5), "PR": (2, 5), "SC": (2, 6), "RS": (2, 7)}
    R = random.Random(14); col = {17: "#0ea5e9", 18: "#6366f1", 19: "#a855f7", 20: "#ec4899", 22: "#f43f5e"}
    tl = ""
    for u, (cx, cy) in pos.items():
        a = R.choice([17, 18, 18, 19, 20, 20, 22]); tl += f'<div class=t style="left:{cx*82}px;top:{cy*82}px;background:{col[a]}">{u}<small>{a}%</small></div>'
    lg = "".join(f"<span><i style='background:{c}'></i>{a}%</span>" for a, c in col.items())
    body = f"""<div class=l><h1>Alíquotas internas por UF</h1><div class=s>Mapa de blocos (cada quadrado é uma UF) · valores ilustrativos</div><div style="position:relative;height:610px;width:600px">{tl}</div><div class=lg>{lg}</div></div>
<div class=r><div class=c><h3>Como a tabela é usada</h3><div class=ln><span>Alíquota interna</span><span>por UF</span></div><div class=ln><span>Alíquota interestadual</span><span>origem × destino</span></div><div class=ln><span>MVA da ST</span><span>por NCM + UF</span></div><div class=ln><span>Benefícios / reduções</span><span>por regra</span></div></div>
<div class=c><h3>Validação em lote</h3><div class=ln><span>Itens calculados</span><b>18.402</b></div><div class=ln><span>ICMS igual ao da nota</span><b style="color:#34d399">17.936</b></div><div class=ln><span>Divergentes</span><b style="color:#fbbf24">466</b></div><div class=ln><span>Sem regra cadastrada</span><b style="color:#f87171">12</b></div></div></div>"""
    return doc(body, css, 1400, 800)

# ---------------------------------------------------------------- 15 Reforma tributária
def s15_trans():
    css = """body{background:linear-gradient(135deg,#f0fdf4,#fefce8 60%,#eff6ff);padding:30px 40px;color:#14532d}h1{font-size:28px;letter-spacing:-.5px}.s{font-size:13px;color:#166534;margin:4px 0 18px}
.g{display:grid;grid-template-columns:1.35fr 1fr;gap:20px}.p{background:#fff;border-radius:20px;padding:20px;box-shadow:0 12px 32px rgba(22,101,52,.12);border:1px solid #dcfce7}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#15803d;margin-bottom:10px}
.tl{display:grid;grid-template-columns:repeat(8,1fr);gap:8px;margin-top:18px}.y{background:#fff;border-radius:14px;padding:10px;border-top:5px solid var(--c);font-size:11px;box-shadow:0 6px 16px rgba(0,0,0,.06);min-height:140px}.y b{display:block;font-size:16px;color:#14532d;margin-bottom:4px}.y span{color:#475569;line-height:1.35;display:block}
.k{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}.kc{background:#fff;border-radius:16px;padding:12px 14px;border:1px solid #dcfce7}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;color:#15803d}.kc b{display:block;font-size:22px;margin-top:3px;color:#14532d}
.ln{display:flex;justify-content:space-between;font-size:12.5px;padding:9px 0;border-bottom:1px solid #ecfdf5}.ln b{color:#15803d}.nt{font-size:11px;color:#64748b;margin-top:10px}"""
    yrs = [str(y) for y in range(2026, 2034)]
    data = [(y, a, b) for y, a, b in zip(yrs, [100, 100, 100, 90, 80, 70, 60, 0], [0, 0, 0, 10, 20, 30, 40, 100])]
    ch = bars(data, ["#94a3b8", "#16a34a"], 760, 300, "#475569", "#e2e8f0", stacked=True, series=["ICMS/ISS (% da alíquota atual)", "IBS (% da referência)"], bw=.55)
    ev = [("2026", "#3b82f6", "Teste: CBS 0,9% + IBS 0,1%, destacados nas notas"), ("2027", "#16a34a", "CBS cobrada · PIS/Cofins extintos · IPI zerado (exceto ZFM)"), ("2028", "#16a34a", "Mesmas regras de 2027"), ("2029", "#eab308", "ICMS/ISS a 90% · IBS entra"), ("2030", "#eab308", "ICMS/ISS a 80%"), ("2031", "#eab308", "ICMS/ISS a 70%"), ("2032", "#eab308", "ICMS/ISS a 60%"), ("2033", "#ef4444", "ICMS e ISS extintos · regime pleno")]
    tl = "".join(f'<div class=y style="--c:{c}"><b>{y}</b><span>{t}</span></div>' for y, c, t in ev)
    body = f"""<h1>Reforma tributária · transição 2026–2033</h1><div class=s>Como a base de dados acompanha a troca de PIS/Cofins, ICMS, ISS e IPI por CBS, IBS e Imposto Seletivo · calendário conforme EC 132/2023 e LC 214/2025</div>
<div class=k><div class=kc><span>Tributos que saem</span><b>PIS · Cofins · ICMS · ISS · IPI</b></div><div class=kc><span>Tributos que entram</span><b>CBS · IBS · IS</b></div><div class=kc><span>Fim da transição</span><b>2033</b></div></div>
<div class=g><div class=p><h3>Convivência dos sistemas ao longo dos anos</h3>{ch}</div><div class=p><h3>O que o modelo de dados precisa cobrir</h3><div class=ln><span>Campos de CBS/IBS nos documentos fiscais</span><b>NF-e · NFS-e</b></div><div class=ln><span>Cadastro de produtos e serviços</span><b>NCM · NBS · classificação</b></div><div class=ln><span>Créditos na compra (não cumulatividade)</span><b>regra por operação</b></div><div class=ln><span>Convivência ICMS/ISS × IBS</span><b>2029 a 2032</b></div><div class=ln><span>Regimes e benefícios</span><b>por NCM e UF</b></div><div class=nt>Alíquotas de referência definitivas dependem do Senado; o projeto usa parâmetros editáveis.</div></div></div>
<div class=tl>{tl}</div>"""
    return doc(body, css, 1400, 780)

def s15_sim():
    css = """body{background:#fffef5;padding:30px 40px;color:#1e3a8a}h1{font-size:27px;letter-spacing:-.4px}.s{font-size:13px;color:#a16207;margin:4px 0 18px}.g{display:grid;grid-template-columns:340px 1fr;gap:20px}
.p{background:#fff;border-radius:20px;padding:20px;box-shadow:0 12px 32px rgba(30,58,138,.12);border:1px solid #fef08a}.p h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#a16207;margin-bottom:12px}
.f{margin-bottom:16px}.f small{display:flex;justify-content:space-between;font-size:12px;color:#1e3a8a;margin-bottom:6px;font-weight:700}.tr{height:8px;background:#e0e7ff;border-radius:8px;position:relative}.tr i{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,#2563eb,#16a34a);border-radius:8px}.tr u{position:absolute;top:-5px;width:18px;height:18px;border-radius:50%;background:#fff;border:3px solid #2563eb}
.k{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:16px}.kc{border-radius:18px;padding:14px 16px;color:#fff}.kc span{font-size:11px;text-transform:uppercase;letter-spacing:1px;opacity:.9}.kc b{display:block;font-size:26px;margin-top:4px}
.nt{font-size:11.5px;color:#a16207;background:#fefce8;border:1px solid #fde047;border-radius:12px;padding:10px 12px;line-height:1.45;margin-top:6px}"""
    yrs = [str(y) for y in range(2026, 2034)]
    data = [(y, a, b) for y, a, b in zip(yrs, [28, 28, 28, 27.6, 27.2, 26.8, 26.4, 26.5], [28, 27.5, 27.5, 27.4, 27, 26.6, 26.3, 26.5])]
    ch = line(data, ["#94a3b8", "#16a34a"], 800, 300, "#475569", "#e2e8f0", series=["Carga atual (ilustrativa)", "Carga no novo modelo (ilustrativa)"], ymin=24, mfill="#fff")
    body = f"""<h1>Simulador de impacto · carga atual × novo modelo</h1><div class=s>Cenário didático com percentuais ilustrativos · não é projeção oficial</div><div class=g>
<div class=p><h3>Premissas editáveis</h3><div class=f><small><span>Receita mensal</span><span>R$ 10,0 mi</span></small><div class=tr><i style="width:55%"></i><u style="left:52%"></u></div></div>
<div class=f><small><span>Compras com direito a crédito</span><span>62%</span></small><div class=tr><i style="width:62%"></i><u style="left:59%"></u></div></div>
<div class=f><small><span>Participação de serviços</span><span>35%</span></small><div class=tr><i style="width:35%"></i><u style="left:32%"></u></div></div>
<div class=f><small><span>Repasse ao preço</span><span>40%</span></small><div class=tr><i style="width:40%"></i><u style="left:37%"></u></div></div><div class=nt>Regime, NCM e fornecedores vêm da base histórica de faturamento e compras no SQL Server.</div></div>
<div><div class=k><div class=kc style="background:linear-gradient(135deg,#2563eb,#1e40af)"><span>Carga atual</span><b>28,0%</b></div><div class=kc style="background:linear-gradient(135deg,#16a34a,#15803d)"><span>Novo modelo (2033)</span><b>26,5%</b></div><div class=kc style="background:linear-gradient(135deg,#eab308,#a16207)"><span>Diferença</span><b>−1,5 p.p.</b></div></div>
<div class=p><h3>Carga tributária estimada por ano</h3>{ch}</div></div></div>"""
    return doc(body, css, 1400, 640)

# ---------------------------------------------------------------- 16 Migração de banco de dados
def s16():
    css = """body{background:#f1f5f9;padding:26px 36px;color:#0f172a}h1{font-size:26px;letter-spacing:-.4px}.s{font-size:13px;color:#475569;margin:4px 0 16px}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.kc{background:#fff;border-radius:16px;padding:12px 16px;border-top:5px solid var(--c);box-shadow:0 6px 18px rgba(15,23,42,.08)}.kc span{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;color:#64748b}.kc b{display:block;font-size:22px;margin-top:3px}
.hd{display:grid;grid-template-columns:250px 1fr 250px 280px;gap:10px;font-size:11px;text-transform:uppercase;letter-spacing:1.1px;color:#64748b;margin-bottom:8px;padding:0 6px}
.r{display:grid;grid-template-columns:250px 1fr 250px 280px;gap:10px;align-items:center;margin-bottom:10px}.bx{background:#fff;border-radius:12px;padding:12px 14px;border:1px solid #cbd5e1;font-family:'Liberation Mono',monospace;font-size:12.5px;box-shadow:0 3px 10px rgba(15,23,42,.06)}.bx small{display:block;font-family:'Liberation Sans',Arial;color:#64748b;font-size:10.5px;margin-top:2px}
.bx.d{border-color:#0ea5e9;background:#f0f9ff}.ar{position:relative;height:2px;background:#94a3b8}.ar:after{content:'';position:absolute;right:-2px;top:-5px;border:6px solid transparent;border-left:9px solid #94a3b8;border-right:0}.ar span{position:absolute;left:50%;top:-24px;transform:translateX(-50%);background:#fff;border:1px solid #cbd5e1;border-radius:20px;padding:2px 12px;font-size:11px;font-weight:700;white-space:nowrap;font-family:'Liberation Sans',Arial}
.ar.ok{background:#16a34a}.ar.ok:after{border-left-color:#16a34a}.ar.ok span{color:#166534;border-color:#86efac;background:#f0fdf4}.ar.wr{background:#f59e0b}.ar.wr:after{border-left-color:#f59e0b}.ar.wr span{color:#92400e;border-color:#fcd34d;background:#fffbeb}
.sm{background:#fff;border-radius:12px;padding:10px 14px;font-size:12px;border:1px solid #cbd5e1}.sm b{font-family:'Liberation Mono',monospace}
.ft{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}.p{background:#0f172a;color:#cbd5e1;border-radius:16px;padding:16px 18px;font-family:'Liberation Mono',monospace;font-size:12px;line-height:1.8}.p .g{color:#4ade80}.p .y{color:#fbbf24}.pl{background:#fff;border-radius:16px;padding:16px 18px;border:1px solid #cbd5e1}.pl h3{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#0284c7;margin-bottom:10px}.pl div{display:flex;justify-content:space-between;font-size:12.5px;padding:7px 0;border-bottom:1px solid #f1f5f9}"""
    rows = [("dbo.Lancamentos", "1.204.331 linhas", "fin.lancamento", "1.204.331 linhas", "ok", "Σ valor: R$ 48.210.334.120,55 = ✔"), ("dbo.Fornecedores", "18.402 linhas", "fin.fornecedor", "18.402 linhas", "ok", "chave única ✔"), ("dbo.PlanoContas", "1.184 linhas", "fin.plano_contas", "1.184 linhas", "ok", "FKs ✔"), ("dbo.Imobilizado", "52.870 linhas", "ativo.imobilizado", "52.870 linhas", "ok", "Σ valor: R$ 3.944.180.020,10 = ✔"), ("dbo.Clientes", "9.311 linhas", "fin.cliente", "9.309 linhas", "wr", "2 duplicados removidos"), ("dbo.Rateios", "210.004 linhas", "fin.rateio", "210.004 linhas", "ok", "decimal(18,2) ✔")]
    rs = "".join(f'<div class=r><div class=bx>{a}<small>{b}</small></div><div class="ar {k}"><span>{"✔ conferido" if k=="ok" else "⚠ ajustado"}</span></div><div class="bx d">{c}<small>{d}</small></div><div class=sm>{e}</div></div>' for a, b, c, d, k, e in rows)
    body = f"""<h1>Migração de banco de dados</h1><div class=s>Reconciliação entre a base legada e a nova base: linhas, somas de valores e integridade · dados fictícios</div>
<div class=k><div class=kc style="--c:#0ea5e9"><span>Tabelas migradas</span><b>6 de 6</b></div><div class=kc style="--c:#16a34a"><span>Linhas movidas</span><b>1.495.102</b></div><div class=kc style="--c:#16a34a"><span>Σ valores conferidos</span><b>100%</b></div><div class=kc style="--c:#f59e0b"><span>Ajustes</span><b>1</b></div></div>
<div class=hd><span>Origem · base legada</span><span></span><span>Destino · nova base</span><span>Validação</span></div>{rs}
<div class=ft><div class=p><span class=g>$</span> python migrar.py --tabela fin.lancamento<br><span class=g>✔</span> staging carregado ........ 1.204.331<br><span class=g>✔</span> contagem origem = destino<br><span class=g>✔</span> soma de valores confere<br><span class=y>!</span> dbo.Clientes: 2 duplicados<br><span class=g>✔</span> pronto para virada (cutover)</div>
<div class=pl><h3>Plano de virada</h3><div><span>1. Congelar escrita na origem</span><b>sex 19h</b></div><div><span>2. Carga final incremental</span><b>sex 19h30</b></div><div><span>3. Reconciliação automática</span><b>sex 20h</b></div><div><span>4. Apontar apps para a nova base</span><b>sáb 8h</b></div><div><span>5. Plano de retorno (rollback)</span><b>pronto</b></div></div></div>"""
    return doc(body, css, 1400, 880)

SCREENS_B = {
    "dashboards-html__painel": s10(), "digital-inventory__apps": s11_apps(), "digital-inventory__fluxos": s11_flow(), "digital-inventory__lista": s11_list(),
    "saneamento-bases-dados__antes-depois": s12(), "apuracao-tributos__livro": s13(), "calculo-icms__calculadora": s14_calc(), "calculo-icms__mapa": s14_mapa(),
    "reforma-tributaria__transicao": s15_trans(), "reforma-tributaria__simulador": s15_sim(), "migracao-banco-dados__reconciliacao": s16(),
}
