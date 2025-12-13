WITH base AS (
    SELECT
        CAST(codigo_ibge AS INT64) AS codigo_ibge,
        nome,
        uf,
        regiao,
        CAST(populacao AS INT64) AS populacao,
        CAST(area_km2 AS FLOAT64) AS area_km2
    FROM {{ ref('municipios') }}
),

municipios_por_uf AS (
    SELECT
        uf,
        COUNT(*) AS total_municipios_uf
    FROM base
    GROUP BY uf
)

SELECT
    b.*,
    m.total_municipios_uf
FROM base b
LEFT JOIN municipios_por_uf m
    ON b.uf = m.uf
