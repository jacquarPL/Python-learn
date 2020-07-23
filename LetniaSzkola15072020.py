# #LAB 2.1.4.9
kilometry = 12.25
mile = 7.38
factor = 1.61
mile_na_kilometry =  mile * factor
kilometry_na_mile =  kilometry / factor
print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

#LAB 2.1.4.10
x =  '-1'
x = float(x)
y = 3*x**3-2*x**2+3*x-1

print("y =", y)

#LAB 2.1.5.2
# Ten program oblicza liczbę sekund w danej liczbie godzin.
# Autor: Grzegorz
# Data: 15.07.2020

sekundy = 3600 # liczba sekund w 1 godzinie
liczba_godzin = 3

print("Godzin: ", liczba_godzin)
print("Sekund w godzinach: ", liczba_godzin * sekundy)
print("Do widzenia")

# Funkcja input()
print("Podaj swoje imię: ")
imie = input()
print("Twoje imię to ", imie)
print(imie, ", jak się miewasz?", sep = "")

# Funkcja input() - wariant drugi

imie = input("Podaj swoje imię: ")
print("Twoje imię to ", imie)
print(imie, ", jak się miewasz?", sep = "")

#Funkcja input() - wczytywanie liczb
mile = input("Podaj liczbę mili do przeliczenia na kilometry: ")
mile = float(mile)
m2km = 1.61
km = mile*m2km
#print(mile, "mili to", km, "kilomwetrów.")
print("%.4f mili to %.4f kilometrów"%(mile, km))
print("nasze mile, można zaokrąglić do ", round(mile))

#Konkatenacja (+)
text1 = "abc"
text2 = "xyz"
print(text1+text2)
# Operator + nie jest przemienny w przypadku konkatenacji
print(text2+text1)

#Replikacja (*)
print('*' + "-"*10 + "*")
print('Ta partia?!', "Nigdy! "*10)

#Funkcje int(), float(), str()
bok_a = float(input("Wprowadź długość pierwszego boku: "))
bok_b = float(input("Wprowadź długość drugiego boku: "))
print("Długość przeciwprostokątnej wynosi " + str((bok_a**2 + bok_b**2) ** .5))
#Alternatywnie, podstawiamy wartość liczbową do stringa:
print("Długość przeciwprostokątnej wynosi %.2f"%((bok_a**2 + bok_b**2) ** .5))

#LAB 2.1.6.9
# tu wprowadź wartość zmiennoprzecinkową dla zmiennej a
a = float(input("Wprowadz wartość A: "))
# tu wprowadź wartość zmiennoprzecinkową dla zmiennej b
b = input("Wprowadz wartość B: ")
b = float(b)

# tutaj wypisz wynik dodania
print("A+B: ", a+b)
# tutaj wypisz wynik odejmowania
print("A-B: ", a-b)
# tutaj wypisz wynik mnożenia
print("A*B: ", a*b)
# tutaj wypisz wynik dzielenia
print("A/B: ", a/b)

print("\nI to by było na tyle!")

#LAB 2.1.6.10
x = float(input("Wprowadź wartość dla x: "))

y = 1/(x+1/(x+1/(x+1/x)))

print("y =", y)

#LAN 2.1.6.11
h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

print("Wydarzenie zaczyna się o %d:%d i trwa %d minut"%(h, m, d))
godz = ((m + d)//60 + h) % 24
minuta = (m + d)%60
print("Wydarzenie zakończy się o %.2d:%.2d"%(godz, minuta))
#wariant 2
print("Wydarzenie zakończy się o ", godz, ":", minuta, sep="")