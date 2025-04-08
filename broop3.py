class Package:
    def __init__(self, address, weight, state, driver):
        self.address = address
        self.weight = weight
        self.state = state
        self.drive = driver

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, state, driver, value):
        super().__init__(address, weight, state, driver)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
    
class Driver:
    def __init__(self, name, phone_number, ):
        self.name = name
        self.phone_number = phone_number

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

total_value = 0
for item in package_list:
    # Zkontroluju, zda je o ValuablePackage
    if isinstance(item, ValuablePackage):
        total_value = total_value + item.value
    # Zkontroluju, zda item má atribut value
    if hasattr(item, "value"):
        total_value = total_value + item.value
    # Pokud není hodnota balíku není, přičtu 0
    total_value = total_value + getattr(item, "value", 0)
print(total_value)

# je tady chyba v zadání z kodim.cz tj od toho total value dobrý ale znovu vzít ten balík
# ještě je to třeba doplnit (převzít potom z githubu)

