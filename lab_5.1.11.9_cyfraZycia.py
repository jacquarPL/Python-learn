#data = '19991229'
#data = '20000101'
data = '19680811'
while len(data) != 1:
    suma = 0
    for i in data:
        suma += int(i)
    data = str(suma)

print("cyfra życia to: " + str(suma))
