# 🇧🇷 **README — Pipeline ELT com dbt + BigQuery (PT-BR)**

# BigQuery ELT – Municípios do Brasil  
Pipeline ELT completo usando **dbt Core**, **BigQuery**, **Python** e **Seeds** para construção de um fluxo de dados com camadas **Bronze → Silver → Gold**.

---

## 📌 **Visão Geral do Projeto**

Este projeto demonstra um pipeline ELT moderno utilizando:

- **dbt Core 1.6**  
- **dbt-bigquery**  
- **Google Cloud BigQuery**  
- **Seeds CSV para ingestão de dados**  
- **Modelos SQL organizados por camadas (Bronze/Silver/Gold)**  

O objetivo é criar um fluxo completo de ingestão, limpeza e transformação dos dados do dataset *municípios brasileiros*.

---

## 🧱 **Arquitetura do Projeto**

```
projeto-pipeline/
│
├── data/
│   └── municipios.csv
│
├── models/
│   ├── bronze/
│   │   └── municipios_raw.sql
│   ├── silver/
│   │   └── municipios_clean.sql
│   └── gold/
│       └── municipios_metricas.sql
│
├── scripts/
│   └── generate_municipios.py
│
├── profiles.yml
├── dbt_project.yml
└── README.md
```

---

## 🗂️ **Fluxo ELT**

### **1️⃣ Bronze – Ingestão bruta**
Model: `municipios_raw.sql`

- Carrega os dados diretamente do seed.
- Não há validação ou transformação pesada.

### **2️⃣ Silver – Padronização**
Model: `municipios_clean.sql`

- Ajuste de tipos.
- Padronização de nomes.
- Normalização de strings.

### **3️⃣ Gold – Métricas e agregações**
Model: `municipios_metricas.sql`

- Cálculo de quantidades.
- Métricas resumidas por UF.

---

## 🚀 Como Executar o Projeto

### **1. Criar ambiente virtual**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### **2. Instalar dependências**
```bash
pip install dbt-bigquery==1.6.4
```

### **3. Configurar o profiles.yml**
Exemplo:
```yaml
my-gcp-dev-project:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: my-gcp-dev-project-481015
      dataset: dev_bronze
      keyfile: C:\Users\eliel\OneDrive\Área de Trabalho\projeto-pipeline\gcp-key.json
      threads: 4
      location: US
```

### **4. Rodar dbt**
```bash
dbt debug
dbt seed
dbt run
```

---

## 📊 Resultado Final no BigQuery

O pipeline cria os seguintes datasets e tabelas:

### Dataset: `dev_bronze`
- `municipios_raw`

### Dataset: `dev_silver`
- `municipios_clean`

### Dataset: `dev_gold`
- `municipios_metricas`

---

## 📈 Exemplo de Métrica (Gold)

| uf | total_municipios |
|----|------------------|
| SP | 645 |
| MG | 853 |
| RS | 497 |

---

## 🎯 Objetivo do Portfólio

Este projeto evidencia:

- Conhecimento em **engenharia de dados**  
- Uso profissional de **dbt**  
- Organização de projeto ELT moderno  
- Deploy em **Google BigQuery**  
- Boas práticas de versionamento Git  

Ideal para vagas de **Engenheiro de Dados Júnior / Estagiário / Analista de Dados**.

---
---

# 🇺🇸 **README — BigQuery ELT Pipeline (EN-US)**

# BigQuery ELT – Brazilian Municipalities  
A complete ELT pipeline using **dbt Core**, **BigQuery**, **Python**, and **Seeds** to build a multi-layer data flow (**Bronze → Silver → Gold**).

---

## 📌 **Project Overview**

This project demonstrates a modern ELT pipeline using:

- **dbt Core 1.6**  
- **dbt-bigquery**  
- **Google Cloud BigQuery**  
- **CSV seed ingestion**  
- **Layered SQL models (Bronze/Silver/Gold)**  

The goal is to build a fully reproducible transformation flow for Brazil's municipalities dataset.

---

## 🧱 **Project Architecture**

```
project-pipeline/
│
├── data/
│   └── municipios.csv
│
├── models/
│   ├── bronze/
│   │   └── municipios_raw.sql
│   ├── silver/
│   │   └── municipios_clean.sql
│   └── gold/
│       └── municipios_metricas.sql
│
├── scripts/
│   └── generate_municipios.py
│
├── profiles.yml
├── dbt_project.yml
└── README.md
```

---

## 🗂️ **ELT Layers**

### **1️⃣ Bronze – Raw ingestion**
Loads data directly from the seed file.

### **2️⃣ Silver – Standardization**
Applies type corrections, name normalization, and structural fixes.

### **3️⃣ Gold – Metrics**
Aggregates and calculates business-ready metrics.

---

## 🚀 How to Run

### **1. Create virtual environment**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### **2. Install dependencies**
```bash
pip install dbt-bigquery==1.6.4
```

### **3. Configure profiles.yml**
```yaml
my-gcp-dev-project:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: my-gcp-dev-project-481015
      dataset: dev_bronze
      keyfile: C:\Users\eliel\OneDrive\Área de Trabalho\projeto-pipeline\gcp-key.json
      threads: 4
      location: US
```

### **4. Run dbt**
```bash
dbt debug
dbt seed
dbt run
```

---

## 📊 Final Outputs in BigQuery

### Dataset: `dev_bronze`
- `municipios_raw`

### Dataset: `dev_silver`
- `municipios_clean`

### Dataset: `dev_gold`
- `municipios_metricas`

---

## 📈 Example Metric Output (Gold)

| state | total_municipalities |
|-------|-----------------------|
| SP    | 645 |
| MG    | 853 |
| RS    | 497 |

---

## 🎯 Portfolio Purpose

This project highlights skills in:

- Modern **data engineering**
- Professional use of **dbt**
- ELT architecture with layered transformations
- Deployment into **Google BigQuery**
- Git best practices

Perfect for **Junior Data Engineer / Data Analyst / ETL Developer** roles.

---

# 📄 Need a PDF version?
I can generate a **beautifully formatted PDF** of this README upon request.

