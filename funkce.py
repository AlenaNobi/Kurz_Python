def greet_user():
    print ("Ahoj")
greet_user()

def greet_user(name):
    print (f"Ahoj {name} ")
greet_user("Jirko")
greet_user("Miso")

def greet_user(name):
    print (f"Ahoj {name} ")
def sum_two_numbers(a, b):
    result = a + b
    return result
greet_user("Jirko")
greet_user("Miso")
print(sum_two_numbers(3, 4))

def sum_two_numbers_and_add_5_short (a, b):
    return a + b + 5
print(sum_two_numbers_and_add_5_short (8, 2))

#Napište dvě funkce: kilometry_na_mile(kilometry) 
# a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.

def mily_na_kilometry (a):
    return a*1.609344
print(mily_na_kilometry (5) )

def kilometry_na_mily (a):
    return a/1.609344
print(kilometry_na_mily (1))

# kod fuknce z chatu od spoluucastnice
def mult(a, b):
    return a * b
print(mult(3, 4))