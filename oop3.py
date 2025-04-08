class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."

class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
frantisek = Employee("František Novák", "konstruktér", 25) 
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")

# isinstance vrací TRUE nebo FALSE nic jiného - ptáme se zda marian pochází ze třídy Manager?
if isinstance(marian, Manager): 
    print("Objekt pochází ze třídy Manager.")
else: 
    print("Objekt nepochází ze třídy Manager.")

# tady to bere jakože taky TRUE, protože je to rodič (tj sice je Manager ale pochází dědí od Employee)
if isinstance(marian, Employee): 
    print("Objekt pochází ze třídy Employee.")
else: 
    print("Objekt nepochází ze třídy Employee.")

# frantisek je Employee, tj tady je TRUE přesná shoda 
# varianta Manager u frantiska - tady už je to FALSE (print else)
if isinstance(frantisek, Manager): 
    print("Objekt pochází ze třídy Manager.")
else: 
    print("Objekt nepochází ze třídy Manager.")

# nyní pokračujeme dál - tvorba employee listu 
# - tj si udělám seznam, určím počáteční hodnotu nula a pak proběhne cyklus for (3x)
# a výsledek je 2 manageri
employe_list = [marian, marketa, frantisek, jakub]
expected_people = 0
for item in employe_list:
    if isinstance(item, Manager):
        print(f"Posílám pozvánku pro: {item.name}")
        expected_people = expected_people + 1
print(expected_people)


# funkce hasattr - kontroluje zda má nějaký objekt daný atribut nebo metodu
# trorba nové třídy Salesman a nový objekt Jakub
# tento cyklus projde celý empl list a vypíše true (car) nebo false (nic)
for item in employe_list:
    if hasattr(item, "car"):
        print(item.car)
# druhá varianta - uložím car do proměnné (ale vzdy tam musí být ten řetězec "")
attr_name = "car"
for item in employe_list:
    if hasattr(item, attr_name):
        print(item.car)

# funkce getattr - pokud tam hodnota je, tak to vypíše, nebo to druhé - nekončí hned chybou
hodnota_atributu = getattr(marketa, "car", "nemá auto")
print(hodnota_atributu)

hodnota_atributu = getattr(frantisek, "car", "nemá auto")
print(hodnota_atributu)

nazev_atributu = input("Zadej název atributu: ")
hodnota_atributu = getattr(marketa, nazev_atributu, "u atributu není žádná hodnota")
print(hodnota_atributu)

