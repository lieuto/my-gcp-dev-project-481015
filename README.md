# Projeto de Engenharia de Dados — BigQuery + dbt  
Arquitetura: Bronze → Silver → Gold  

Este repositório contém um projeto completo de engenharia de dados utilizando **dbt (Data Build Tool)** como motor de transformação, e **Google BigQuery** como Data Warehouse.  
O foco do projeto é demonstrar boas práticas de modelagem, versionamento e governança de dados usando o padrão **Medallion Architecture** (Bronze / Silver / Gold).

---

## 🔥 Principais Tecnologias

- **Google BigQuery** (Data Warehouse)
- **dbt (Data Build Tool)** — versão compatível com BigQuery
- **Arquitetura Bronze → Silver → Gold**
- **Git / GitHub**
- **VS Code**
- **Python (opcional)**

---

## 🧱 Arquitetura do Projeto

Este projeto segue o modelo de camadas:

### 🟫 **Bronze — Dados brutos**
- Dados ingeridos diretamente da fonte (CSV, API ou tabela externa).
- Sem transformação.
- Representa o dado como ele é.

### 🥈 **Silver — Dados limpos e padronizados**
- Padronização de nomes, tipos e formatação.
- Correção de nulos, conversões e validações.
- Tabelas prontas para serem consumidas pelo negócio.

### 🥇 **Gold — Métricas e agregações**
- Tabelas finais analíticas.
- Indicadores, métricas e agregações.
- Pronto para dashboards (ex: Power BI, Looker, Data Studio).

---

## 📁 Estrutura de Diretórios
projeto-pipeline/
├── models/
│ ├── bronze/
│ │ └── municipios_raw.sql
│ ├── silver/
│ │ └── municipios_clean.sql
│ └── gold/
│ └── municipios_metricas.sql
├── dbt_project.yml
├── README.md
└── .gitignore
