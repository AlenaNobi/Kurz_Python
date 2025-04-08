from datetime import datetime, timedelta
apollo_start = datetime(1969, 7, 16, 14, 32)
america = apollo_start.strftime("%m/%d/%Y")        
print(america) 


start_Orbiter = datetime(2020, 2, 10, 5, 3)
print(start_Orbiter.isoweekday()) 

aktualni = datetime.now()

doba = aktualni - start_Orbiter
print(doba)


objednani = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

objednavka = objednani + prevzeti + priprava + doprava
print(objednavka)




