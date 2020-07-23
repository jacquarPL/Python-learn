def l100kmtompg(litry):
    return (100*3.785411784)/(litry*1.609344)


def mpgtol100km(mile):
    return 100 / (mile * 1.609344 / 3.785411784)


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
