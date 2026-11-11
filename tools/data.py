# -*- coding: utf-8 -*-
"""
FONTE ÚNICA DO CONTEÚDO. Edite aqui e rode:  python tools/build_site.py --pdf
(site, PDF e READMEs são regenerados a partir deste arquivo)

ATENÇÃO: a stack por projeto (camadas) e os bancos de dados são uma proposta baseada no que já
conversamos. Confira o que não for fiel ao que você realmente usou (veja REVISAR.md).
"""

PERFIL = {
    "nome": "Miguel Vinicius Moura Martins",
    "titulo": "Contábil · Financeiro · Fiscal · Dados",
    "headline": "Transformo processos contábeis, financeiros e fiscais em dados, automações e painéis.",
    "sobre": [
        "Trabalho na interseção entre contabilidade, finanças, fiscal e dados. Pego processos que costumam viver em planilhas e e-mails, como fechamento, conciliações, provisões, forecast e budget, apuração de impostos e obrigações fiscais, e os transformo em bases estruturadas, regras automatizadas e painéis.",
        "Construo as ferramentas que eu mesmo uso: apps em Python e Streamlit, consultas e modelagem em SQL, aplicativos e fluxos em Power Apps e Power Automate, painéis em Power BI e HTML. Também uso IA para criar cenários de teste, revisar código e integrar assistentes aos apps e dashboards.",
        "Meu foco é entregar ferramentas confiáveis, auditáveis e simples de usar, que o time consiga operar sem depender de mim.",
    ],
    "diferencial": "Entendo a regra de negócio, modelo os dados e automatizo. Cada ferramenta é validada contra o processo manual antes de entrar em uso.",
    "nome_curto": "Miguel Moura", "linkedin": "linkedin.com/in/miguel-moura-779b45267", "email": "mvmoura2004@gmail.com", "github": "MV-Dev-Finance",
    "local": "Brasil", "iniciais": "MM",
    "foto": "assets/foto.jpg",   # coloque sua foto aqui (use tools/foto.py); se não existir, aparecem as iniciais
}

METODO = [
    ("Entender a regra", "Começo pelo processo: o que a norma pede, onde o dado nasce e onde costuma divergir."),
    ("Modelar os dados", "Mapeio fontes (SAP, Excel, PDF, bancos SQL), defino chaves de cruzamento e padronizo formatos."),
    ("Automatizar", "Transformo a regra em Python, SQL ou Power Platform e entrego em um app simples para o time."),
    ("Validar", "Comparo com o processo manual, uso cenários de teste (inclusive gerados com IA) e deixo a trilha auditável."),
]

DOMINIOS = [
    ("Contabilidade e controladoria", [
        "Fechamento contábil", "Conciliações contábeis", "Provisões e accruals", "Contingências (CPC 25)", "Despesa antecipada",
        "Ativo imobilizado e inventário", "Depreciação", "Depósitos judiciais e cauções", "Lançamentos manuais", "Balanço e DRE",
        "Notas explicativas", "Plano de contas e centros de custo", "Consolidação e intercompany", "Controles internos e auditoria"]),
    ("Financeiro e planejamento", [
        "Forecast", "Budget e orçamento", "Orçado × realizado", "Análise de variações", "Fluxo de caixa", "Contas a pagar e a receber",
        "Aging e inadimplência", "Tesouraria e contas bancárias", "CAPEX e OPEX", "Business case e payback", "Rateios e custos", "KPIs e indicadores"]),
    ("Fiscal e tributário", [
        "Apuração de impostos", "ICMS (alíquotas, DIFAL, ST)", "PIS e COFINS", "ISS", "IRPJ e CSLL", "Retenções na fonte", "Créditos fiscais",
        "SPED (EFD, ECD, ECF)", "NF-e e NFS-e (XML)", "Reforma tributária (IBS, CBS, IS)", "Conciliação fiscal × contábil", "Obrigações acessórias", "Incentivos fiscais"]),
    ("Dados e sistemas", [
        "Modelagem de dados", "ETL e cargas", "Migração de bancos de dados", "Qualidade e saneamento de dados", "Extração de PDFs", "Integração entre sistemas",
        "Automação de processos", "Aplicativos corporativos", "Dashboards e BI"]),
]

TECNOLOGIAS = [
    ("Bancos de dados e SQL", [
        "SQL Server", "T-SQL", "PostgreSQL", "MySQL", "Oracle", "SQLite", "SAP HANA", "Azure SQL", "MS Access", "Dataverse", "SharePoint Lists",
        "Views e consultas", "Modelagem relacional", "ETL e carga", "Índices e desempenho"]),
    ("Linguagens e bibliotecas", [
        "Python", "pandas", "NumPy", "openpyxl", "XlsxWriter", "python-docx", "PyMuPDF", "SQLAlchemy", "Plotly", "Streamlit", "DAX", "Power Query (M)", "VBA", "JavaScript", "HTML e CSS", "Regex"]),
    ("Power Platform e BI", [
        "Power BI", "Power Apps", "Power Fx", "Power Automate", "SharePoint", "Power Query", "Teams", "Microsoft Forms", "AI Builder"]),
    ("ERP, fiscal e ferramentas", [
        "SAP (FBL3N e extrações)", "SAP GUI Scripting", "SPED (EFD, ECD, ECF)", "NF-e (XML)", "Excel avançado", "VS Code", "SSMS", "DBeaver", "Git e GitHub", "Jupyter", "Microsoft Copilot e IA generativa"]),
]

