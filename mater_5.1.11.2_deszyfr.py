# Szyfr Cezara - rozszyfrowywanie wiadomosci
szyfr = input('Podaj kryptogram: ')
tekst = ''
for char in szyfr:
    if not char.isalpha():
        continue
    char = char.upper()
    kod = ord(char) - 1
    if kod < ord('A'):
        if kod > ord('Z'):
            tekst+= chr(kod)

print(tekst)
