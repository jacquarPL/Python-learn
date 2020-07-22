def czy_przestepny(rok):
    if (rok%4==0 and rok%100!=0) or rok%400==0:
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    ile_dni = [31,28,31,30,31,30,31,31,30,31,30,31]
    if czy_przestepny(rok) and miesiac == 2:
        return 29
    else:
        return ile_dni[miesiac-1]
#
# twój kod z LABORATORIUM 4.1.3.7
#

def dzien_w_roku(rok, miesiac, dzien):
    dni_roku = 0
    for m in range(1,miesiac):
        #print(m, dni_w_miesiacu(rok,m))
        dni_roku += dni_w_miesiacu(rok,m)
    dni_roku += dzien
    return dni_roku
#
# wstaw nowy kod tutaj
#

print(dzien_w_roku(2000, 12, 31))