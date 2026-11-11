# Lançamento de Docas

> Da planilha base ao arquivo de lançamento contábil validado.

**Tipo de tela:** Wizard + log

![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

[Ver esta página no site](https://mv-dev-finance.github.io/Portfolio_Automacoes_Financeiras/projects/lancamento-docas.html) · [Voltar ao portfólio](../../README.md)

## 1. Lógica do negócio

Alguns lançamentos recorrentes partem de uma planilha de apuração e precisam virar um arquivo de lançamento para o ERP. Todo lote precisa ter débito igual a crédito, contas e centros de custo válidos e competência correta.

**Regras que governam o processo**

- Débito = crédito em todo lote
- Conta e centro de custo precisam existir no plano de contas
- A data precisa estar dentro da competência

> **O problema:** Montar o lançamento manualmente aumentava o risco de erro de conta, centro de custo e lote desbalanceado.

## 2. Como resolvi com dados

1. **Leitura**: Carrego a planilha base.
2. **Validação**: Aplico regras de conta, centro de custo, valor e competência.
3. **Erros**: Listo cada erro com a linha e a ação sugerida.
4. **Geração**: Monto o arquivo de lançamento no layout do ERP.
5. **Conferência**: Confirmo débito = crédito antes de entregar.

## 3. Tecnologias utilizadas

```mermaid
flowchart LR
    fontes["Fontes de dados<br/>Planilha base Excel<br/>Plano de contas"]
    dados["Bancos e SQL<br/>pandas"]
    proc["Processamento<br/>Python<br/>pandas<br/>openpyxl"]
    ui["Interface<br/>Streamlit"]
    saida["Entrega<br/>Arquivo de lançamento .xlsx"]
    auto["Automação<br/>Launcher .bat"]
    fontes --> dados --> proc --> ui --> saida --> auto
```

| Camada | Tecnologias |
|---|---|
| Fontes de dados | Planilha base (Excel), Plano de contas |
| Bancos e SQL | pandas |
| Processamento | Python, pandas, openpyxl |
| Interface | Streamlit |
| Entrega | Arquivo de lançamento (.xlsx) |
| Automação | Launcher .bat |

## 4. Funcionalidades

- Validação por regra, linha a linha
- Log com avisos e erros
- Conferência automática de débito e crédito
- Arquivo pronto para carga

## IA aplicada neste projeto

Cenários de lote desbalanceado, conta inexistente e data fora da competência.

## Telas

**Processamento**

![Processamento](../../assets/screens/lancamento-docas__terminal.jpg)

## Quem fez

**Miguel Vinicius Moura Martins**: Defini a regra de negócio, modelei os dados, validei os números contra o processo manual e desenvolvi a ferramenta com apoio de IA.

> Todas as telas usam dados sintéticos de uma empresa fictícia.
