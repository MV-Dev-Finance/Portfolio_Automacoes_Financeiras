# Revise antes de publicar

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
| 01 Conciliação de Depósitos Judiciais | **Fontes de dados:** SAP (FBL3N), Excel da área jurídica, Selic (PDF oficial) · **Bancos e SQL:** SQL Server (staging e validação), pandas · **Processamento:** Python, pandas, openpyxl, PyMuPDF · **Interface:** Streamlit · **Entrega:** Excel multi-abas, Alertas e resumo por UF · **Automação:** Launcher .bat (porta livre) |
| 02 Contingências Judiciais | **Fontes de dados:** SAP, Base do jurídico (Excel) · **Bancos e SQL:** SQL Server, pandas · **Processamento:** Python, pandas, openpyxl, python-docx · **Interface:** Streamlit · **Entrega:** Nota explicativa (Word), Excel de variação, Matriz de risco |
| 03 Provisões OPEX e CAPEX | **Fontes de dados:** SAP, Pedidos e recebimentos · **Bancos e SQL:** SQL Server (cruzamentos), pandas · **Processamento:** Python, pandas, openpyxl · **Interface:** Streamlit · **Entrega:** Planilha Excel com fórmulas, Arquivo de lançamento e estorno · **Automação:** Launcher .bat |
| 04 Relatórios CAPEX: Fechamento e Justificativa | **Fontes de dados:** SAP, Base de projetos (Excel) · **Bancos e SQL:** SQL Server, pandas · **Processamento:** Python, pandas, openpyxl · **Interface:** Streamlit · **Entrega:** Excel, Relatório de justificativas · **Automação:** Power Automate (cobrança de pendências) |
| 05 Relatório de Lançamentos Manuais | **Fontes de dados:** SAP (extração do razão) · **Bancos e SQL:** SQL Server (consultas), pandas · **Processamento:** Python, pandas · **Interface:** Power BI, Streamlit · **Entrega:** Evidência de controle (Excel) |
| 06 Despesa Antecipada: Conciliação, Vigência e Relatório Trimestral | **Fontes de dados:** SAP, Controle de contratos (Excel) · **Bancos e SQL:** SQL Server, pandas · **Processamento:** Python, pandas, datetime · **Interface:** Streamlit · **Entrega:** Excel, Relatório trimestral · **Automação:** Launcher .bat |
| 07 Depósito Caução | **Fontes de dados:** SAP, Controle de contratos (Excel / SharePoint) · **Bancos e SQL:** pandas · **Processamento:** Python, pandas · **Interface:** Streamlit · **Entrega:** Excel, Painel de pendências |
| 08 Análise de Contas Bancárias | **Fontes de dados:** Extratos bancários (PDF), Relação de contas do balanço · **Bancos e SQL:** SQL Server (histórico das extrações), pandas · **Processamento:** Python, PyMuPDF, Regex, pandas, openpyxl · **Interface:** Script Python guiado (pasta e mês) · **Entrega:** Excel consolidado, Confiança por extrato |
| 09 Lançamento de Docas | **Fontes de dados:** Planilha base (Excel), Plano de contas · **Bancos e SQL:** pandas · **Processamento:** Python, pandas, openpyxl · **Interface:** Streamlit · **Entrega:** Arquivo de lançamento (.xlsx) · **Automação:** Launcher .bat |
| 10 Dashboards em HTML | **Fontes de dados:** CSV / XLSX · **Bancos e SQL:** SQL Server (evolução) · **Processamento:** JavaScript (SheetJS), Power Query (origem BI) · **Interface:** HTML, CSS e JavaScript · **Entrega:** Dashboard em HTML, Exportação em CSV · **Automação:** SharePoint (pasta por área) |
| 11 App Digital Inventory | **Fontes de dados:** Bases do SAP (estoque por serial) · **Bancos e SQL:** SharePoint Lists (Serial_List) · **Processamento:** Power Fx, Power Automate · **Interface:** Power Apps (app de bipagem) · **Entrega:** Relatório final em PDF, Assinatura eletrônica (DocuSign), Histórico no SharePoint · **Automação:** Importação de seriais via Excel, Limpeza e atualização em lote |
| 12 Saneamento de Bases de Dados | **Fontes de dados:** Excel e CSV, SQL Server, PostgreSQL, MySQL, MS Access, Oracle · **Bancos e SQL:** SQL Server (T-SQL), PostgreSQL · **Processamento:** Python, pandas, Regex · **Interface:** Streamlit · **Entrega:** Base saneada, Relatório antes × depois · **Automação:** Launcher .bat |
| 13 Apuração de Tributos | **Fontes de dados:** NF-e (XML), Livros fiscais (SAP), Excel · **Bancos e SQL:** SQL Server (staging fiscal), pandas · **Processamento:** Python, pandas, Decimal · **Interface:** Streamlit · **Entrega:** Excel de apuração, Conciliação fiscal × contábil, Valor a recolher · **Automação:** Power Automate (alerta de vencimentos) |
| 14 Cálculo de ICMS | **Fontes de dados:** NF-e (XML), Tabelas de alíquotas e MVA, SAP · **Bancos e SQL:** SQL Server (tabelas de parâmetros), pandas · **Processamento:** Python, Decimal, pandas · **Interface:** Streamlit · **Entrega:** Memória de cálculo, Excel de divergências · **Automação:** Launcher .bat |
| 15 Reforma Tributária: Transição e Simulador | **Fontes de dados:** Base de faturamento e compras, Cadastro de produtos e serviços (NCM/NBS), Calendário da transição · **Bancos e SQL:** SQL Server (histórico), Power Query · **Processamento:** Python, pandas, DAX · **Interface:** Power BI, Excel · **Entrega:** Cenários e relatório de impacto |
| 16 Migração de Banco de Dados | **Fontes de dados:** SQL Server (legado), MS Access, Excel e CSV, Oracle · **Bancos e SQL:** SQL Server, Azure SQL, PostgreSQL, MySQL · **Processamento:** SQL (T-SQL), Python, SQLAlchemy, pandas · **Interface:** Console e relatório de reconciliação · **Entrega:** Relatório de reconciliação, Plano de virada e rollback · **Automação:** Agendamento de cargas |

## Também preencher
- **Foto:** `python tools/foto.py sua-foto.jpg` (recorta em quadrado) e depois `python tools/build_site.py --pdf`. Sem foto, aparecem as iniciais.
- `RESULTADOS` com números reais (antes → depois) para os demais projetos.
- Confirmar com a empresa o que pode ser divulgado.

Depois de editar `tools/data.py`, rode `python tools/build_site.py --pdf`.
