class Employee:
    def __init__(self, name, position, holiday_entlitlement):
        self.name = name
        self.position = position
        self.holiday_entlitlement = holiday_entlitlement
    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."
    def take_holiday(self, days):
        if days <= self.holiday_entlitlement:
            self.holiday_entlitlement = self.holiday_entlitlement - days
            return "Užij si to"
        else:
            return "Na tolik dní nemáš nárok."
class Manager(Employee):
    def __init__(self, name, position, holiday_entlitlement, subordinates):
        super().__init__(name, position, holiday_entlitlement)
        self.subordinates = subordinates
class TopManager(Manager):
    def __init__(self, name, position, holiday_entlitlement, subordinates, car):
        super().__init__(name, position, holiday_entlitlement, subordinates)
        self.car = car
    def take_holiday(self, days):
        return "Uzij si to"
# tady jsem změnila odkaz na Emploee čerpání dovolené a nadefinovala přimo pro top managera
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízené."
# tady jsem doplnila funkci str pro topmanagera
frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nová", "konstruktérka", 35)
marian = TopManager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Peugeot 403")
print(marian)




