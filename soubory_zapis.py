text = "Tento text bude zapsán do souboru."

with open('soubor.txt', mode='w', encoding='utf-8') as soubor:
    print(text, file=soubor)

#toto mi vytvoří nový soubor.txt tady ve VS a s uvedeným textem


names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as uzivatele:
    for name in names:
        print(name, file=uzivatele)