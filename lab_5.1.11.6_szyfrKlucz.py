# Szyfr Cezara
#tekst = input("Wpisz wiadomosc: ")
tekst = "abcxyzABCxyz 123"
klucz = 2
szyfr = ''
for char in tekst:
    if char != ' ' and not char.isdigit():
        kod = ord(char) + klucz
        if kod > ord('z'):
            kod = ord('A') + (ord(char) + klucz - ord('z'))
        szyfr += chr(kod)
    else:
        szyfr += char

print(szyfr)
