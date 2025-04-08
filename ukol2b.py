import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "moneta"}'
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
response_json = response.json()

# toto mi vypíše jednu položku ze seznamu podle indexu
#print(response_json["ekonomickeSubjekty"][0]["obchodniJmeno"])
#print(response_json["ekonomickeSubjekty"][0]["ico"])

print("Nalezeno subjektů:", response_json["pocetCelkem"])
for subjekt in response_json["ekonomickeSubjekty"]:
    print(subjekt["obchodniJmeno"], ", ", subjekt["ico"])


