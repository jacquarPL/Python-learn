#### Powtórzenie funkcji ################

# Deklarowanie funckji
def nazwa_funckji(opcjonalny_parametr1, opcjonalny_Parametr2):
    # ciało funkcji
    # TODO
    pass # pusta instrukcja

# Deklaracja funkcji bez parametrów
def fun_bez_parametrow():
    pass

# Deklaracja funckji z realnymi instrukcjami, nie wykona się dopóki jej nie wywołamy
def dummy_fun():
    print("To jest głupiutka funkcja...")

# Wywołanie funkcji bez parametrów
dummy_fun()

############################ Wywoływanie funckji a parametry ######################################
# Przykład 1 - funkcja z parametrami pozycyjnymi
def fun_z_parametrami_poz(par1, par2, par3):
    print(par1, par2, par3, sep="  #  ")

# Przykład 2 - funkcja z parametrami keywordowymi
def fun_z_parametrami_key(par1="Parametr1", par2="Parametr2", par3="Parametr3"):
    print(par1, par2, par3, sep="  #  ")

# Przykład 3 - funkcja z parametrami mieszanymi (pozycyjne i keywordowe)
def fun_z_parametrami_mix(par1, par2="Parametr2", par3="Parametr3"):
    print(par1, par2, par3, sep="  #  ")

# Wywoływanie funkcji w zależności od rodzaju parametrów
# 1. Parametry pozycyjne - wywołanie pozycyjne
fun_z_parametrami_poz("Wyraz1", "wyraz2", "Wyraz3")
# 2. Parametry pozycyjne - wywołanie pozycyjne
fun_z_parametrami_poz(par3="Wyraz1", par1="wyraz2", par2="Wyraz3")
# 3. Parametry pozycyjne - wywołanie pozycyjne i keywordowe - błędne
#fun_z_parametrami_poz(par3="Wyraz3", "wyraz1", "Wyraz2")
# 4. Parametry pozycyjne - wywołanie pozycyjne i keywordowe - poprawne
fun_z_parametrami_poz("wyraz1", "Wyraz2", par3="Wyraz3_key")
fun_z_parametrami_poz("wyraz1", par3="Wyraz2", par2="Wyraz3_key")

#######################################
# 5. Parametry keywordowe - wywołanie keywordowe
fun_z_parametrami_key(par1="key1", par2="key2", par3="key3")
# 6. Parametry keywordowe - wywołanie bez przekazania wartosci parametrów
fun_z_parametrami_key()
# 7. Parametry keywordowe - wywołanie z wybranymi wartosciami parametrów
fun_z_parametrami_key(par2="TADAM")
# 8. Parametry keywordowe - wywołanie z wybranymi wartosciami parametrów, pozycyjne
fun_z_parametrami_key("TADAM", "TADAM2")

#######################################
# 9. Parametry mieszane - wywołanie z parametrami pozycyjnymi
fun_z_parametrami_mix("Mix1")
# 10. Parametry mieszane - wywołanie z parametrami pozycyjnymi i keywordowymi
fun_z_parametrami_mix("Mix1", par3="TADAM3")


########## Co zwraca funkcjia bez słowa return ###################
temp = fun_z_parametrami_mix("Mix1")
print(temp)
# Funkcja, w ciele której nie ma słowa return, zwraca zawsze wartość None

# Deklaracja funkcji zwracającej wartość (słowo kluczowe return)
# 1. pusty return

def fun(var1, var2):
    print(var1, var2)
    return

zwrotka = fun(2, 3)
print(zwrotka)

# 2. return zwracający wartość wyrażenia

def fun_mnoz(var1, var2):
    print(var1, var2, sep = " * ", end=" = ")
    return var1*var2

zwrotka = fun_mnoz(2, 3)
print(zwrotka)

# 3. funkcja zwracająca różne wartości w zależności od pewnego warunku

def fun_dziel(var1, var2):
    if var2 == 0:
        print("Nie dziel przez 0!")
        return False
    else:
        print(var1, var2, sep = " / ", end=" = ")
        return var1/var2

zwrotka = fun_dziel(6, 0)
print(zwrotka)

##### Zakresy funkcji ########
print("\n\nZakresy funkcji\n")
# Zmienne występujące poza funkcją mają zasięg również wewnątrz tej funkcji,
# dopóki funkcja ni edefiniuje zmiennej o takiej samej nazwie
# 1. zmienna globalna użyta wewnątrz funkcji
var = True
def funkcja():
    print(var)
funkcja()
# 2. zmienna globalna i lokalna o tej samej nazwie wewnątrz funkcji
var = True
def funkcja():
    var = False
    print(var)

print("Wartość zmiennej globalnej:", var)
print("Wartość zmiennej lokalnej:", end = " ")
funkcja()
print("Wartość zmiennej globalnej:", var)

# 3. zmienna globalna i jej nadpisanie/przywołanie wewnątrz funkcji
var = True
def funkcja():
    global var
    var = False
    print(var)


print("Wartość zmiennej globalnej:", var)
print("Wartość zmiennej lokalnej:", end = " ")
funkcja()
print("Wartość zmiennej globalnej:", var)

# Zmienna zdefiniowana wewnątrz funkcji (lokalna), ma zakres tylko wewnątrz tejże funckji

zmienna1 = 1
zmienna2 = 2

def fuzn_zm():
    zmienna3 = 3
    print(zmienna3)
    return zmienna3

zmienna3=fuzn_zm()
print(zmienna1)
print(zmienna2)
print(zmienna3)

############## Rekurencja ###################
print("\n\nRekurencja\n")
# Funkcja silnia
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * (3 * (2 * (1))) = 24