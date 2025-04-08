import json
with open("absolventi.json", encoding="utf-8") as file:
    absolventi = json.load(file)
#print(absolventi)
print(absolventi[0])

petr = absolventi[0]
print(petr["dochazka"])

#import do jsonu -- vytvoří mi to v seznamu hodiny.json
import json
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open("hodiny.json", mode="w", encoding="utf-8") as file:
    json.dump(hours, file)

import json

absolvents = []
with open("absolventi2.jsonl", encoding="utf-8") as file:
    for line in file:
        # Při prvním běhu cyklu
        # line = {"name": "Gilbert", "session": "2013", "score": 24, "completed": true}
        # Ale line je str (řetězec)
        # current_absolvent je slovník
        # funkce loads převede řetězec na slovník
        current_absolvent = json.loads(line)
        absolvents.append(current_absolvent)
gilbert = absolvents[0]
print(gilbert["score"])

# https://jsonlines.org/examples/

