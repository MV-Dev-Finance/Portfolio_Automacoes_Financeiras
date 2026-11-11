# Saneamento de Bases de Dados

> Diagnóstico e correção automática de qualidade de dados antes da carga.

**Tipo de tela:** Antes × depois

![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white) ![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

[Ver esta página no site](https://mv-dev-finance.github.io/Portfolio_Automacoes_Financeiras/projects/saneamento-bases-dados.html) · [Voltar ao portfólio](../../README.md)

## 1. Lógica do negócio

Decisões e conciliações são tão boas quanto a qualidade da base. Dados com duplicidades, campos vazios, formatos misturados ou contas sem de/para quebram cargas, cruzamentos e relatórios.

**Regras que governam o processo**

- Chave única por registro
- Campos obrigatórios preenchidos
- Datas e valores em formato padronizado
- Todas as contas com de/para

> **O problema:** Bases de várias fontes chegavam sujas e o retrabalho de limpeza se repetia a cada ciclo.

## 2. Como resolvi com dados

1. **Perfilamento**: Meço duplicados, nulos, formatos e contas sem de/para.
2. **Regras**: Defino regras por campo e por tipo de problema.
3. **Correção segura**: Corrijo automaticamente o que é seguro corrigir.
4. **Pendências**: Listo o que precisa de decisão humana.
5. **Prova**: Relatório de problemas antes × depois.

## 3. Tecnologias utilizadas

```mermaid
flowchart LR
    fontes["Fontes de dados<br/>Excel e CSV<br/>SQL Server<br/>PostgreSQL"]
    dados["Bancos e SQL<br/>SQL Server T-SQL<br/>PostgreSQL"]
    proc["Processamento<br/>Python<br/>pandas<br/>Regex"]
    ui["Interface<br/>Streamlit"]
    saida["Entrega<br/>Base saneada<br/>Relatório antes × depois"]
    auto["Automação<br/>Launcher .bat"]
    fontes --> dados --> proc --> ui --> saida --> auto
```

| Camada | Tecnologias |
|---|---|
| Fontes de dados | Excel e CSV, SQL Server, PostgreSQL, MySQL, MS Access, Oracle |
| Bancos e SQL | SQL Server (T-SQL), PostgreSQL |
| Processamento | Python, pandas, Regex |
| Interface | Streamlit |
| Entrega | Base saneada, Relatório antes × depois |
| Automação | Launcher .bat |

## 4. Funcionalidades

- Remoção de duplicados por chave
- Padronização de datas e valores
- De/para de contas
- Relatório antes × depois

## IA aplicada neste projeto

Geração de bases sujas sintéticas para testar cada regra de limpeza.

## Telas

**Antes × depois**

![Antes × depois](../../assets/screens/saneamento-bases-dados__antes-depois.jpg)

## Quem fez

**Miguel Vinicius Moura Martins**: Defini a regra de negócio, modelei os dados, validei os números contra o processo manual e desenvolvi a ferramenta com apoio de IA.

> Todas as telas usam dados sintéticos de uma empresa fictícia.
