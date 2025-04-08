import math
import statistics

# zaokrohlovani nahoru
vysledek = math.ceil(3.1)
#zaokrohlovani dolu
vysledek = math.floor(3.1)
print(vysledek)

prumer = statistics.mean([2, 3, 4, 5])
print(prumer)

# od holek sam prace
cislo = float(input("Zadej libovolné desetinné číslo: "))
print(math.ceil(cislo))
print(math.floor(cislo))
print(round(cislo))

desetinne_cislo = float(input("Zadej desetinné číslo: "))
print(math.ceil(desetinne_cislo))
print(math.floor(desetinne_cislo))
print(round(desetinne_cislo))

import math
cislo = float(input("napiš desetiné číslo:"))
nahoru = math.ceil(cislo)
print(nahoru)
dolu = math.floor(cislo)
print(dolu)
print(round(cislo))
 
# bonusovy ukol od Jirky Pesika
import statistics
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

znamky = []
dulezite_predmety = ["Český jazyk", "Matematika", "Anglický jazyk", "Fyzika"]
for row in school_report:
    if row[0] in dulezite_predmety:
        znamky.append(row[1])
print(znamky)
prumer = statistics.mean(znamky)
print(prumer)
# row je mnou zvolený název (náhodný)

znamky = []
dulezite_predmety = ["Český jazyk", "Matematika", "Anglický jazyk", "Fyzika"]
for row in school_report:
    # Při prvním běhu
    # row = ["Český jazyk", 1]
    # Chci uložit pouze předměty v seznamu dulezite_predmety
    # Podívej se, jestli je předmět (row[0]) v seznamu dulezite_predmety
    if row[0] in dulezite_predmety:
        # row[0] = "Český jazyk"
        # row[1] = 1
        znamky.append(row[1])
print(znamky)

znamky = []
dulezite_predmety = ["Český jazyk", "Matematika", "Anglický jazyk", "Fyzika"]
for row in school_report:
    # Při čtvrtém běhu
    # row = ["Přírodopis", 2]
    # Chci uložit pouze předměty v seznamu dulezite_predmety
    # Podívej se, jestli je předmět (row[0]) v seznamu dulezite_predmety
    if row[0] in dulezite_predmety:
        # Sem se program vůbec nedostane
        znamky.append(row[1])
print(znamky)
prumer = statistics.mean(znamky)
print(prumer)

