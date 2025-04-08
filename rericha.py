import json
data = {"řeřicha": "Česká Třebová"}

with open("rericha.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file)

# vytvoří soubor rericha.json a vidím, že tam josu kody pro háčky
