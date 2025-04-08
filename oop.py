class Employee: 
    def __init__(self, name, position, holiday_entlitlement):
        # name -> parametr metody, zanikne po opuštění metody
        # self.name -> atribut objektu, je svázán s objektem, hodnota zůstane, dokud objekt nezanikne
        # POtřebuji uložit hodnotu z parametru name do atributu name
        # atribut name = parametr name
        self.name = name 
        self.position = position
        self.holiday_entlitlement = holiday_entlitlement
    def get_info(self):
        #__str__(self):    toto je jiná možnost místo get info (převod na str)
        return f"{self.name} pracuje na pozici {self.position}."
    def take_holiday(self, days): 
        if days >= self.holiday_entlitlement:
           self.holiday_entlitlement = self.holiday_entlitlement - days
           return "Užij si to"
        else: 
           return "Na tolik dní nemáš nárok"

frantisek_novak = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Novák", "konstruktérka", 35)
klara.take_holiday(5)
klara.take_holiday(15)
print(klara.holiday_entlitlement)

print(klara.get_info()) 
# print(klara) -> toto stačí použít u toho druhého __str__
print(frantisek_novak.get_info())


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
klara = Employee("Klára Nová", "konstruktérka", 35)
print(klara.take_holiday(25))
print(klara.take_holiday(15))
print(klara.holiday_entlitlement)

