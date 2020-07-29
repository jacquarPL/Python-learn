# LAB 3.1.2.14
blokow = int(input("Wprowadź liczbę bloków: ")) # wczytujemy ilosc bloczków do budowy
w_rzedzie = 1 # wyliczenia zaczynamy od góry - najwyższy rząd to tylko jeden bloczek, kolejne rzędy będą zwiększać się o jeden
wysokosc = 0 # 0 ponieważ jeszcze nic nie zbudowalismy :) nie wiemy ile rzędów powstanie, będziemy to liczyc
while blokow >= w_rzedzie: # pętla budowania rzędów. Sprawdzamy czy ilosc bloczków wystarczy do wybudowaniu rzędu o zadanej wielkosci
    #jesli warunek jest spełniony, czyli bloczków wystarczy na zbudowanie zadanego rzędu, to budujemy:
    blokow -= w_rzedzie # od ilosci bloczków odliczamy ilosc potrzebną do budowy konkretnego rzędu
    w_rzedzie += 1 # wyliczamy ilosc bloczków potrzebną do budowy kolejnego rzędu
    wysokosc += 1 # zbudowalismy jeden rząd, wiec piramida urosła o jedną wysokosc/ jeden rząd
    print("Rząd %d wybudowany, pozostało %d bloczków"%(wysokosc, blokow)) # print pomocniczy pokazujący aktualny stan pozostałych do budowy bloczków
# Pętla zakonczyła się jesli bloczków jest mniej niż potrzeba na zbudowanie kolejnego rzędu
print("Wysokość piramidy wynosi:", wysokosc) # Drukujemy ile udało się wybudować.

# #LAB 3.1.2.15
# weź dowolną nieujemną i niezerową liczbę całkowitą i nadaj jej nazwę c0;
# jeżeli jest parzysta oblicz nową wartość dla c0 równą c0 ÷ 2;
# w przeciwnym razie, jeżeli liczba jest nieparzysta, oblicz nową wartość dla c0 równą 3 × c0 + 1;
# jeżeli c0 ≠ 1, przeskocz do punktu 2.

c0 = int(input("Podaj wartość c0: "))
steps = 0
if c0 > 0:
    while c0!=1:
        if c0%2:
            c0 = 3* c0 +1
        else:
            c0//=2
        print("Aktualna wartość c0:", c0)
        steps += 1
    print("c0 wynosi 1; Ilość kroków:", steps)
else:
    print("Wartość początkowa musi być dodatnia, różna od 0!")

#Operatory logiczne and or not

var = 1
print(var > 0)
print(not (var <= 0))

print(var != 0)
print(not (var == 0))

zm = 12
print(bin(zm))

# Koniunkcja bitowa - np sprawdzanie stanu bitów w rejestrze
rej = 10
bitmask = 15
stan_rej = rej & bitmask
print(bin(rej))
print(bin(bitmask))
print(bin(stan_rej))

print(rej)
print(bitmask)
print(stan_rej)

# Koniunkcja bitowa - zerowanie bitów w rejestrze
rej_wyzerowany = rej & ~bitmask
print(bin(rej))
print(bin(bitmask))
print(bin(rej_wyzerowany))

# Alternatywa bitowa - ustawianie bitów w rejestrze
rejestr = 0b11110000
maska = 0b11000011
ustaw = rejestr | maska
print(bin(rejestr))
print(bin(maska))
print(bin(ustaw))

# Negacja bitowa
rejestr = 0b00001111
maska = 0b11111111
negacja = rejestr ^ maska
print(bin(rejestr))
print(bin(maska))
print(bin(negacja))

#Przesunięcie bitowe << >>
var = 17
print(bin(var))
var_w_prawo = var >> 1
print(bin(var_w_prawo))
var_w_lewo = var << 2
print(bin(var_w_lewo))
print(var, var_w_lewo, var_w_prawo)

#            var = 0b0010001
# 1 bit w prawo -> 0b0001000
# 2 bity w lewo -> 0B1000100

# # CWICZENIE OPERATORÓW BITOWYCH

x = 4 # 0b0100
y = 1 # 0b0001

a = x & y # 0b0000
b = x | y # 0b0101 -> 5
c = ~x # 0b1011 ---> UWAGA!!!! ~x = -(x+1) więc wynikiem -5
       # 0b0100 ^ 0b1111 -> 0b1011 (negowanie bitów)
d = x ^ 5 # 0b0100 ^ 0b0101 ---> 0b0001
e = x >> 2 # 0b0001 (1)
f = x << 2 # 0b10000 (16)

print(a, b, c, d, e, f)


########## LISTY #################
# Deklarowanie listy
lista = [] # Pusta lista
print(type(lista))

lista2 = [1, 2, 3, 4, 5, 6, 9]
print(lista2)
# Odnoszenie się do konkretnego elementu listy
print(lista2[0])
# Odnoszenie się do indeksu spoza zakresu
# print(lista2[7])
# Liczba ujemna jako index
print(lista2[-3])
# # Sprawdzanie dlugosci listy
print(len(lista2))
print("Wydrukuj wszystkie elementy listy")
# Wybieranie kolejnych elementów w pętli, funkcja len() - zwraca dlugosc obiektu iterowalnego np listy, stringa
for i in range(len(lista2)):
    print(lista2[i])
print("Druga pętla, wybierająca kolejne elementy z listy")
for el in lista2:
    print(el)


lista_rozna = [1, 2., 'jakiś ciąg znaków', ['x', 'y', 'z'], 0]
print(lista_rozna)
# Usuwanie elementów list
del lista_rozna[0]
print(lista_rozna)

# Nadpisywanie wartości danego elementu
lista_rozna[0]=2.54321
print(lista_rozna)

# Odnoszenie się do listy zagnieżdzonej
print(lista_rozna[-2])
print(lista_rozna[-2][-2])

#Odnoszenie się do elementu w stringu
ciag = 'Madagaskar'
print(ciag)
print(ciag[3])

# Dodawanie kolejnych elementów listy
# .append() - dodawanie na koncu listy
print(lista_rozna)
lista_rozna.append(99)
print(lista_rozna)

lista_do_dodania = [100, 101, 102]
lista_rozna+=lista_do_dodania
print(lista_rozna)

# metoda insert() - dodawanie lementu w konkretnym miejscu listy
print(lista_rozna)
lista_rozna.insert(5, "pozycja nr 5")
print(lista_rozna)




