# LAB 3.1.4.6
liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.

# Krok 1: Napisz wiersz kodu, który prosi użytkownika
# o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
liczby_z_kapelusza[2] = int(input("Podaj liczbę całkowitą: "))

# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
del liczby_z_kapelusza[-1]

# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print("Nasza lista zawiera %d elementów"%(len(liczby_z_kapelusza)))

print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.
print()
# ################ LISTY - powtórzenie #############################
print("####################### LISTY - POWTÓRZENIE ########################")
# DEFINICJA LISTY
myList = [1, None, True, "Jestem ciągiem znaków", 256., 0, 123]  # Lista może zawierać dane różnych typów (int, float, string, list etc.)
print(myList) # Instrukcja spowoduje wydrukowanie całej listy
print(len(myList), '\n') # Wydrukowanie liczby elementów listy

# Każdy element listy posiada index - miejsce na liscie
# Listy są zatem indexowane i mogą być uaktualniane
print(myList[3]) # drukuje wlasciwie czwarty element, gdyż indexowanie zaczyna od zera
print(myList[-1], '\n') # drukuje ostatni element z listy - listy wspierają ujemne indexy (zliczane od konca)

# Uaktualnianie list - zmiana wartości danego elementu
# Listy są mutowalne, czyli elementy mogą byc aktualizowane
myList[1] = 'element_zmieniony'
print(myList, '\n') # drukuje: [1, 'element_zmieniony', True, 'Jestem ciągiem znaków', 256, 0]

# Dodawanie nowych elementów do listy
# Obiekty klasy list posiadają wbudowane metody wspierające dodawanie elementów do listy
# Metoda insert()
myList.insert(0, "pierwszy") # 1szy argument wskazuje index na liscie, 2gi argument wskazuje obiekt/wartość wstawianą do listy
# Metoda append()
myList.append("ostatni") # argument wskazuje obiekt/element wstawiany do listy - zawsze na ostatniej pozycji w liscie
print(myList, '\n') # drukuje: ['pierwszy', 1, '?', True, 'Jestem ciągiem znaków', 256, 0, 'ostatni']
#Listy można też dodawać
secList = ['element1', 'element2']
sumList = myList + secList
print(sumList, '\n')  # drukuje: ['pierwszy', 1, '?', True, 'Jestem ciągiem znaków', 256, 0, 'ostatni', 'element1', 'element2']

# Listy mogą być zagnieżdzone
myList = [[11, 12, 13],
          [21, 22, 23],
          [31, 32, 33]]
print(myList) # drukuje: [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# Odwoływanie sie do elementów listy zagnieżdzonej:
print(myList[1]) # drukuje element o indexie 1 z listy zewnętrznej, a zatem listę: [21, 22, 23]
print(myList[1][2], '\n') # drukuje element o indexie 2 z wewnętrznej listy będącej elementem o indexie 1 w liscie zewnętrznej, a zatem: 23

myList = [['00', '01', '02'],
          ['10', '11', '12'],
          ['20', '21', '22']]
print(myList) # drukuje: [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
# Odwoływanie sie do elementów listy zagnieżdzonej:
print(myList[1]) # drukuje element o indexie 1 z listy zewnętrznej, a zatem listę: ['10', '11', '12']
print(myList[1][2], '\n') # drukuje element o indexie 2 z wewnętrznej listy będącej elementem o indexie 1 w liscie zewnętrznej, a zatem: 12
print(len(myList)) # drukuje 3
print(len(myList[1])) # drukuje 3
print(len(myList[1][2])) # drukuje 2

# Usuwanie elementów listy
myList = [1, 2, 3, 4]
del myList[2] #Usuwa element o indeksie 2 - czyli de facto trzeci element listy (liczbę 3)
print(myList, '\n') # drukuje: [1, 2, 4]
del myList #usuwa całą listę

# # Listy mogą być "iterowane" w pętli for
print("Pierwsza implementacja pętli: ")
myList = ["white", "purple", "blue", "yellow", "green"]
for color in myList:
    print(color) # w kolejnych liniach drukuje kolory pobrane z listy
