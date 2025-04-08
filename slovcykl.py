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


books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total_sales = 0
for item in books:
    if item["year"] == 2019:
        total_sales = total_sales + item["sold"] *  item["price"]
print(total_sales)

