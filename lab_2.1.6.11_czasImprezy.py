h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

# wprowadź tutaj swój kod
h += (m + d) // 60
h %= 24
m = (m + d) % 60

print(h, m, sep=":")
