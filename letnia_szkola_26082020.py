### Wybrane zadania z testu końcowego
lista=[x*x for x in range(5)]
def fun(lst):
     del lst[lst[2]]
     print(lst)
     print(lst[2])
     print(len(lst))
     return lst
print(fun(lista))

# Pytanie ...
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y - 1)
print(fun(0, 3))

# Pytanie ...
nums = [1,2,3]
vals = nums
del vals[:]
print(nums)
print(vals)

# Pytanie ...
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct ['three']
for k in range (len(dct)):
    v = dct[v]
print (v)

# Pytanie ...
lista = [1,2,3]
xyz = lista

print(lista)
print(xyz)
del xyz[1]
print(lista)
print(xyz)

# Pytanie ...
a = 1
b = 0
a = a ^ b
print(a)
b = a ^ b
print(b)
a = a ^ b
print(a)
print (a, b)

# ^ (xor) to operator bitowy - przykład operacji 5^6
5   -> 0b101
6   -> 0b110
5^6 -> 0b011

# Pytanie ...
def fun(x):
    if x%2==0:
        return 1
    else:
        return 2
print(fun(fun(2)))

# Pytanie ...
for i in range(0, 11): #<0, 11) -> <0,10>
    if i % 2 == 0:
        print(i, end=",")
tup = (1,)
print(tup)

# Przykład od Pani Magdaleny
moja_L=[1,2,4,4,1,4,5,2,2,3,4,3,]
temp_L=[]
[x for x in moja_L if x not in temp_L and temp_L.append(x) ]
temp_L.sort()
print(temp_L)

# Przykład rekurencji (obliczanie sumy długości odcinków o dlugosci od 5-10cm)
def suma(dl):
    if dl<5:
        return None
    elif 5<=dl<2000:
        return dl + suma(dl+1)
    else:
        return dl

print(suma(5))
# Wyjaśnienie działania rekurencji
# return w wywołaniu funkcji działa na zasadzie pętli: 
# w linii return dl + suma(dl+1)
# zwraca wartość dl i jednocześnie ponownie wywołuje funkcję (tworzy nowy wątek),
# nie mogąc zakończyć aktualnego, tak jakby zawieszając go do czasu zakonczenia nowego wywołania (nowego wątku)
# Przykład działania dla pow funckji przy dl=5:
# 1. Wywołanie suma(5) zwraca ---> 5 + suma(6)
#   2. Nowy wątek: Wywołanie suma(6) ---> 6 + suma(7)
#     3. Nowy wątek: Wywołanie suma(7) zwraca ----> 7 + suma(8)
#       4. Nowy wątek: Wywołanie suma(8) zwraca ---> 8 + suma(9)
#         5. Nowy wątek: Wywołanie suma(9) zwraca ----> 9 + suma(10)
#           6. Nowy wątek: Wywołanie suma(10) zwraca -----> 10
# Wątek 6 uruchomił warunek gdzie funkcja suma zwraca jedną wartość bez kolejnego wywołania funkcji,
# co jest swoistym zakońćzeniem naszej "pętli" rekurencji
# W efekcie:
# wątek 6 przekazuje wartość (10) do wątku 5 (w wątku 5 wychodzi 9+10)
# wątek 5 przekazuje wartość (9+10) do wątku 4 (w wątku 4 wychodzi 8+9+10)
# wątek 4 przekazuje wartość (8+9+10) do wątku 3 (w wątku 3 wychodzi 7+8+9+10)
# wątek 3 przekazuje wartość (7+8+9+10) do wątku 2 (w wątku 2 wychodzi 6+7+8+9+10)
# wątek 1 przekazuje wartość (6+7+8+9+10) do wątku 1 (w wątku 1 wychodzi 5+6+7+8+9+10)
# Tak działa rekurencja.
# UWAGA! W naszej funkcji musi być warunek zwracający ostatecznie wartość, bez kolejnego wywołania funkcji,
# w przeciwnym wypadku stworzy nam sie "pętla nieskonczona" 
# (ograniczona do ok. 900 wywołań ze względu na wartość pewnej zmiennej środowiskowej w Pythonie)


# Przykład przechwytywania wyjątków (błędów) - instrukcje try-except:
try:
    y = 5/1
    print(y)
    z = None*None
except ZeroDivisionError:
    print("Nie dziel przez 0")
    print("!!!")
    y = 5/1
except TypeError:
    print("Nie mnóż None")

# Bez przechwycenia wyjątku (błędu) program zakończy się natychmiast po próbie wykonania błędnej linii kodu 
# y = 5/0
# print(y)

# Pytanie ..
lista_1 = [1,2]

for v in range(2): v = 0; v = 1
    lista_1.insert(-1, lista_1[v])

# Pętla dodaje elementy do listy tworząc w iteracji co następuje:
# iteracja 1: [1, 1, 2]
# iteracja 2: [1, 1, 1, 2]

print(lista_1)

# Pytanie z testu gdzie utworzono dct={'one'='two', 'two'='three', 'three'='one'}
# 0. v = dct['one'] ---> v='two'
# 1. v = dct['two'] ---> v='three'
# 2. v = dct['three'] ----> v='one'

# Który z poniższych wierszy poprawnie uruchamia (błąd tłumaczenia! powinno być DEFINIUJE!) funkcję przy użyciu dwóch parametrów, 
# gdzie oba parametry mają zerowe wartości domyślne?
# 
# 
# 1) def fun(a=0, b=0):
# 2) fun fun(a=0, b):
# 3) def fun(a=b=0):
# 4) fun fun(a,b=0):
#
# Prawidlowa odp. 1)
-----------------------------------------------

# Pytanie od kursanta: Co w poniższym kodzie jest źle:
# wierszyk=['Mary', 'had', 'a', 'little', 'lamb']
# 
# def wierszyk(wiersz):
#     del wiersz[3]
#     wiersz[3]='ram'
# 
# print(wierszyk(wierszyk))
# Wyjaśnienie: lista wierszyk została nadpisana przez funkcję o tej samej nazwie, 
# dlatego przy wywołaniu funkcji nie przekazujemy jako jej argument listy (gdyż nie istnieje),
# ale samą funkcję... W ciele funkcji del wiersz[3] sugeruje usunięcie 3 elementu, gdzie funkcja nie jest obiektem iterowalnym. Stąd kod jest błędny.

# print("Zadanie 61")
# Podaj właściwy wynik kodu:
# for i in range(0, 11): #<0, 11) -> <0,10>
#     if i % 2 == 0:
#         print(i, end=",")
# 
# a) 0,1,3,5,7,9,
# b) 0,2,4,6,8,10,
# c) 1,3,5,7,9
# d) 0,2,4,6,8,10
# Prawidlowa odpowiedz: b) 0,2,4,6,8,10
-----------------------------

# Pytanie od Kursantki - dlaczego wynikiem jest 4?
tup = (1, ) + (1, ) # Tworzy krotkę tup = (1, 1) ---> dwuelementową
tup = tup + tup  # Dodaje (1, 1) i (1, 1) w efekcie obiekt tup nadpisujemy nowym obiektem - krotką 4 elementową
print(len(tup)) # stąd len(tup) zwraca właśnie 4

--------------------------------















