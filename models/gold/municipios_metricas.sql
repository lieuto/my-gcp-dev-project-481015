{{ config(materialized='table') }}

SELECT
  uf,
  regiao,
  COUNT(*) AS qtd_municipios,
  SUM(populacao) AS populacao_total,
  AVG(densidade) AS densidade_media
FROM {{ ref('municipios_clean') }}
GROUP BY 1, 2
ORDER BY uf;
