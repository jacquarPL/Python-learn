# # Operatory porównujące
# # Przyrównanie ==
przypisanie  = 2
przyrownanie = 2
print(przypisanie)
print(przyrownanie == przypisanie)
# # Wartości Boolowskie: True, False
#
# #Kilka przykładów porównań:
print("2==2: ", 2 == 2)
print("2==2.: ", 2 == 2.)
#
# #Priorytetyzacja operatorów (arytmetyczna vs porównujące)
print(10 == 2 * 6)
# # Porównanie wartości liczbowej ze stringiem - zwróci "prawie zawsze" false)
print(2=='2')
#
# # Operator nierówności !=
var1 = 10
var2 = 10
var3 = 15
print('10 != 10', var1 != var2)
print('10 == 10', var1 == var2)
print('10 != 15', var1 != var3)
print('10 == 15', var1 == var3)
#
# Operator większości >
print("Operator większości")
print("10>10: ", var1 > var2)
print("15>10: ", var3 > var2)
print("10>15: ", var1 > var3)
# Operator większy-równy >=
print("Operator większości/równości")
print("10>=10: ", var1 >= var2)
print("15>=10: ", var3 >= var2)
print("10>=15: ", var1 >= var3)
#
# Operator mniejszości <
print("Operator mniejszości")
print("10<10: ", var1 < var2)
print("15<10: ", var3 < var2)
print("10<15: ", var1 < var3)

# Operator mniejszy-równy <=
print("Operator mniejszości/równości")
print("10<=10: ", var1 <= var2)
print("15<=10: ", var3 <= var2)
print("10<=15: ", var1 <= var3)

#
# #Używając jednego z operatorów porównania w Pythonie, napisz prosty dwuliniowy program,
# # który przyjmuje parametr n jako dane wejściowe, będące liczbą całkowitą, i wypisuje w konsoli False
# # jeżeli n jest mniejsze niż 100, lub True jeżeli n jest większe lub równe 100.
#
n = int(input("Podaj wartość n: "))
print("Czy wartość n jest większa/równa 100?: ", n >= 100)

# Instrukcje warunkowe - wstęp
pies = 1
ladna_pogoda = 1
if pies + ladna_pogoda == 2:
    print("Idziemy na spacer z psem")
    print("Porzucamy mu patyk")
    print("Posiedzimy na ławeczce")
print("Zjemy obiad")

# łączenie warunków
pies = True
ladna_pogoda = True
if pies and ladna_pogoda:
    print("Idziemy na spacer z psem")
    print("Porzucamy mu patyk")
    print("Posiedzimy na ławeczce")
print("Zjemy obiad")

# Przykłąd instrukcji if-else:

def idziemy_na_spacer():
    #print("Idziemy na spacer, bo pogodna jest ładna.")
    print("Możemy wyjść z domu!")

def idziemy_do_kina():
    print("Idziemy do kina, bo są bilety na fajny film.")

def idziemy_do_teatru():
    print("Idziemy do teatru, bo udało się zdobyć bilety.")

pogoda = input("Czy jest pogoda? [T/N]: ")
if pogoda=="T":
    idziemy_na_spacer()
    teatr = input("Czy mamy bilety do teatru? [T/N]: ")
    film = input("Czy grają dobry film w kinie? [T/N]: ")
    if teatr=="T":
        idziemy_do_teatru()
    else:
        idziemy_do_kina()
else:
    print("Zostajemy w domu")

# if-elif-else
# Zadanie
# Jeseli mamy bilety do teatru - jedziemy do teatru, jezeli nie,
# to idziemy na spacer, pod warunkiem, że jest pogoda. Jesli nie ma pogody, to skończymy w kinie, pod warunkiem, że grają dobry film.
#Jeśli nie, to zostajemy w domu.

def idziemy_na_spacer():
    print("Idziemy na spacer, bo pogodna jest ładna.")

teatr = input("Czy mamy bilety do teatru? [T/N]: ")
pogoda = input("Czy jest pogoda? [T/N]: ")
film = input("Czy grają dobry film w kinie? [T/N]: ")
dom = True

if teatr=="T":
    idziemy_do_teatru()
elif pogoda=="T":
    idziemy_na_spacer()
elif film=="T":
    idziemy_do_kina()
else:
    if dom:
        print("Zostajemy w domu")
    else: print("Spacerujemy dalej")