#lub drugi wariant:
print("Druga implementacja pętli: ")
for color_index in range(len(myList)): # for color_index in range(5):
    print(color_index) # ta linia pokazuje, że pętla nie iteruje po kolejnych elementach z listy, ale po indexach wygenerowanych przez funkcję range()
    print(myList[color_index]) # ta linia drukuje juz elementy z listy, odwołując się do kolejnych indexów, generowanych przez pętlę for.

# Funkcja len() zwraca długość danych sekwencyjnych np list czy stringów (ciągów znaków)
myList = ["white", "purple", "blue", "yellow", "green", "yellow"]
print(len(myList)) # drukuje wartość 6
print("Usuńmy jeden element i sprawdźmy długość ponownie")
del myList[2]
print(len(myList)) # drukuje wartość 5
print(myList)

# Iterowanie po pętli zagnieżdżonej
nestedList = [['00', '01', '02'],
          ['10', '11', '12'],
          ['20', '21', '22']]

# for wiersz in nestedList:
#     print(wiersz)
#     for kolumna in wiersz:
#         print(kolumna)

for element in nestedList:
    print(element)
    for wartosc in element:
        print(wartosc)
#
# Usuwanie konkretnego elementu - metoda remove()
myList.remove('yellow') #usuwa z listy pierwsze wystąpienie elementu podanego jako argument metody, w tym przypadku słowo 'yellow'
print(myList) #drukuje: ['white', 'purple', 'green', 'yellow']
# Zauważmy, że drugie wystąpienie słowa 'yellow' pozostało na liscie
# UWAGA! Próba usunięcia elementu, którego lista nie zawiera wywoła wyjątek: ValueError
#
#
######################## Zadania z listami ###############################
# Przeanalizujmy kod:
moja_lista = [] # Tworzenie pustej listy.
print(moja_lista)
print(type(moja_lista))
for i in range(5):
    moja_lista.append(i - 1)
    # [5, 4, 3, 2, 1]
print(moja_lista)


# list = [1, 2, 3, 4, 5]
# list.insert(2, 'A')
# print(list)
#
# # 3.1.4.11-12
# # LAB 3.1.4.13
# # 3.1.4.15
#
# Równoległą w czasie zmiana wartości elementów listy (zmiana pozycji elementów na liscie)
lista = [10, 1, 8, 3, 5]

lista[0], lista[4] = lista[4], lista[0]
lista[1], lista[3] = lista[3], lista[1]
print(lista)

#Sortowanie bąbelkowe:

lista = [8, 10, 6, 2, 4] # lista do posortowania
swapped = True # to trochę fałszywe - potrzebujemy tego, by wprowadzić pętlę while

while swapped:
    swapped = False # jak na razie bez zamian
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            swapped = True # zamiana wystąpiła!
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)
# Metoda sort()
lista = [8, 10, 6, 2, 4, 2.5, 7.8]
lista.sort()
print(lista)
print()

print(" Kopiowanie list oraz wycinki ")
# Kopiowanie list a tworzenie wskaźnika/referencji do tego samego obaszaru pamięci
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_kopia = lista # Taki zapis tworzy refderencje do tego samego obszaru pamięci!
lista.append(11)
print(lista_kopia)

#Wycinki
# Jak zrobić faktyczną  kopię listy?

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_kopia = lista[:] # Taki zapis tworzy kopię elementów listy!
lista.append(11)
print(lista_kopia)
# "Kilka printów z wycinków list"
print(lista[:3]) #Pierwsze 3 elementy - indexy od 0-2
print(lista[3:]) # Od elementu o indexie 3 do konca
print(lista[3:5])
print(lista[3:-2])
print(lista[-5:-2])

# Wycinki można tworzyc na wiele sposobów, ale ich efekt (lista elementow moze byc taka sama)
print(lista[:4] == lista[-11:-7])




