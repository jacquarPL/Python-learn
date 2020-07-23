def czy_przestepny(rok):
    if (rok%4==0 and rok%100!=0) or rok%400==0:
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    dni = [31,28,31,30,31,30,31,31,30,31,30,31]
    if czy_przestepny(rok) and miesiac == 2:
        return 29
    elif miesiac != 2:
        return dni[miesiac-1]
    else:
        return 28
#
# wstaw nowy kod tutaj
#

testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")