# využití vykaz.txt
with open("vykaz.txt", "r", encoding="utf-8") as file:
    obsah = file.readlines()

for radek in obsah:
    print(radek.strip())

print(obsah)

hodinova_mzda = int(input("Zadej hodinovou mzdu: "))
hodiny = int(radek.strip())

vyplata = 0
for radek in obsah:
    vyplata += hodinova_mzda * hodiny
    print(vyplata)

rocni_vyplata = sum(vyplata)
print(rocni_vyplata)

# využití praha.txt
with open("praha.txt", "r", encoding="utf-8") as file:
    obsah = file.readlines()



# využití auta.txt
with open("auta.txt", "r", encoding="utf-8") as file:
    obsah = file.readlines()