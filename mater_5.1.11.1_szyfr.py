# Szyfr Cezara
tekst = input("Wpisz wiadomosc: ")
szyfr = ''
for char in tekst:
    if not char.isalpha():
        continue
    char = char.upper()
    kod = ord(char) + 1
    if kod > ord('Z'):
        kod = ord('A')
    szyfr += chr(kod)

print(szyfr)
