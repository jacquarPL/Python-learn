#dochód = float(input("Wprowadź roczny dochód: "))
#
# tutaj wpisz swój kod
#
dochód = 100000
if dochód <= 85528:
    podatek = dochód * 0.18 - 556.02
else:
    podatek = 14839.02 + (dochód - 85528) * 0.32
podatek = round(podatek, 0)
if podatek < 0:
    podatek = 0
print("Podatek wynosi:", podatek)