c0 = 15
liczba_krokow = 0
while c0 > 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))
    liczba_krokow += 1
print(liczba_krokow)