def bmi(waga, wzrost):
    if waga >0 and wzrost > 0:
        return waga / wzrost ** 2
    else:
        return

print(bmi(70.5, 1.78))
print(bmi(-52.5, 1.65))