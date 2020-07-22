#rok = int(input("Wprowadź rok: "))
#
# tutaj wpisz swój kod
#
rok = 1580
if rok <=1580:
    komunikat = "Nie w kalendarzy gregoriańskim"
elif rok % 4 != 0:
    komunikat = "Zwykły rok"
elif rok % 100 != 0:
    komunikat = "Rok przestępny"
elif rok % 400 != 0:
    komunikat = "Zwykły rok"
else:
    komunikat = "Rok przestępny"
    
print(komunikat)