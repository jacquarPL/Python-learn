def ftnam(ft, inch = 0.0):  #stopy lub cale
    return ft * 0.3048 + inch * 0.0254


def lbsnakg(lb):    #funty
    return lb * 0.45359237


def bmi(waga, wzrost):
    if wzrost < 1.0 or wzrost > 2.5 or \
    waga < 20 or waga > 200:
        return None
    
    return waga / wzrost ** 2


print(bmi(waga = lbsnakg(176), wzrost = ftnam(5, 7)))