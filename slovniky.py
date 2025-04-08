item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
print(item["title"])
#funguje od verze 3.12 - starší verze musí mít u title jen jedny uvozovky 'title'
print(f"Název předmětu je {item["title"]}")
item["weight"] = 0.8
# má item klíč weight?
if "weight" in item:
    print(item["weight"])
else: 
    print ("Hmotnost není udána")

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Název předmětu je Čajová konvička s hrnky
# Funguje ve verzi 3.12
print(f"Název předmětu je {item["title"]}")
# Funguje od verze 3.6
print(f"Název předmětu je {item['title']}")
item["weight"] = 0.8
key = "price"
item[key] = 929
# Má item klíč weight?
if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není udána")

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total_sales = 0
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} kusů.")
    total_sales = total_sales + value
    # total_sales += value
print(f"Celkem bylo prodáno {total_sales} kusů.")