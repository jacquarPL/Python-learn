t = "Ala wzory rozwala"
tekst = ""
for char in t:
    if char != ' ':
        tekst += char
dl = len(tekst)
print(tekst)
palindrom = True
for i in range(dl // 2):
    print(str(i) + " " + tekst[i] + " " + tekst[dl - i - 1])
    if tekst[i].lower() != tekst[dl - i - 1].lower():
        palindrom = False
        break
if palindrom:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
