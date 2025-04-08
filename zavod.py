import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
print(runners[0])  

print(runners[0]["casy"]["oficialni"])

finishers = []
for runner in runners:     
    if runner["casy"]["oficialni"] != "DNF":
        finishers.append([runner["jmeno"], runner["casy"]["oficialni"]])

print(finishers[1])

