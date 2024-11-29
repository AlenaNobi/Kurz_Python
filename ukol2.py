import requests

# část 1
ico = input("Zadej ICO: ")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
response_json = response.json()

print(response_json["obchodniJmeno"])
print(response_json["sidlo"]["textovaAdresa"])

# část 2 moneta 
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "moneta"}'
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
response_json = response.json()

# vypíše jednu položku ze seznamu podle indexu
print(response_json["ekonomickeSubjekty"][0]["obchodniJmeno"])
print(response_json["ekonomickeSubjekty"][0]["ico"])

# vypíše všechny nalezené subjekty 
print("Nalezeno subjektů:", response_json["pocetCelkem"])
for subjekt in response_json["ekonomickeSubjekty"]:
    print(subjekt["obchodniJmeno"], ", ", subjekt["ico"])

# část 2 input
jmeno = input("Zadej obchodní jméno: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{jmeno}"}}'
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
response_json = response.json()

print("Nalezeno subjektů:", response_json["pocetCelkem"])
for subjekt in response_json["ekonomickeSubjekty"]:
    print(subjekt["obchodniJmeno"], ", ", subjekt["ico"])


