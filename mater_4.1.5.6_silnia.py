def funkcja_silni_rek(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * funkcja_silni(n - 1)

def funkcja_silni(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    iloczyn = 1
    for i in range(2, n + 1):
        iloczyn *= i
    return iloczyn

for n in range(1, 6): # sprawdzenie
    print(n, funkcja_silni(n))