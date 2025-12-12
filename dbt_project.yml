name: 'projeto_pipeline'
version: '1.0'
config-version: 2

profile: 'projeto_pipeline'

model-paths: ["models"]

models:
  projeto_pipeline:
    bronze:
      +schema: dev_bronze
      +materialized: table

    silver:
      +schema: dev_silver
      +materialized: table

    gold:
      +schema: dev_gold
      +materialized: table
