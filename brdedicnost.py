# Dedicnost první příklad Cenný balík a druhý Cena přepravy + delivery_price()
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
    def delivery_price(self): 
        cost = 0
        if self.weight <= 2:
            cost = 150
        elif self.weight <= 5:
            cost = 190
        else:
            cost = 220
        return cost
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        
        self.state = "doručen"
        return "Doručení uloženo"
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
       super().__init__(address, weight, state)
       self.value = value
    def __str__(self):
        return super().__str__() + f" Má cenu {self.value}."
    # od koučky řešení
    #def delivery_price(self): 
        #return super().delivery_price() + self.value * 0.05
    def get_costs(self):
        price = super().get_costs()
        return price * 1.05
        return super().__str__() + f" Přeprava je {price}."
    # toto jsem si zkoušela sama (ale bez celého přikladu)
       # delivery.price = self.value + (self.value*0.05)
       # return super().__str__() + f" Cena přepravy je {self.price}."
 
    
balik1 = Package("Moravec 125", 8, "doručen")
balik2 = ValuablePackage("Moravec 249", 5.1, "nedoručen", 2500)

print(balik1)
print(balik2)
