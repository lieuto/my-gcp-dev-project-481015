SELECT
    codigo_ibge,
    nome as municipio,
    uf,
    regiao,
    populacao,
    area_km2,
FROM {{ ref('municipios_raw') }}
WHERE populacao IS NOT NULL
