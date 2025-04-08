import requests

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