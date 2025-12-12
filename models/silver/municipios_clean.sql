{{ config(materialized='table') }}

SELECT
  codigo_ibge,
  INITCAP(nome) AS nome,
  UPPER(uf) AS uf,
  regiao,
  populacao,
  area_km2,
  SAFE_DIVIDE(populacao, area_km2) AS densidade
FROM {{ ref('municipios_raw') }}