IA = {
    "titulo": "Inteligência artificial no meu trabalho",
    "intro": "Uso IA como parceira de desenvolvimento e como parte das soluções. Ela acelera o trabalho, mas a validação continua sendo minha: tudo é conferido contra o processo manual.",
    "pilares": [
        ("test", "Cenários de teste", "Peço cenários sintéticos que tentam quebrar a regra: duplicidades, valores negativos, datas fora do período, formatos mistos e planilhas vazias. Rodo, comparo com o esperado e ajusto o código."),
        ("search", "Testar e revisar código", "Uso a IA como par de revisão: explicar trechos, apontar casos não tratados, sugerir testes e melhorias de desempenho. Cada mudança é validada com números reais do processo manual."),
        ("chat", "IA dentro de apps e dashboards", "Integro assistentes que respondem perguntas sobre os dados do painel, explicam variações, resumem o fechamento e sugerem justificativas, sempre mostrando a fonte e a data da base."),
    ],
    "principios": ["Dados sintéticos nos testes", "A IA acelera, a validação é humana", "Fonte e data da base em cada resposta"],
}

PAPEL = "Defini a regra de negócio, modelei os dados, validei os números contra o processo manual e desenvolvi a ferramenta com apoio de IA."
PAPEL_PP = "Desenhei o aplicativo e os fluxos, modelei as listas e validei o processo em campo, com apoio de IA em melhorias de código e cenários de teste."

# Resultados medidos. Aparecem no site/PDF quando preenchidos: "slug": [("Indicador", "antes → depois")]
RESULTADOS = {
    "digital-inventory": [("Tempo de bipagem", "2 h → 1 h (≈ −50%)"), ("Tempo total do inventário", "5 h → 3 h (≈ −40%)"), ("Custo adicional de licenças", "R$ 0 · plataformas já licenciadas")],
}

AREAS = ["Judicial", "Provisões e CAPEX", "Controles e conciliações", "Fiscal e tributário", "Dados e plataformas"]

CAMADAS_ORDEM = [("fontes", "Fontes de dados"), ("dados", "Bancos e SQL"), ("proc", "Processamento"), ("ui", "Interface"), ("saida", "Entrega"), ("auto", "Automação")]

def T(a1, a2, hero, mode="light", pbg="#f6f8fc"): return dict(a1=a1, a2=a2, hero=hero, mode=mode, pbg=pbg)
def L(hero, biz, steps, stack, frame="bare"): return dict(hero=hero, biz=biz, steps=steps, stack=stack, frame=frame)

