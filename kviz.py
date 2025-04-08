venecky = [1, 2, 4, 1, 6, 0, 1] 
print(venecky[1])

print(venecky[:3])

venecky[5] = 5
print(venecky)

print(venecky[1])

inzerat = "TechStream v proměnné inzerat"
inzeratnovy = inzerat.replace("TechStream", "NextGen Innovations")
print(inzeratnovy)

jen_cisla = "10"

if jen_cisla.isdecimal() :
    print("Spravne")

mesta = "Praha, Plzeň, Brno, Ostrava, Liberec"
mesta2 = mesta.split(", ")
print(mesta2)

filmy = ["Čtyři svatby a jeden Python", 
         "Pán Pythonů: Návrat Soustruha", 
         "Rychle a Python", 
         "Harry Potter a Kámen Pythonů", 
         "Forrest a Python"]
cislo_filmu = int(input("Zadej číslo filmu: "))
if cislo_filmu < len(filmy) :
     print(filmy[cislo_filmu])
else :
     print("Tolik filmů nemáme")
