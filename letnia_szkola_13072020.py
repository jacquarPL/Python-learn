#
# Operatory i ich kolejnosc:
# 1. + - (unary - jedno-argumentowe)
# 2. **
# 3. * / // %
# 4. + - (binary - dwu-argumentowe)

# Python keywords:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
#
# Varaibles / zmienne - muszą zaczynac sie od liter. _ uznawany jest za literę. Case-sensitive. nie mogą nadpisywac keywordów
# PEP8 sugeruje używania małych liter do nazewnictwa zmiennych i _. Ewentualnie mixed-case np. myVariable.
# Zmienne tworzymy poprzez przypisanie im wartości - Python nie potrzebuje deklaracji zmiennych i jej typu.
# Zmienne można nadpisywać.
#
# Zapis skrócony operacji arytmetycznych:
# i = i + 2 * j           --------------> i += 2 * j
# var = var / 2           --------------> var /= 2
# rem = rem % 10          --------------> rem %= 10
# j = j - (i + var + rem) --------------> j -= (i + var + rem)
# x = x ** 2              --------------> x **= 2
#
# LAB 2.1.4.9 do zrobienia
# LAB 2.1.4.10

# Brudnopis w trakcie zajęć:
print("Potęgowanie (**)")
print(2**3)
print(2**2**3) # liczymy od prawej strony!

print("Liczba całkowita czy liczba zmiennoprzecinkowa (int vs float)?")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
# Jeżeli w wyrażeniu występuje liczba zmiennoprzecinkowa, to wynik też będzie liczbą zmiennoprzecinkową

print(4**0.5)

print("Mnożenie (*)")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print("Dzielenie (/)")
print(6 / 2)
print(6 / 2.)
print(6. / 2)
print(6. / 2.)

print("Dzielenie całkowite (//)")
print(8 // 3)
print(8 // 3.)
print(8. // 3)
print(8. // 3.)

print("Modulo (%)")
print(-7 % 2)
print(-7 % 2)
print(-7. % 2)
print(-7. % 2.)

print("Dodawanie (+)")
print(6 + 2)
print(6 + 2.)
print(6. + 2)
print(6. + 2.)

print("Odejmowanie (-)")
print(6 - 2)
print(6 - 2.)
print(6. - 2)
print(6. - 2.)

print((-2)**2)

print((2+3)**2)

print((2 ** 4)+(2 * 4.)+(2 * 4))

print("Modulo (%)")
print(7 % 2)  #Dodatnie
print(-7 % 2) #Dodatnie
print(7 % -2) #Ujemne
print(-7 % -2) #Ujemne

print("zmienne")

tuturu = 1
print("Wartośc mojej zmiennej to", tuturu)

_10top = 100

var1 = 1
var2 = 'none'
var3 = 15.

print("var1", var1, type(var1))
print("var2", var2, type(var2))
print("var3", var3, type(var3))

var1 = "rututu"
print("var1", var1, type(var1))
print("var2", var2, type(var2))
print("var3", var3, type(var3))

# Czy można stworzyc zmienną pustą
zmienna = ""
print("zmienna", zmienna, type(zmienna))

# Jak zdefiniowac nową zmienną będącą wynikiem wyrażenia
liczba1 = 10 #int
liczba2 = 2. #float
print(liczba1 * liczba2)

# Przykłąd prostego wtrącenia wartości do tekstu

imie = "Grzegorz"
nazwisko = "Iksiński"
wiek = 18
ocena_koncowa = 6
#print("Uczeń " + imie + nazwisko +" w wieku " + wiek + " otrzymał ocenę " + ocena_koncowa)
print("Uczeń %s %s otrzymał w wieku %d lat ocenę z informatyki: %d"%(imie, nazwisko, wiek, ocena_koncowa))

licznik = 0
print("licznik = ", licznik)
licznik = licznik +1
print("licznik = ", licznik)
licznik = licznik +1
print("licznik = ", licznik)

#Notacja skrócona "iteratora"
licznik = 2
licznik = licznik + 2 #2+2=4
licznik = licznik ** 2 # 4**2 = 16
licznik **= 2
licznik **= 1+1 # licznik = licznik ** (1 + 1)
print("licznik = ", licznik)
licznik **= 1+1
print("licznik = ", licznik)
licznik **= 1+1
print("licznik = ", licznik)

# Lab - pomaranczowy krol
pomaranczowy_krol = 3
agnieszka = 6
adam = 5
print(pomaranczowy_krol, agnieszka, adam, sep=",")
pomaranczy_razem = pomaranczowy_krol + agnieszka + adam
print(pomaranczy_razem)
print("Całkowita liczba pomarańczy:", pomaranczy_razem)
licznik+=1
print(licznik)
print(-7%2)