PROJETOS = [
 dict(slug="conciliacao-depositos-judiciais", n=1, area="Judicial", kind="App Streamlit", title="Conciliação de Depósitos Judiciais",
  tag="App único com seletor de tipo: Trabalhista, Regulatório, Cível e Tributário.",
  itens=["Depósito Tributário", "Depósito Trabalhista", "Depósito Regulatório", "Depósito Civil"], cover="civel",
  screens=[("civel", "Cível"), ("trabalhista", "Trabalhista"), ("regulatorio", "Regulatório"), ("tributario", "Tributário")],
  theme=T("#3b82f6", "#22d3ee", "#0a1226"), layout=L("band", "cards", "timeline", "rows", "browser"),
  contexto="Quando a empresa é parte em um processo, pode precisar depositar valores em juízo como garantia. Esse dinheiro continua sendo dela até o desfecho, então fica no ativo e é atualizado monetariamente (Selic) até ser levantado ou convertido em pagamento.",
  regras=["O saldo do razão (SAP) precisa bater com o controle da área jurídica, depósito a depósito", "A atualização segue a Selic acumulada desde a data do depósito até o fechamento", "Diferenças podem ser depósito sem controle, controle sem lançamento ou valor divergente", "A análise gerencial é feita por UF, via centro de custo"],
  dor="Cruzar milhares de linhas entre SAP, planilha da área e análise do mês anterior à mão, com macros pesadas e difíceis de auditar.",
  passos=[("Extração", "Razão do SAP (FBL3N) e controle da área em Excel, mais a análise do mês anterior como base."), ("Padronização", "Normalizo chaves, valores e datas e leio a tabela da Selic direto do PDF oficial."), ("Cruzamento nos dois sentidos", "Full join entre contábil e extra: SAP sem par no controle e controle sem par no SAP, cada um com motivo."), ("Cálculo", "Atualização monetária pela Selic acumulada e comparação com o saldo contábil, por processo."), ("Entrega", "Planilha de análise com capa, balanço, bases e resumo por UF, com alertas e cores, sem macro.")],
  camadas=dict(fontes=["SAP (FBL3N)", "Excel da área jurídica", "Selic (PDF oficial)"], dados=["SQL Server (staging e validação)", "pandas"], proc=["Python", "pandas", "openpyxl", "PyMuPDF"], ui=["Streamlit"], saida=["Excel multi-abas", "Alertas e resumo por UF"], auto=["Launcher .bat (porta livre)"]),
  feats=["Validação nos dois sentidos, com motivo e linha de origem", "Atualização pela Selic calculada pelo próprio app", "Resumo por UF com centro de custo mapeado", "Planilha final no padrão de análise da área", "Alertas e cores nas bases", "Histórico recolhido e cartões de resumo"],
  comp=["Conciliação contábil", "Atualização monetária", "Depósitos judiciais", "SQL"], ia="Cenários de teste com itens sem par, diferenças de centavos e Selic na virada do mês, além de revisão do código de cruzamento."),

 dict(slug="contingencias-judiciais", n=2, area="Judicial", kind="Documento + mapa de risco", title="Contingências Judiciais",
  tag="Classificação de risco e provisão para as naturezas Tributária, Trabalhista, Regulatória e Cível.",
  itens=["Contingência Tributária", "Contingência Trabalhista", "Contingência Regulatória", "Contingência Civil"], cover="nota",
  screens=[("nota", "Nota explicativa"), ("matriz", "Matriz de risco")],
  theme=T("#e11d48", "#fb7185", "#2a0a14"), layout=L("split", "banner", "grid", "tiles"),
  contexto="Contingência é uma possível obrigação futura decorrente de processos. Pelo CPC 25, se a perda é provável e o valor é estimável, reconhece-se uma provisão no passivo. Se é possível, apenas divulga-se em nota explicativa. Se é remota, nada é registrado.",
  regras=["Provável: provisão no balanço", "Possível: divulgação em nota explicativa", "Remota: sem registro", "A cada mês, a provisão varia por constituição, reversão, atualização e baixa"],
  dor="Garantir que o saldo contábil reflita a estimativa do jurídico e explicar a variação do mês para a gestão e para a auditoria.",
  passos=[("Extração", "Base de processos do jurídico e saldo do razão contábil."), ("Classificação", "Aplico o prognóstico e separo o que é provisão do que é divulgação."), ("Reconciliação", "Comparo saldo contábil e estimativa do jurídico por processo e natureza."), ("Abertura da variação", "Decomponho o movimento em constituição, reversão, atualização e baixa."), ("Entrega", "Nota explicativa em Word, matriz de risco e base para o lançamento.")],
  camadas=dict(fontes=["SAP", "Base do jurídico (Excel)"], dados=["SQL Server", "pandas"], proc=["Python", "pandas", "openpyxl", "python-docx"], ui=["Streamlit"], saida=["Nota explicativa (Word)", "Excel de variação", "Matriz de risco"], auto=[]),
  feats=["Classificação por prognóstico", "Provisão contábil × estimativa do jurídico", "Abertura da variação do mês", "Nota explicativa gerada em Word", "Matriz de risco probabilidade × impacto"],
  comp=["CPC 25", "Provisões", "Notas explicativas", "Análise de variações"], ia="Casos de borda de reclassificação de risco e testes da abertura de variação entre meses."),

 dict(slug="provisoes-opex-capex", n=3, area="Provisões e CAPEX", kind="Planilhas Excel", title="Provisões OPEX e CAPEX",
  tag="Provisão de gastos incorridos e não faturados, com estorno e comparação com o orçado.",
  itens=["Provisão OPEX", "Provisão CAPEX"], cover="opex", screens=[("opex", "Provisão OPEX"), ("capex", "Provisão CAPEX")],
  theme=T("#16a34a", "#84cc16", "#052e16"), layout=L("poster", "split", "big", "flow"),
  contexto="Pelo regime de competência, a despesa pertence ao mês em que o serviço foi prestado ou o bem foi recebido, mesmo sem nota fiscal. No fechamento, provisiona-se o que foi incorrido e não faturado. No mês seguinte, quando a nota chega, a provisão é estornada para não duplicar. OPEX vai para o resultado e CAPEX vai para o imobilizado em curso.",
  regras=["Incorrido e sem nota fiscal: provisionar no mês", "Nota recebida no mês seguinte: estornar a provisão", "OPEX afeta o resultado, CAPEX afeta o imobilizado", "Itens sem pedido, centro de custo ou ordem de investimento vão para revisão"],
  dor="Montar a lista de provisões a cada fechamento, separando OPEX e CAPEX, gerando o lançamento e o estorno sem esquecer nada.",
  passos=[("Extração", "Pedidos, recebimentos e notas lançadas no período."), ("Cruzamento", "Identifico o que foi recebido e ainda não faturado, por fornecedor e centro de custo."), ("Regras", "Classifico em OPEX ou CAPEX por natureza, centro de custo e ordem de investimento."), ("Lançamento", "Gero o lançamento de provisão e o estorno do mês seguinte."), ("Entrega", "Planilha com fórmulas, comparação com o orçado e lista de itens a revisar.")],
  camadas=dict(fontes=["SAP", "Pedidos e recebimentos"], dados=["SQL Server (cruzamentos)", "pandas"], proc=["Python", "pandas", "openpyxl"], ui=["Streamlit"], saida=["Planilha Excel com fórmulas", "Arquivo de lançamento e estorno"], auto=["Launcher .bat"]),
  feats=["Separação OPEX e CAPEX por regra", "Lançamento e estorno gerados automaticamente", "Comparativo orçado × realizado + provisão", "Lista de itens a revisar"],
  comp=["Regime de competência", "Provisões", "CAPEX e OPEX", "Orçamento"], ia="Casos com pedido sem recebimento, faturamento parcial e estorno no mês seguinte."),

 dict(slug="relatorios-capex", n=4, area="Provisões e CAPEX", kind="Waterfall + Kanban", title="Relatórios CAPEX: Fechamento e Justificativa",
  tag="Fechamento do CAPEX e justificativa das variações acima da faixa de tolerância.",
  itens=["Relatório de Fechamento CAPEX", "Relatório de Justificativa CAPEX"], cover="fechamento", screens=[("fechamento", "Fechamento"), ("justificativa", "Justificativas")],
  theme=T("#ea580c", "#f59e0b", "#2b1203"), layout=L("band", "cards", "zigzag", "rows"),
  contexto="CAPEX é o investimento em ativos de longo prazo. Enquanto a obra está em andamento, o valor fica em imobilizado em curso. Quando o ativo entra em operação, é capitalizado e passa a ser depreciado. A gestão acompanha orçado × realizado e exige justificativa quando a variação passa de uma faixa de tolerância.",
  regras=["Orçado × realizado × capitalizado por projeto", "Obras em andamento ficam em imobilizado em curso até a ativação", "Variação fora da faixa exige justificativa da área", "Justificativas pendentes são acompanhadas por área"],
  dor="Consolidar números de dezenas de projetos e correr atrás das justificativas manualmente todo mês.",
  passos=[("Extração", "Base de projetos com orçado, realizado e capitalizado."), ("Consolidação", "Agrego por projeto, categoria e período, acumulado do ano."), ("Filtro de tolerância", "Calculo a variação e separo o que ficou fora da faixa."), ("Justificativas", "Gero a lista por área com campo para o motivo e o status."), ("Entrega", "Waterfall do orçado ao realizado e quadro de justificativas.")],
  camadas=dict(fontes=["SAP", "Base de projetos (Excel)"], dados=["SQL Server", "pandas"], proc=["Python", "pandas", "openpyxl"], ui=["Streamlit"], saida=["Excel", "Relatório de justificativas"], auto=["Power Automate (cobrança de pendências)"]),
  feats=["Waterfall do orçado ao realizado", "Obras em andamento e capitalização", "Filtro automático das variações fora da faixa", "Quadro de justificativas por status"],
  comp=["CAPEX", "Imobilizado em curso", "Análise de variações", "Gestão de pendências"], ia="Revisão das faixas de tolerância e cenários de variação positiva e negativa."),

 dict(slug="relatorio-lancamentos-manuais", n=5, area="Controles e conciliações", kind="Console de auditoria", title="Relatório de Lançamentos Manuais",
  tag="Trilha de auditoria dos lançamentos feitos fora das rotinas automáticas.",
  itens=["Relatório de Lançamentos Manuais"], cover="console", screens=[("console", "Console")],
  theme=T("#ef4444", "#f97316", "#0b0e13", "dark", "#0b0e13"), layout=L("dark", "banner", "big", "flow"),
  contexto="Lançamentos manuais fogem das rotinas automáticas e por isso são ponto clássico de atenção de controles internos e auditoria. O que se olha: valor alto, ausência de justificativa, concentração no fim do período, usuário atípico e alçada.",
  regras=["Lançamentos manuais exigem justificativa e aprovação conforme a alçada", "Valores acima da alçada passam por revisão obrigatória", "Concentração no fim do período merece atenção", "A evidência precisa ser reproduzível para a auditoria"],
  dor="Sem um relatório estruturado, era difícil ver quem lançou, quanto e se havia justificativa.",
  passos=[("Extração", "Documentos do razão no período, com usuário, tipo, data, valor e texto."), ("Filtro", "Isolo o que é lançamento manual pelo tipo de documento e pela origem."), ("Classificação de risco", "Pontuo por valor, falta de texto, horário e alçada."), ("Destaques", "Separo os sem justificativa e os acima da alçada."), ("Entrega", "Console de revisão e evidência de controle em Excel.")],
  camadas=dict(fontes=["SAP (extração do razão)"], dados=["SQL Server (consultas)", "pandas"], proc=["Python", "pandas"], ui=["Power BI", "Streamlit"], saida=["Evidência de controle (Excel)"], auto=[]),
  feats=["Distribuição por dia do mês e por usuário", "Índice de risco do período", "Alertas por severidade", "Pronto para evidência de controle"],
  comp=["Controles internos", "Auditoria", "Análise de risco", "SQL"], ia="Cenários de lançamentos no fim do período e simulação de usuários atípicos para testar os alertas."),

 dict(slug="despesa-antecipada", n=6, area="Controles e conciliações", kind="Calculadora + Gantt", title="Despesa Antecipada: Conciliação, Vigência e Relatório Trimestral",
  tag="Três ferramentas para controlar a apropriação de despesas pagas antecipadamente.",
  itens=["Conciliação de Despesa Antecipada", "Calculadora de Vigência", "Relatório de Despesa Antecipada Trimestral"], cover="gantt",
  screens=[("calculadora", "Calculadora de vigência"), ("gantt", "Cronograma dos contratos"), ("trimestral", "Relatório trimestral")],
  theme=T("#0d9488", "#22d3ee", "#042f2e", "light", "#f0fdfa"), layout=L("split", "cards", "timeline", "tiles"),
  contexto="Pagamentos adiantados, como seguros, licenças e aluguéis, são ativo porque o benefício ainda será consumido. A cada mês apropria-se para despesa a parte consumida, proporcional ao tempo de vigência, até zerar o saldo.",
  regras=["Apropriação proporcional aos dias de vigência (pro rata dia)", "Saldo a apropriar = valor pago − valor já apropriado", "Vigências que começam ou terminam no meio do mês exigem cálculo por dias", "O saldo contábil precisa bater com o saldo recalculado por contrato"],
  dor="Recalcular contrato a contrato e conciliar com o razão consumia muito tempo e era fácil errar vigência.",
  passos=[("Extração", "Contratos, datas de vigência, valores pagos e saldo do razão."), ("Cálculo", "A calculadora gera o cronograma de apropriação pro rata dia."), ("Conciliação", "Comparo o saldo recalculado com o saldo contábil por contrato."), ("Divergências", "Marco no cronograma os contratos divergentes para ajuste."), ("Relatório", "Resumo trimestral: saldo inicial, adições, apropriações e saldo final.")],
  camadas=dict(fontes=["SAP", "Controle de contratos (Excel)"], dados=["SQL Server", "pandas"], proc=["Python", "pandas", "datetime"], ui=["Streamlit"], saida=["Excel", "Relatório trimestral"], auto=["Launcher .bat"]),
  feats=["Apropriação mensal pro rata dia", "Cronograma visual dos contratos", "Saldo contábil × saldo recalculado", "Movimentação trimestral do saldo"],
  comp=["Regime de competência", "Cálculo financeiro", "Conciliação", "Relatórios gerenciais"], ia="Testes de vigência: início e fim no meio do mês, ano bissexto e contratos de um único dia."),

 dict(slug="deposito-caucao", n=7, area="Controles e conciliações", kind="Cartões de contratos", title="Depósito Caução",
  tag="Conciliação do razão com o controle de contratos de locação.",
  itens=["Depósito Caução"], cover="cartoes", screens=[("cartoes", "Contratos")],
  theme=T("#7c3aed", "#c084fc", "#1e1038", "light", "#faf5ff"), layout=L("poster", "split", "grid", "rows"),
  contexto="Depósito caução é uma garantia dada em contratos, como os de locação. Fica no ativo, não vira despesa e é devolvido ao fim do contrato. O risco está em perder o prazo de devolução ou em ter saldo contábil diferente do contrato.",
  regras=["O saldo contábil precisa bater com o valor de cada contrato", "Vencimentos próximos exigem ação antecipada", "Devoluções pendentes precisam ser cobradas do locador"],
  dor="Faltava uma visão única do saldo, dos vencimentos e das devoluções pendentes.",
  passos=[("Extração", "Saldo do razão e controle de contratos."), ("Cruzamento", "Comparo contrato a contrato e destaco diferenças."), ("Prazos", "Calculo contratos vencendo em 90 dias e devoluções pendentes."), ("Entrega", "Cartões por contrato com status e lista de ações.")],
  camadas=dict(fontes=["SAP", "Controle de contratos (Excel / SharePoint)"], dados=["pandas"], proc=["Python", "pandas"], ui=["Streamlit"], saida=["Excel", "Painel de pendências"], auto=[]),
  feats=["Saldo contábil × saldo dos contratos", "Alerta de vencimentos em 90 dias", "Controle de devoluções pendentes", "Cartões com status por contrato"],
  comp=["Conciliação", "Gestão de contratos", "Controle de prazos"], ia="Cenários de vencimento na virada do ano e devoluções parciais."),

 dict(slug="analise-contas-bancarias", n=8, area="Controles e conciliações", kind="PDF → dados", title="Análise de Contas Bancárias",
  tag="Lê o saldo de dezenas de extratos em PDF de vários bancos e compara com o balanço.",
  itens=["Análise de Contas de Banco"], cover="extracao", screens=[("extracao", "Extração")],
  theme=T("#0284c7", "#38bdf8", "#082f49", "light", "#f0f9ff"), layout=L("band", "banner", "zigzag", "flow"),
  contexto="A conciliação bancária compara o saldo do extrato, no último dia do mês, com o saldo contábil da conta. As diferenças costumam ser lançamentos pendentes ou erros. O gargalo é que os extratos chegam em PDF e cada banco tem seu próprio layout, às vezes mais de um por banco.",
  regras=["No último dia do mês, saldo do extrato = saldo do balanço", "Sem movimento no dia, vale o último saldo anterior", "Cada banco tem layout e formato numérico próprios", "Contas com diferença precisam de explicação antes do fechamento"],
  dor="Mais de 90 extratos por mês, de cerca de 20 bancos, abertos um a um. O AI Builder do Power Automate exigia um modelo por layout e não deu conta de bancos com mais de 4 modelos.",
  passos=[("Leitura", "Extraio o texto dos PDFs com PyMuPDF; os escaneados são sinalizados."), ("Regras genéricas", "Em vez de um modelo por banco, busco linhas de saldo e a coluna de saldo dos extratos corridos."), ("Data de corte", "Escolho o saldo mais recente até o último dia do mês e converto o formato numérico brasileiro."), ("Comparação", "Cruzo com a relação de contas do balanço e marco as diferenças."), ("Entrega", "Excel com resumo, confiança (alta, média, baixa), linha encontrada e candidatos.")],
  camadas=dict(fontes=["Extratos bancários (PDF)", "Relação de contas do balanço"], dados=["SQL Server (histórico das extrações)", "pandas"], proc=["Python", "PyMuPDF", "Regex", "pandas", "openpyxl"], ui=["Script Python guiado (pasta e mês)"], saida=["Excel consolidado", "Confiança por extrato"], auto=[]),
  feats=["Leitura em lote de PDFs de vários layouts", "Confiança alta, média ou baixa por saldo", "Trecho do PDF de onde saiu o valor", "Contas sem extrato e extratos sem conta"],
  comp=["Conciliação bancária", "Tesouraria", "Extração de dados", "SQL"], ia="Testes com PDFs simulados de layouts diferentes para validar a leitura do saldo antes de usar nos extratos reais."),

 dict(slug="lancamento-docas", n=9, area="Controles e conciliações", kind="Wizard + log", title="Lançamento de Docas",
  tag="Da planilha base ao arquivo de lançamento contábil validado.",
  itens=["Lançamento Docas"], cover="terminal", screens=[("terminal", "Processamento")],
  theme=T("#22c55e", "#a3e635", "#05090a", "dark", "#05090a"), layout=L("dark", "cards", "timeline", "tiles"),
  contexto="Alguns lançamentos recorrentes partem de uma planilha de apuração e precisam virar um arquivo de lançamento para o ERP. Todo lote precisa ter débito igual a crédito, contas e centros de custo válidos e competência correta.",
  regras=["Débito = crédito em todo lote", "Conta e centro de custo precisam existir no plano de contas", "A data precisa estar dentro da competência"],
  dor="Montar o lançamento manualmente aumentava o risco de erro de conta, centro de custo e lote desbalanceado.",
  passos=[("Leitura", "Carrego a planilha base."), ("Validação", "Aplico regras de conta, centro de custo, valor e competência."), ("Erros", "Listo cada erro com a linha e a ação sugerida."), ("Geração", "Monto o arquivo de lançamento no layout do ERP."), ("Conferência", "Confirmo débito = crédito antes de entregar.")],
  camadas=dict(fontes=["Planilha base (Excel)", "Plano de contas"], dados=["pandas"], proc=["Python", "pandas", "openpyxl"], ui=["Streamlit"], saida=["Arquivo de lançamento (.xlsx)"], auto=["Launcher .bat"]),
  feats=["Validação por regra, linha a linha", "Log com avisos e erros", "Conferência automática de débito e crédito", "Arquivo pronto para carga"],
  comp=["Lançamentos contábeis", "Plano de contas", "Validação de dados"], ia="Cenários de lote desbalanceado, conta inexistente e data fora da competência."),

 dict(slug="dashboards-html", n=10, area="Dados e plataformas", kind="Dashboard HTML", title="Dashboards em HTML",
  tag="Painéis compartilháveis sem licença de BI: o arquivo é carregado e os dados somam ao painel.",
  itens=["Dashboards"], cover="painel", screens=[("painel", "Painel com upload")],
  theme=T("#2563eb", "#7c3aed", "#1e1b4b", "light", "#eef2ff"), layout=L("split", "split", "big", "rows", "browser"),
  contexto="A gestão precisa acompanhar números rapidamente, mas compartilhar dashboards de Power BI depende de licenças e de um fluxo de atualização. A saída foi levar a visualização para HTML, que abre em qualquer navegador e atualiza com um arquivo.",
  regras=["Os mesmos indicadores do Power BI, em formato leve e compartilhável", "A atualização não pode depender de licença individual", "Cada área atualiza o seu painel com um arquivo padronizado", "Evolução: dados em SQL Server, lidos por uma API"],
  dor="Dificuldade de compartilhar e atualizar dashboards sem Power BI Pro para todos. Uma pessoa atualizava tudo e as áreas não entendiam de dados.",
  passos=[("Mapeamento", "Defino quais dashboards do Power BI valem a migração."), ("Modelagem", "Preparo os dados em Excel e SQL no formato que o painel consome."), ("Painel em HTML", "KPIs, gráficos e tabelas em um único arquivo."), ("Atualização", "Upload de CSV/XLSX soma os dados no navegador, aceitando números no formato brasileiro."), ("Evolução", "Painel → API Python → SQL Server, com upload mensal validado.")],
  camadas=dict(fontes=["CSV / XLSX"], dados=["SQL Server (evolução)"], proc=["JavaScript (SheetJS)", "Power Query (origem BI)"], ui=["HTML, CSS e JavaScript"], saida=["Dashboard em HTML", "Exportação em CSV"], auto=["SharePoint (pasta por área)"]),
  feats=["Upload por arraste de arquivo", "KPIs e gráficos atualizados na hora", "Um único arquivo HTML, fácil de compartilhar", "Agrupar por qualquer coluna e somar qualquer valor"],
  comp=["Visualização de dados", "Power BI", "Gestão por indicadores"], ia="Apoio na construção da interface e nos testes de leitura de números no formato brasileiro."),

 dict(slug="digital-inventory", n=11, area="Dados e plataformas", kind="Power Apps · Power Automate · SharePoint", title="App Digital Inventory",
  tag="Inventário de estoque por número de série em lojas, feito 100% em Power Platform.",
  itens=["App Digital Inventory"], cover="apps", screens=[("apps", "Power Apps"), ("fluxos", "Power Automate"), ("lista", "SharePoint")],
  theme=T("#742774", "#0066ff", "#1a0b1f", "light", "#fbf7fc"), layout=L("poster", "banner", "zigzag", "flow"),
  contexto="No inventário físico, cada item com número de série precisa ser contado e comparado com o saldo do SAP. O que não é encontrado vira pendência, o que não pertence à loja é sinalizado, e as diferenças geram o ajuste contábil. Antes, a bipagem e a conferência eram manuais e demoradas.",
  regras=["Todo serial do SAP precisa ser bipado ou justificado", "Serial já bipado, de outro centro ou fora do SAP é sinalizado", "Pendências são recontadas antes de finalizar", "O relatório final traz valores, diferenças e ajustes e segue para assinatura"],
  dor="Bipagem completa de cerca de 2 horas e inventário de cerca de 5 horas, com consolidação manual e retrabalho depois da contagem.",
  passos=[("Carga da base SAP", "Bases do SAP (estoque por serial) alimentam a lista Serial_List no SharePoint."), ("Bipagem no app", "O Power Apps registra cada bip, atualiza a galeria e salva automaticamente na lista."), ("Pendências e recontagem", "Tela com só o que não foi encontrado; é possível remover um bip e recontar."), ("Importação e lotes", "Power Automate importa seriais de um Excel e limpa a lista em lote, sem travar o app."), ("Relatório e assinatura", "Prévia no app, PDFs finais, histórico no SharePoint e envio para assinatura eletrônica.")],
  camadas=dict(fontes=["Bases do SAP (estoque por serial)"], dados=["SharePoint Lists (Serial_List)"], proc=["Power Fx", "Power Automate"], ui=["Power Apps (app de bipagem)"], saida=["Relatório final em PDF", "Assinatura eletrônica (DocuSign)", "Histórico no SharePoint"], auto=["Importação de seriais via Excel", "Limpeza e atualização em lote"]),
  feats=["Salvamento automático a cada bip", "Remoção de bip com atualização sincronizada", "Tela de pendências (itens não encontrados)", "Controle de acesso por status da loja", "Feedback visual ao usuário", "Importação de seriais por Excel", "Relatório final e assinatura eletrônica"],
  comp=["Power Apps", "Power Automate", "SharePoint", "Inventário"], ia="O Copilot ajudou em melhorias de código (Power Fx) e na criação de cenários de teste do aplicativo.", papel=PAPEL_PP),

 dict(slug="saneamento-bases-dados", n=12, area="Dados e plataformas", kind="Antes × depois", title="Saneamento de Bases de Dados",
  tag="Diagnóstico e correção automática de qualidade de dados antes da carga.",
  itens=["Saneamento de bases de dados"], cover="antes-depois", screens=[("antes-depois", "Antes × depois")],
  theme=T("#db2777", "#a855f7", "#4a0d2c", "light", "#fff5fa"), layout=L("band", "cards", "grid", "tiles"),
  contexto="Decisões e conciliações são tão boas quanto a qualidade da base. Dados com duplicidades, campos vazios, formatos misturados ou contas sem de/para quebram cargas, cruzamentos e relatórios.",
  regras=["Chave única por registro", "Campos obrigatórios preenchidos", "Datas e valores em formato padronizado", "Todas as contas com de/para"],
  dor="Bases de várias fontes chegavam sujas e o retrabalho de limpeza se repetia a cada ciclo.",
  passos=[("Perfilamento", "Meço duplicados, nulos, formatos e contas sem de/para."), ("Regras", "Defino regras por campo e por tipo de problema."), ("Correção segura", "Corrijo automaticamente o que é seguro corrigir."), ("Pendências", "Listo o que precisa de decisão humana."), ("Prova", "Relatório de problemas antes × depois.")],
  camadas=dict(fontes=["Excel e CSV", "SQL Server", "PostgreSQL", "MySQL", "MS Access", "Oracle"], dados=["SQL Server (T-SQL)", "PostgreSQL"], proc=["Python", "pandas", "Regex"], ui=["Streamlit"], saida=["Base saneada", "Relatório antes × depois"], auto=["Launcher .bat"]),
  feats=["Remoção de duplicados por chave", "Padronização de datas e valores", "De/para de contas", "Relatório antes × depois"],
  comp=["Qualidade de dados", "Modelagem", "Governança de dados", "SQL"], ia="Geração de bases sujas sintéticas para testar cada regra de limpeza."),

 dict(slug="apuracao-tributos", n=13, area="Fiscal e tributário", kind="Livro de apuração", title="Apuração de Tributos",
  tag="Débitos, créditos e saldo a recolher por tributo, conciliados com o razão contábil.",
  itens=["Apuração de tributos"], cover="livro", screens=[("livro", "Livro de apuração")],
  theme=T("#b45309", "#eab308", "#2d1a05", "light", "#fbf6ea"), layout=L("split", "split", "timeline", "rows"),
  contexto="Apuração é o cálculo periódico do imposto a recolher: débitos (sobre saídas e receitas) menos créditos (sobre entradas e insumos), por tributo, estabelecimento e período. O resultado é um saldo a recolher ou um crédito a transportar, e precisa bater com o razão contábil e com as obrigações acessórias.",
  regras=["Saldo = débitos − créditos, por tributo e por estabelecimento", "Crédito depende de documento fiscal válido e da natureza da operação", "O regime define a regra: cumulativo ou não cumulativo", "Fiscal e contábil precisam conciliar (impostos a recolher e a recuperar)"],
  dor="Reunir notas, livros e ajustes de vários estabelecimentos em planilhas, com risco de crédito indevido e diferença entre o fiscal e o contábil.",
  passos=[("Extração", "Notas (XML), livros fiscais e razão contábil do período."), ("Padronização", "Normalizo CFOP, CST, NCM e UF e valido a chave dos documentos."), ("Cálculo", "Débito e crédito por tributo e estabelecimento, com estornos e ajustes."), ("Conciliação", "Comparo o saldo apurado com o razão de impostos a recolher e a recuperar."), ("Entrega", "Livro de apuração, valor a recolher, pendências e calendário de vencimentos.")],
  camadas=dict(fontes=["NF-e (XML)", "Livros fiscais (SAP)", "Excel"], dados=["SQL Server (staging fiscal)", "pandas"], proc=["Python", "pandas", "Decimal"], ui=["Streamlit"], saida=["Excel de apuração", "Conciliação fiscal × contábil", "Valor a recolher"], auto=["Power Automate (alerta de vencimentos)"]),
  feats=["Apuração por tributo e estabelecimento", "Conciliação fiscal × contábil", "Estornos e saldos credores", "Calendário de vencimentos", "Pendências por documento"],
  comp=["Apuração de impostos", "ICMS", "PIS e COFINS", "ISS", "Conciliação fiscal"], ia="Cenários de débito e crédito com estornos, créditos extemporâneos e saldos credores."),

 dict(slug="calculo-icms", n=14, area="Fiscal e tributário", kind="Calculadora + mapa de UFs", title="Cálculo de ICMS",
  tag="Calculadora e validação em lote de ICMS próprio, DIFAL e substituição tributária.",
  itens=["Cálculo de ICMS"], cover="calculadora", screens=[("calculadora", "Calculadora"), ("mapa", "Mapa de alíquotas")],
  theme=T("#4338ca", "#0ea5e9", "#1e1b4b", "light", "#eef2ff"), layout=L("band", "banner", "big", "flow"),
  contexto="O ICMS é um imposto estadual sobre a circulação de mercadorias e serviços e é calculado “por dentro”: o próprio imposto compõe a base. A alíquota depende da UF e da operação (interna ou interestadual). Em operações sujeitas a substituição tributária, a base é ajustada por uma margem (MVA) e o imposto é recolhido antecipadamente.",
  regras=["ICMS “por dentro”: a base inclui o próprio imposto", "Alíquota interna ou interestadual conforme origem e destino", "ST: base = valor × (1 + MVA) e ICMS-ST = base × alíquota interna − ICMS próprio", "Parâmetros variam por UF, NCM e regime e precisam estar versionados"],
  dor="Calcular na mão ou em planilhas com regras espalhadas, sem rastro do porquê de cada valor e sem comparar com o que foi destacado na nota.",
  passos=[("Parâmetros", "Tabelas de alíquotas, MVA e regras por UF e NCM em SQL Server."), ("Regras de cálculo", "ICMS próprio, DIFAL e ST implementados com Decimal para não perder centavos."), ("Cálculo em lote", "Recalculo item a item a partir do XML da nota."), ("Conferência", "Comparo com o valor destacado e com a apuração no SAP."), ("Entrega", "Memória de cálculo, lista de divergências e itens sem regra cadastrada.")],
  camadas=dict(fontes=["NF-e (XML)", "Tabelas de alíquotas e MVA", "SAP"], dados=["SQL Server (tabelas de parâmetros)", "pandas"], proc=["Python", "Decimal", "pandas"], ui=["Streamlit"], saida=["Memória de cálculo", "Excel de divergências"], auto=["Launcher .bat"]),
  feats=["Calculadora com memória de cálculo passo a passo", "ICMS próprio, DIFAL e ST", "Validação em lote contra a nota fiscal", "Mapa de alíquotas por UF", "Itens sem regra cadastrada"],
  comp=["ICMS", "DIFAL", "Substituição tributária", "NF-e"], ia="Casos de borda por UF, ST com MVA e arredondamento com Decimal. Os valores da tela são ilustrativos."),

 dict(slug="reforma-tributaria", n=15, area="Fiscal e tributário", kind="Linha do tempo + simulador", title="Reforma Tributária: Transição e Simulador",
  tag="Acompanhamento da transição para CBS, IBS e Imposto Seletivo e simulação de impacto.",
  itens=["Reforma tributária"], cover="transicao", screens=[("transicao", "Transição 2026–2033"), ("simulador", "Simulador de impacto")],
  theme=T("#15803d", "#facc15", "#0b2e13", "light", "#f7fee7"), layout=L("split", "cards", "zigzag", "tiles"),
  contexto="A reforma tributária do consumo (EC 132/2023 e LC 214/2025) substitui PIS, Cofins, ICMS, ISS e IPI por CBS, IBS e Imposto Seletivo, em uma transição de 2026 a 2033. Em 2026 há alíquotas de teste (CBS 0,9% e IBS 0,1%); em 2027 a CBS passa a ser cobrada e PIS/Cofins são extintos; de 2029 a 2032 ICMS e ISS caem a cada ano; em 2033 o novo regime fica pleno.",
  regras=["2026: teste com CBS 0,9% e IBS 0,1% destacados nos documentos", "2027: CBS cobrada, PIS/Cofins extintos e IPI zerado (exceto Zona Franca de Manaus)", "2029 a 2032: ICMS e ISS a 90%, 80%, 70% e 60% das alíquotas, com IBS crescente", "2033: ICMS e ISS extintos e regime pleno de IBS e CBS"],
  dor="Cada etapa muda uma variável diferente: documentos e cadastros, créditos, preço e caixa. Era preciso enxergar o impacto na base de dados da empresa, e não só no texto da lei.",
  passos=[("Mapeamento", "Levanto tributos atuais por operação, produto e serviço."), ("Base histórica", "Modelo faturamento e compras em SQL, com NCM, NBS, regime e créditos."), ("Calendário", "Parametrizo as regras e percentuais de cada ano da transição."), ("Simulação", "Comparo a carga atual com o novo modelo por cenário."), ("Entrega", "Painel de acompanhamento e relatório de impacto, com premissas editáveis.")],
  camadas=dict(fontes=["Base de faturamento e compras", "Cadastro de produtos e serviços (NCM/NBS)", "Calendário da transição"], dados=["SQL Server (histórico)", "Power Query"], proc=["Python", "pandas", "DAX"], ui=["Power BI", "Excel"], saida=["Cenários e relatório de impacto"], auto=[]),
  feats=["Linha do tempo 2026–2033", "Participação de ICMS/ISS e IBS por ano", "Simulador com premissas editáveis", "Pendências de cadastro (NCM, NBS, regra de crédito)"],
  comp=["Reforma tributária", "IBS e CBS", "Planejamento tributário", "Modelagem de cenários"], ia="Simulação de cenários por ano da transição e revisão das premissas de cálculo. Percentuais do simulador são ilustrativos."),

 dict(slug="migracao-banco-dados", n=16, area="Dados e plataformas", kind="Reconciliação origem × destino", title="Migração de Banco de Dados",
  tag="Migração entre bases com reconciliação de linhas, valores e integridade antes da virada.",
  itens=["Migração de banco de dados"], cover="reconciliacao", screens=[("reconciliacao", "Reconciliação")],
  theme=T("#0284c7", "#f97316", "#0f172a", "light", "#f1f5f9"), layout=L("dark", "split", "grid", "flow"),
  contexto="Migrar uma base não é só copiar tabelas: é provar que nada se perdeu. Isso exige mapear esquema e tipos, carregar por etapas, reconciliar contagens e somas de valores entre origem e destino e planejar a virada (cutover) com plano de retorno.",
  regras=["Contagem de linhas igual entre origem e destino", "Soma de valores por período igual (valor monetário nunca em float)", "Chaves únicas e chaves estrangeiras preservadas", "Virada com janela definida e plano de retorno (rollback)"],
  dor="Bases legadas em formatos e tipos diferentes, com risco de perder linhas, arredondar valores ou quebrar relatórios que dependem delas.",
  passos=[("Inventário e mapeamento", "Levanto tabelas, tipos e dependências e defino o de/para de esquema."), ("Carga em etapas", "Staging, carga completa e depois incremental até a virada."), ("Reconciliação", "Comparo contagens, somas e checksums tabela a tabela."), ("Tratamento", "Corrijo duplicados e tipos antes de liberar."), ("Virada e retorno", "Congelo a origem, carrego o final, valido e aponto os apps para a nova base.")],
  camadas=dict(fontes=["SQL Server (legado)", "MS Access", "Excel e CSV", "Oracle"], dados=["SQL Server", "Azure SQL", "PostgreSQL", "MySQL"], proc=["SQL (T-SQL)", "Python", "SQLAlchemy", "pandas"], ui=["Console e relatório de reconciliação"], saida=["Relatório de reconciliação", "Plano de virada e rollback"], auto=["Agendamento de cargas"]),
  feats=["Reconciliação por tabela: linhas e somas", "Checagem de chaves e duplicados", "Tipos monetários em decimal", "Plano de virada e rollback", "Log de execução auditável"],
  comp=["Migração de dados", "SQL", "Reconciliação", "Governança de dados"], ia="Geração de cenários de divergência (duplicados, tipos numéricos, datas) para testar a reconciliação."),
]

DASH = [
    ("forecast-budget", "Forecast × Budget", "Neon escuro", "Planejamento"), ("dre-executiva", "DRE executiva", "Editorial", "Contabilidade"),
    ("apuracao-tributos", "Apuração de tributos", "Laranja claro", "Fiscal"), ("fluxo-de-caixa", "Fluxo de caixa", "Verde menta", "Financeiro"),
    ("contingencias-risco", "Contingências · mapa de risco", "Roxo escuro", "Jurídico"), ("capex-projetos", "CAPEX por projeto", "Minimalista", "Investimentos"),
    ("reforma-tributaria", "Reforma tributária", "Gradiente", "Fiscal"), ("contas-a-pagar-aging", "Contas a pagar · aging", "Azul claro", "Financeiro"),
    ("orcamento-centro-custo", "Orçamento por centro de custo", "Pastel", "Planejamento"),
]