# Slajd  3.1.9
# przeczytaj dwie liczby
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))

# wybierz większą liczbę
if liczba1 > liczba2: większaLiczba = liczba1
else: większaLiczba = liczba2

# wyświetl wynik
print("Większą liczbą jest:", większaLiczba)

# Przykład 3 slajd 3.1.9:
# przeczytaj trzy liczby
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))
liczba3 = int(input("Wprowadź trzecią liczbę: "))

# tymczasowo zakładamy, że pierwszy numer
# jest największa
# sprawdzimy to wkrótce
największaLiczba = liczba1

# sprawdzamy, czy druga liczba jest większa niż obecna największaLiczba
# i uaktualniamy największaLiczba jeżeli zachodzi taka potrzeba
if liczba2 > największaLiczba:
    największaLiczba = liczba2

# sprawdzamy, czy trzecia liczba jest większa niż obecna największaLiczba
# i uaktualniamy największaLiczba jeżeli zachodzi taka potrzeba
if liczba3 > największaLiczba:
    największaLiczba = liczba3

wyświetlamy wynik
print("Największą liczbą jest:", największaLiczba)

# LAB 3.1.1.11
#
name = input("Podaj nazwę kwiatu: ")

if name == "Skrzydłokwiat":
    print("Tak, Skrzydłokwiat jest najlepszy w historii")
elif name == "skrzydłokwiat":
    print("Nie, nie nie! Chcę duży Skrzydłokwiat!")
else:
    print("Skrzydłokwiat! A nie", name + "!")
    print("Spathiphyllum! Not %s!" %name)




#############################    KONSULTACJE   ######################################

# # # LAB 3.1.1.12
# # jeżeli dochód obywatela nie był wyższy niż 85,528 talarów, podatek był równy 18% dochodu minus 556 talarów i 2 centy (była to tak zwana ulga podatkowa)
# # jeżeli dochód był wyższy niż ta kwota, podatek był równy 14,839 talarów i 2 centy plus 32% nadwyżki ponad 85,528 talarów.
#
dochód = float(input("Wprowadź roczny dochód: "))
# tutaj wpisz swój kod
if dochód <= 85528:
    podatek = (18/100 * dochód) - 556.02
else:
    podatek = 14839.02 + (dochód - 85528)*32/100
# koniec naszego kodu
podatek = round(podatek, 0)
if podatek < 0: podatek = 0.
print("Podatek wynosi:", podatek, "talarów.")
# Kosultacje - zapis wartości wewnątrz ciągów znaków z użyciem operatora %
print("Podatek wynosi %s talarów."%podatek)  #%s zrobi to samo co zrobiłaby funkcja str(podatek)
print("Podatek wynosi %d talarów."%podatek)  #%d lub %i zrobi to samo co zrobiłaby funkcja int(podatek)
print("Podatek wynosi %.3f talarów."%podatek)  #%f zrobi to samo co zrobiłaby funkcja float(podatek)

#### Sprawdzanie typu zmiennej w instrukcji warunkowej - przykład ######
var1 = 1
var2 = 2.
var3 = "asd"
print(type(var1))
print(type(var2))
print(type(var3))

if type(var3) is str:
    print("String!")
else: print("not string")




############# if -else zagnieżdzanie rozwinięcie tematu w ramach konsultacji

teatr = input("Czy mamy bilety do teatru? [T/N]: ")
pogoda = input("Czy jest pogoda? [T/N]: ")
film = input("Czy grają dobry film w kinie? [T/N]: ")
dom = True
#
# if teatr=="T":
#     idziemy_do_teatru()
# elif pogoda=="T":
#     idziemy_na_spacer()
# elif film=="T":
#     idziemy_do_kina()
# else:
#     if dom:
#         print("Zostajemy w domu")
#     else: print("Spacerujemy dalej")


# Poniższy kod jest alternatywnym zapisem tego co wyżej.
# Wyżej w formie if-elif-else (kaskadowy zapis), niżej w formie if-else zagnieżdżonych
# Oba kody działąją tak samo :)

if teatr=="T":
    idziemy_do_teatru()
else:
    if pogoda=="T":
        idziemy_na_spacer()
    else:
        if film=="T":
            idziemy_do_kina()
        else:
            if dom:
                print("Zostajemy w domu")
            else:
                print("Zostajemy pod chmurką")


