print  ("Hello world!")
jmena = ["Michal", "Jana", "Martina"]
teploty = [23.3, 21.2, 10, 14, 2, 3]
kniha = ["Kniha 1", 300, 500, True, True]

print(jmena[1])
print(teploty[3:6])
print(teploty[2:])
print(teploty[:3])
print(len(kniha))
print(len("SuperTajneHeslo123"))


inzerat = "Na této pracovní pozici budete využívat Python a SQL"

if "SQL" in inzerat:
    print("SQL se v inzeratu nachazi")
else:
    print("SQL se v inzeratu nenachazi")


email = "michal.kuceraczechitas.cz"

if "@" not in email:
    print("spatny email")
else:
    print("spravny e-mail")


cisla = [1, 2, 3, 1, 2, 132, 123, 43, 55, 12, 2, 3, 4, 5, 12, 1435, 93]

print(min(cisla))
print(max(cisla))
print(sorted(cisla))
print(sum(cisla))


pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(min(pohyby))
print(max(pohyby))
print(sum(pohyby))


produkt = input("Zadej produkt: ")
produkt = produkt.lower() # VINO na vino

if produkt == "vino":
    print("vitej v kategorii vina")
elif produkt == "pivo":
    print("vitej v kategorii piva")
else:
    print("spatne zvolena hodnota")


print("michal".upper())
print("JANA".lower())
print("$$$text$$$".strip("$").upper())
print("jana martina michal pavel".split(" "))
print("jana,martina,michal,pavel".split(","))

jmena = "jana,martina,michal,pavel".split(",")

print("$".join(jmena))
print(",".join(jmena))

text = "Jirka Pesik je nejhorsi lektor Pythonu"
new_text = text.replace("nejhorsi", "nejlepsi")

print(new_text)

jmeno = "Alena"
print(jmeno.lower())
print(jmeno.upper())


hodnoty = ['12', '1', '7', '-11']

cislo = [2]

a = "12"
print(float(a))

