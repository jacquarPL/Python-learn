def str2list(strng):
    txt = ""
    for char in strng:
        txt += char + " "
    lst = txt.split()
    return lst
        
#t1 = "arbuzy".lower()
#t2 = "burza".lower()
t1 = "Ranek".lower()
t2 = "Nerka".lower()
#print(str2list(t1))
l1 = sorted(str2list(t1))
l2 = sorted(str2list(t2))

if l1 == l2:
    print("To anagramy")
else:
    print("To nie są anagramy")
