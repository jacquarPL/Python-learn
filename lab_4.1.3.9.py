def czy_pierwsza(liczba):
    for i in range(2, int(liczba**0.5)+1):
        if liczba % i == 0:
            return False
    return True

for i in range(1, 20):
	if czy_pierwsza(i + 1):
	    print(i + 1, end=" ")
print()
