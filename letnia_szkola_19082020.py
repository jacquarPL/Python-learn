################################## Przypomnienie list##################################
# Przeszukiwanie list
Rainbow = ['czerwony', 'pomarańczowy', 'zółty', 'zielony', 'cyjan', 'niebieski', 'indygo', 'fioletowy']

print('czerwony:', 'czerwony' in Rainbow)
print('biały:', 'biały' in Rainbow)

print('czerwony:', 'czerwony' not in Rainbow)
print('biały:', 'biały' not in Rainbow)

# Wyszukiwanie czy element występuje na liście:
wylosowano = [5, 11, 9, 42, 3, 49]
obstawiono = [3, 7, 11, 42, 34, 49]
trafiono = 0

for liczba in obstawiono:
    if liczba in wylosowano:
        trafiono += 1
print("Obstawiono:", obstawiono)
print("Wylosowano:", wylosowano)
print("Trafiono:", trafiono)

# Wybieranie unikalnych elementów listy
moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Napisz program służący do wybrania unikalnych elementów w liscie:
temp_lista = []
for element in moja_lista:
    if element not in temp_lista:
        temp_lista.append(element)
moja_lista = temp_lista
print("Lista tylko z unikalnymi elementami:")
print(moja_lista)

#Tablica trójwymiarowa:
# System rezerwacji pokoju w kompleksie hoteli:
TEMP = [False for r in range(20)]
print(TEMP)


pokoje = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(pokoje)
# rezerwuj pokój w 2 budynku, na 10 pietrze, pokój 14:
pokoje[1][9][13] = True
# sprawdz wolne pokoje na 15 pietrze w 3 budynku:
wolne = 0
pokoje[2][14][0] = True
for numer_pokoju in range(20):
    if not pokoje[2][14][numer_pokoju]:
        wolne += 1

print("Wolne pokoje:", wolne)

#################################### Typy sekwencyjne: Krotki i słowniki #########################3333333
# # # Tuples are ordered and unchangeable (immutable) collections of data.
# # # They can be thought of as immutable lists. They are written in round brackets:
# # #
myTuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(myTuple)
krotka = 1,
print(type(krotka))
print(krotka)
# #
myList = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(myList)
# # #
# # # Each tuple element may be of a different type (i.e., integers, strings, booleans, etc.).
# # # What is more, tuples can contain other tuples or lists (and the other way round).
# # #
# # # You can create an empty tuple like this:
# # #
emptyTuple = ()
print(type(emptyTuple))    # outputs: <class 'tuple'>
# # #
# # # A one-element tuple may be created as follows:
# # #
oneElemTup1 = ("one", )    # brackets and a comma
oneElemTup2 = "one",     # no brackets, just a comma
# # #
# # # If you remove the comma, you will tell Python to create a variable, not a tuple.
# # # You can also create a tuple using a Python built-in function called tuple().
# # # This is particularly useful when you want to convert a certain iterable
# # # (e.g., a list, range, string, etc.) to a tuple.
myTup = tuple((1, 2, "string"))
print(myTup)
# # #
# # # You can access tuple elements by indexing them:
# # #
myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(myTuple[3])    # outputs: [3, 4]
# # #
# # # Tuples are immutable, which means you cannot change their elements (you cannot append tuples, or modify,
# # # or remove tuple elements). The following snippet will cause an exception:
# # #
myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
#myTuple[2] = "guitar"    # a TypeError exception will be raised
# # #
# # # However, you can delete a tuple as a whole:
# # #
myTuple = 1, 2, 3,
# del myTuple
print(myTuple)    # NameError: name 'myTuple' is not defined
# # #
# # # You can loop through a tuple elements, check if a specific element is present in a tuple,
# # # use the len() function to check how many elements there are in a tuple, or even join/multiply tuples:
# # #
# # # Example 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)
# #
# # # Example 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)
# #
# # # Example 3
t3 = (1, 2, 3, 5)
print(len(t3))
# #
# # # Example 4
t4 = t1 + t2
t5 = t3 * 2
print(t4)
print(t5)
# #
# # #
# # # Dictionaries are unordered*, changeable (mutable), and indexed collections of data.
# # # (*In Python 3.6x dictionaries have become ordered by default.
# # # Each dictionary is a set of key : value pairs. You can create it by using the following syntax:
# # #
myDictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3,
    }
# # #
# # # If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets
# # # or by using the get() method:
# # #
polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"]    # ex. 1
print(item1)    # outputs: soil

item2 = polEngDict.get("woda")
print(item2)    # outputs: water
print(polEngDict.keys())
print(polEngDict.items())
print(polEngDict.values())

for key in polEngDict:
    print(polEngDict.get(key))

# # # If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

