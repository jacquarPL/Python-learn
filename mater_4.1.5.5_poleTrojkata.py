def czy_to_trojkat(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def pole_trojkata(a, b, c):
    if not czy_to_trojkat(a, b, c):
        return None
    return heron(a, b, c)

print(pole_trojkata(1., 1., 2. ** .5))