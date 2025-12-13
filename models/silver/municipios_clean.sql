SELECT
    codigo_ibge,
    nome AS municipio,
    uf,
    regiao,
    populacao,
    area_km2,
    total_municipios_uf
FROM {{ ref('municipios_raw') }}
WHERE populacao IS NOT NULL
