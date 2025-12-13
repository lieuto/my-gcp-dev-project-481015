import requests
import csv

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

response = requests.get(URL)
response.raise_for_status()
municipios = response.json()

with open("seeds/municipios_ibge.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "codigo_ibge",
        "nome",
        "uf",
        "regiao"
    ])

    for m in municipios:
        try:
            uf = m["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
            regiao = m["regiao-imediata"]["regiao-intermediaria"]["UF"]["regiao"]["nome"]

            writer.writerow([
                m["id"],
                m["nome"],
                uf,
                regiao
            ])
        except KeyError:
            # Se algum registro vier incompleto (raro), apenas ignora
            continue

print("✅ CSV oficial de municípios IBGE gerado com sucesso!")
print(f"Total de municípios: {len(municipios)}")
