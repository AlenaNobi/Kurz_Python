class Employee:
    def __init__(self, name, position, holiday_entitlement, manager):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.manager = manager
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. Nadřízeným je {self.manager.name}."
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, manager, subordinates, car):
        super().__init__(name, position, holiday_entitlement, manager)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, None, 2, "Škoda Octavia")
klara = Employee("Klára Nová", "konstruktérka", 25, marian)
# chci zjistit jmné manažera Kláry - pomocí teček postupně se doberu k tomu, co chci zjistit
# druhý print nás zavede k tomu stejnému - jméno Mariana, ale vím, že chci mariana
print(klara.manager.name)
print(marian.name)
print(klara)
