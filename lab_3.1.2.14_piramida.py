#blokow = int(input("Wprowadź liczbę bloków: "))
blokow = 2
#
# Napisz tutaj swój kod.
#	
wysokosc = 0
while blokow > wysokosc:
    for i in range(wysokosc +1):
        blokow -= 1
    wysokosc += 1
print("Wysokość piramidy wynosi:", wysokosc)