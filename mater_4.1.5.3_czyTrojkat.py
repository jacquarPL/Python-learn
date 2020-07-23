def czy_to_trojkat(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(czy_to_trojkat(1, 1, 1))
print(czy_to_trojkat(1, 1, 3))