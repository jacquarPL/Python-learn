def mysplit(strng):
    myList = []
    fnd = strng.find(' ')
    start = 0
    while fnd != -1: 
        if strng[start:fnd] != '':
            myList.append(strng[start:fnd])
        start = fnd + 1
        fnd = strng.find(' ', fnd + 1)
    if strng[start:fnd] != '':
            myList.append(strng[start:])    
    return myList

print(mysplit("Być albo nie być, oto jest pytanie"))
print(mysplit("Być albo nie być,oto jest pytanie"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
