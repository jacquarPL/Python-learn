

# Przykład 01 na redefinicję funkcji 'wiadomosc()'. Co otrzymamy na ekranie po uruchomieniu poniższego kodu?
def wiadomosc():
    print('abc')
 
 
def wiadomosc():
    print('def')
 
wiadomosc()


# Przykład 02 na użycie wartości domyślnych dla parametrów. Obecnie najpopularniejsza stawka VAT to 23%, więc można przyjąć że to wartość domyślna poniższej funkcji 'policz_brutto()'
def policz_brutto(netto, vat=23):
    brutto = netto * (1 + vat/100)
    print(brutto)
    
policz_brutto(100)   
policz_brutto(81)
 
policz_brutto(100, 8)
 
  
 
# Przykład 03 na użycie słowa kluczowego 'pass'
# Funkcja nic nie robi i jest poprawnie zdefiniowana
def oszczedna_funkcja():
    pass
 
# wywołanie
oszczedna_funkcja()
 
 
# Przykład 04 na stworzenie funkcji zmieniającej wielkość liter
def popraw_imie(imie="jan"):
    imie = imie.capitalize()
    print(imie)
 
popraw_imie('michal')
popraw_imie(imie='tomek')
 
 

# Przykład 05 na stworzenie funkcji zwracającej pierwiastek kwadratowy danej liczby
def pierwiastek(liczba):
    if liczba >=0:
        wynik = liczba ** 0.5
        print(wynik)
    else:
        print('Nie umiem policzyć pierwiastka kwadratowego z liczby ujemnej')
 
liczba = 9
print('Oto wynik operacji obliczania pierwiastka kwadratowego z liczby %s: ' % liczba, end='')
pierwiastek(liczba)
 
 

# Przykład 06 na funkcję odwracającą elementy listy
def odwracanka(lista):
    s = []
    for element in lista:
        s.insert(0, element)
    print(s)
 
odwracanka([2,3,4,5,6])
 
 
# Przykład 07 na funkcję weryfikująca poprawność danych. To przykład na bardzo popularne zastosowanie funkcji
def weryfikator(wartosc, minimum, maximum):
    if minimum <= wartosc <= maximum:
        print('Podana wartość znajduje się w zadanym zakresie')
    else:
        print('Podana wartość nie znajduje się w zadanym zakresie')
 
weryfikator(110, 20, 300)
weryfikator(10, 20, 300)
