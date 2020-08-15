def sortInt(number):    #zwraca posortowany ciąg znaków jako int
    strg = str(number)
    txt = ''
    for c in strg:
        txt += c + ' '
    lst = txt.split()
    #print(int(''.join(sorted(lst))))
    return int(''.join(sorted(lst)))

def transponuj(lst):    #zmiana wierszy na kolumny
    temp = []
    for i in range(9):
        txt = ''
        for j in range(9):
            strng = str(lst[j])
            txt += strng[i]
        temp.append(txt)
    return temp

#s = [295743861,431865927,876192543,387459216,612387495,549216738,763524189,928671354,154938672]
s = [195743862,431865927,876192543,387459216,612387495,549216738,763524189,928671354,254938671]

transponuj(s)
ok = 123456789 #[znak(x + ord('0')) for x in range(1, 10)]

sudoku = True

#sprawdzamy rzedy
for a in s:
    if sortInt(a) != ok:
        sudoku = False
        break
#sparwdzamy kolumny
sk = transponuj(s)
for a in sk:
    if sortInt(a) != ok:
        sudoku = False
        break
#sprawdzamy kwadraty
sb = []
for r in range(0, 9, 3):
    for k in range(0, 9, 3):
        nrs = ''
        for i in range(3):
            txt = str(s[r+i])
            nrs += txt[k:k+3]
        sb.append(nrs)
print(sb)
for a in sb:
    if sortInt(a) != ok:
        sudoku = False
        break
#koncowa decyzja
if sudoku:
    print("Tak")
else:
    print("Nie")
