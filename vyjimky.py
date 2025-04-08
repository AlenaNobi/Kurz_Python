def is_odd(number):
    # 2 % 2 -> 1 -> vrátí False
    # 4 % 2 -> 1 -> vrátí False
    # 5 % 2 -> 0 -> vrátí True
    return number % 2 == 1
# 3 je liché číslo, funkce má vrátit True
assert is_odd(3) == True


vek = input("Zadej věk: ")
# Zkontroluju, zda jsou v řetězci jen číslice
# Pokud tam nejsou jen čísla, program ukončím
if not vek.isdigit():
    print("Věk musí být číslo")
    exit()
vek = int(vek)


