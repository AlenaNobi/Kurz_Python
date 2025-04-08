from datetime import datetime, timedelta

#toto mi vypíše vždy aktuální čas
print(datetime.now())

dnesni_poledne = datetime(2024, 11, 7, 12, 00)
#dnesni_poledne = datetime(2024, 11, 7)   - toto mi vypíše půlnoc: 2024-11-07 00:00:00
print(dnesni_poledne)

aktualni = datetime.now()
print(aktualni)


apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
print(apollo_start.isoweekday()) # den v týdnu, počítáno od 0
print(apollo_start.isoformat()) # formát času s písmenem T


print(aktualni.strftime("%d. %m. %Y , %H:%M"))

print(aktualni.strftime("%d. %b. %Y , %H:%M")) # vypsalo v jiném jazyce, u mě AJ

apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
print(apollo_pristani)

apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
print(apollo_pristani)

delka_mise = apollo_pristani - apollo_start
print(delka_mise)

planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10)
skutecny_prijezd = planovany_prijezd + zpozdeni

zpozdeni = timedelta(minutes=10, seconds=25)
skutecny_prijezd = planovany_prijezd + zpozdeni
