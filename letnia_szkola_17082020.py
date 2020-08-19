

# Przykład na utworzenie dokumentacji dla funkcji w konwencji 'docstring'
# Użycie:
# help(kwadrat)
# help(pierwiastek)

def kwadrat(liczba):
    """ Funkcja oblicza i zwraca kwadrat podanej liczby"""
    return liczba**2

print(kwadrat(10))


def pierwiastek(a):
    """Funkcja oblicza i zwraca wartość pierwiastka kwadratowego dla danego argumentu

    (float) -> float
    :param a: argument funkcji
    :return: wartość pierwiastka kwadratowego dla danego argumentu"""
    return a ** 0.5

print(pierwiastek(625))

help(kwadrat)
help(pierwiastek)


# --------------------------------------------------------


# Niewielka modyfikacja laboratorium 4.1.3.7 - dodałem rok 300 i oczekiwaną wartość "None"
# https://en.wikipedia.org/wiki/Leap_year - stąd skopiowałem pseudokod i bardzo szybko przedstawiłem go w j. Python
# leap - przestępny
# common - zwykły, nieprzestępny


def czy_przestepny(rok):
    if rok % 4 != 0:
        return False
    elif rok % 100 != 0:
        return True
    elif rok % 400 != 0:
        return False
    else:
        return True

def dni_w_miesiacu(rok, miesiac):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if rok < 1582 or miesiac <1 or miesiac > 12:
        return None

    if czy_przestepny(rok) and miesiac == 2:
        return 29

    return dni[miesiac - 1]


testuj_lata = [1900, 2000, 2016, 1987, 300]
testuj_miesiace = [2, 2, 1, 11, 4]
testuj_wynik = [28, 29, 31, 30, None]

for i in range(len(testuj_lata)):
    r = testuj_lata[i]
    m = testuj_miesiace[i]
    print(r, m, "-> ", end="")
    wynik = dni_w_miesiacu(r, m)
    if wynik == testuj_wynik[i]:
        print("OK")
    else:
        print("Nie powiodło się")


# ---------------------------------------------------------------

# Niewielka modyfikacja laboratorium 4.1.3.7 - dodałem wywołania dla 2001.2.29 oraz 2002.2.30 - oba wywołania powinny zwrócić 'None'

def czy_przestepny(rok):
    if rok % 4 != 0:
        return False
    elif rok % 100 != 0:
        return True
    elif rok % 400 != 0:
        return False
    else:
        return True

def dni_w_miesiacu(rok, miesiac):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if rok < 1582 or miesiac <1 or miesiac > 12:
        return None

    if czy_przestepny(rok) and miesiac == 2:
        return 29

    return dni[miesiac - 1]

def dzien_w_roku(rok, miesiac, dzien):
    dni = 0
    for m in range(1, miesiac):
        md = dni_w_miesiacu(rok, m)
        if md == None:
            return None
        dni += md
        
    md = dni_w_miesiacu(rok, miesiac)
    if dzien >= 1 and dzien <= md:
        return dni + dzien
    else:
        return None


print(dzien_w_roku(2000, 12, 31)) # 366
print(dzien_w_roku(2000, 1,1)) # 1
print(dzien_w_roku(2000, 2,1)) # 32
print(dzien_w_roku(2000, 3,1)) # 61
print(dzien_w_roku(2001, 2, 29)) # None
print(dzien_w_roku(2002, 2, 30)) # None