polEngDict["zamek"] = "lock"
item = polEngDict["zamek"]
print(item) # outputs: lock
# # #
# # # To add or remove a key (and the associated value), use the following syntax:
# # #
myPhonebook = {}    # an empty dictionary
myPhonebook["Adam"] = 3456783958    # create/add a key-value pair
print(myPhonebook)    # outputs: {'Adam': 3456783958}
#
del myPhonebook["Adam"]
print(myPhonebook)    # outputs: {}
# # #
# # # You can also insert an item to a dictionary by using the update() method, and remove the last element by using the popitem() method, e.g.:
# # #
polEngDict = {"kwiat" : "flower"}

polEngDict.update({"gleba" : "soil"})
print(polEngDict)    # outputs: {'kwiat' : 'flower', 'gleba' : 'soil'}

polEngDict.popitem()
print(polEngDict)    # outputs: {'kwiat' : 'flower'}
#
# # # You can use the for loop to loop through a dictionary, e.g.:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for item in polEngDict:
    print(item)    # outputs: zamek
                   #          woda
                   #          gleba

# # #
# # #
# # #
# # # If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for keyas, valueas in polEngDict.items():
    print("Pol/Eng ->", keyas, ":", valueas)
# #
# # # To check if a given key exists in a dictionary, you can use the in keyword:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

if "zamek" in polEngDict:
    print("Yes")
else:
    print("No")
# # #
# # # You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

print(len(polEngDict))    # outputs: 3
del polEngDict["zamek"]    # remove an item
print(len(polEngDict))    # outputs: 2
#
polEngDict.clear()   # removes all the items
print(len(polEngDict))    # outputs: 0

del polEngDict    # removes the dictionary

# # # To copy a dictionary, use the copy() method:
# # #
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

copyDict = polEngDict.copy()
print(copyDict)

dict1 = {'John': 29, "Eve": 32}
dict2 = {'John2': 25, "Eve2": 12}
dict3 = dict1.copy()
dict3.update(dict2.items())

# # Analiza kodu:
# Wyobraźmy sobie, że stoimy przed takim oto wyzwaniem:
#
# potrzebujemy programu, który określi średni wynik grupy studentów,
# program powinien poprosić o wprowadzenie imienia studenta oraz otrzymanego wyniku,
# imiona można wprowadzać w dowolnej kolejności,
# zatwierdzenie wprowadzenia imienia bez jego podawania kończy proces wprowadzania danych,
# następnie powinna zostać wyświetlona lista imion razem z oszacowanym średnim wynikiem.

klasa = {} # tworzymy pusty słownik

while True: # tworzymy pętlę nieskończoną
    imie = input("Wprowadź imię studenta i naciśnij klawisz Enter, żeby przerwać wprowadzanie: ")
    if imie == '':
        break  # jeżeli nie wprowadzono żadnego imienia, przerwij wczytywanie kolejnych imion studentów

    wynik = int(input("Wprowadź wynik uzyskany przez studenta (0-10): "))
    # WCZYTANIE OCENY STUDENTA O DANYM IMIENIU

    if imie in klasa:
        klasa[imie] += (wynik,)
        # dodaj kolejną ocenę do krotki istniejącej już w słowniku jako wartość dla zadanego klucza (imienia)
    else:
        klasa[imie] = (wynik,)
        # jeśli imie nie istnieje jeszcze w slowniku, dodaj je tworząc krotkę z pierwszą oceną jako wartosc nowego klucza (imienia)

print(klasa)

for imie in sorted(klasa.keys()): # pętla wybierająca po kolei kolejnych studentów (ze slownika), w kolejnosci alfabetycznej - dzieki funkcji sorted()
    suma = 0 # zmienna do przechowania sumy ocen
    licznik = 0 # zmienna do przechowania liczby ocen danego studenta
    for wynik in klasa[imie]: # pętlę sumującą oceny danego studenta
        suma += wynik # obliczanie sumy ocen
        licznik += 1 # zliczanie ilości ocen
    print(imie, ":", suma / licznik) # drukowanie sredniej arytmetycznej


# Sprawdzenie typów zwracanych przez metody keys(), values() itp.
colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

klucze = colors.keys()
wartosci = colors.values()
pary = colors.items()

print(type(klucze))
print(type(wartosci))
print(type(pary))

print(klucze)
print(wartosci)
print(pary)

# Dodawanie elementów słowników do nowego słownika
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}
#
for item in (d1, d2):
    print(d3)
    d3.update(item)
print(d3)
# Alternatywne rozwiązanie, wykorzystujące prostą pętlę
# for key in d1.keys():
#     d3[key]= d1[key]
# for key in d2.keys():
#     d3[key]= d2[key]
# print(d3)

# Jeszcze inne rozwiązanie
# d3=d1.copy()
# d3.update(d2)
# print(d1)
# print(d3)