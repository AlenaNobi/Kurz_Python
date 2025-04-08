# Otevře soubor ve čtecím režimu
with open("mereni.txt", "r", encoding="utf-8") as file:
    obsah = file.readlines()  # Načte řádky do seznamu
    # nebo obsah = file.read()  # Pokud chcete načíst celý text jako jeden řetězec

# Vypíše načtený obsah
for radek in obsah:
    print(radek.strip())  # strip() odstraní nové řádky


print(obsah)

import statistics  # Importujeme modul statistics, který nám umožní snadno spočítat průměr.

teploty = []  # Seznam, do kterého budeme ukládat hodnoty teplot.

# Otevřeme soubor mereni.txt pro čtení
with open('mereni.txt', 'r') as file:
    for radek in file:
        # Rozdělíme každý řádek podle mezer nebo tabulátorů
        casti = radek.split()

        # Zkontrolujeme, zda poslední část je číslo, než ji přidáme do seznamu teplot
        if len(casti) > 1 and casti[-1].replace('.', '', 1).isdigit():  # Kontrola, zda je poslední část číslo (včetně možnosti desetinné tečky)
            teplota = float(casti[-1])  # Převedeme na číslo typu float
            teploty.append(teplota)  # Přidáme teplotu do seznamu

# Zkontrolujeme, zda máme nějaké teploty k výpočtu průměru
if teploty:
    prumerna_teplota = statistics.mean(teploty)  # Vypočítáme průměrnou teplotu pomocí statistics.mean()
    print(f"Průměrná teplota za týden je: {prumerna_teplota:.2f} °C")
else:
    print("Žádná data pro výpočet průměrné teploty.")