SELECT
    uf,
    regiao,
    COUNT(codigo_ibge) AS municipios_no_estado,
    MAX(total_municipios_uf) AS total_municipios_uf,
    SUM(populacao) AS populacao_total,
    AVG(populacao) AS populacao_media
FROM {{ ref('municipios_clean') }}
GROUP BY uf, regiao
