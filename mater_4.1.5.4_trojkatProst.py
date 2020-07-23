def czy_to_trojkat(a, b, c):
    return a + b > c and b + c > a and c + a > b

def czy_to_trojkat_prostokatny(a, b, c):
    if not czy_to_trojkat(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(czy_to_trojkat_prostokatny(5, 3, 4))
print(czy_to_trojkat_prostokatny(1, 3, 4))