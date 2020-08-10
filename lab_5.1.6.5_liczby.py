def liczba(zacheta, min, max):
    ok = False
    while not ok:
        try:
            wartość = int(input(zacheta))
            ok = wartość >= min and wartość <= max
            if not ok:
                print("Błąd: podana liczba jest spoza dozwolonego zakresu (" + str(min) + ".." + str(max) + ")")
        except ValueError:
            print("Błąd: wprowadzono nieprawidłową liczbę")
        
    return wartość;

v = liczba("Podaj liczbę od -10 do 10: ", -10, 10)

print("Liczba to:", v)
