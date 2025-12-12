# scripts/generate_municipios.py
import csv
from pathlib import Path

Path("data/bronze").mkdir(parents=True, exist_ok=True)

rows = [
    (3550308, "são paulo", "sp", "Sudeste", 12325232, 1521.11),
    (3304557, "rio de janeiro", "rj", "Sudeste", 6775561, 1200.28),
    (1302603, "manaus", "am", "Norte", 2145442, 11401.0),
    (5300108, "brasília", "df", "Centro-Oeste", 3055149, 5801.94),
    (2927408, "salvador", "ba", "Nordeste", 2886698, 693.45),
    (4106902, "curitiba", "pr", "Sul", 1963726, 435.04),
    (1502400, "belém", "pa", "Norte", 1500102, 1068.08),
    (2611606, "recife", "pe", "Nordeste", 1653461, 218.44),
    (4314902, "porto alegre", "rs", "Sul", 1484941, 496.82),
    (3106200, "belo horizonte", "mg", "Sudeste", 2556144, 331.40)
]

with open("data/bronze/municipios.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["codigo_ibge","nome","uf","regiao","populacao","area_km2"])
    for r in rows:
        writer.writerow(r)

print("CSV criado em data/bronze/municipios.csv")
