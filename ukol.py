# Zadání úkolu 1
# Aplikace pro zjednodušený výpočet daně z nemovitosti

import math
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__(self, locality):
        self.locality = locality
    
    @abstractmethod
    def __str__():
        pass

    @abstractmethod
    def calculate_tax():
        pass

class Estate(Property): 
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area 

    def __str__(self):
        return f"Typ pozemnku je {self.estate_type}, lokalita {self.locality.name} ({self.locality.locality_coefficient}), {self.area} metrů čtverečních, {self.calculate_tax}."

    @property
    def calculate_tax(self):
        if self.estate_type == "land":
            tax = math.ceil(self.area*0.85*self.locality.locality_coefficient) 
            return f"daň {tax}"
        elif self.estate_type == "building_site":
            tax = math.ceil(self.area*9*self.locality.locality_coefficient) 
            return f"daň {tax}"
        elif self.estate_type == "forrest":
            tax = math.ceil(self.area*0.35*self.locality.locality_coefficient) 
            return f"daň {tax}"
        elif self.estate_type == "garden":
            tax = math.ceil(self.area*2*self.locality.locality_coefficient) 
            return f"daň {tax}"

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def __str__(self):
        return f"Typ pozemku je {self.estate_type}, lokalita {self.locality.name} ({self.locality.locality_coefficient}), {self.area} metrů čtverečních, {self.calculate_tax}."

    @property
    def calculate_tax(self):
        for item in list:
            tax = (self.area*self.locality.locality_coefficient*15)
            if hasattr(item, "commercial") and self.commercial == "commercial":
             tax = tax*2
        return f"daň {tax}"

           
#příklad výpočtu
locality2 = Locality('locality2', 2)
les1 = Estate(locality2, 'forrest', 500)
print(les1.calculate_tax)

#příklad výpočtu
locality3 = Locality('locality_3', 3)
byt1 = Residence(locality3, 60, "commercial")
list = []
list.append(byt1)
#list = [byt1]
print(byt1.calculate_tax)

#Vyzkoušej svůj program pomocí následujících nemovitostí: 
manetin = Locality('Manětín', 0.8)
zemedelsky_pozemek = Estate(manetin, 'land', 900)
print(zemedelsky_pozemek.calculate_tax)

dum1 = Residence(manetin, 120, "none")
list.append(dum1)
print(dum1.calculate_tax)

brno = Locality('Brno', 3)
kancelar1 = Residence(brno, 90, "commercial")
list.append(kancelar1)
print(kancelar1.calculate_tax)

print(les1)
print(zemedelsky_pozemek)
