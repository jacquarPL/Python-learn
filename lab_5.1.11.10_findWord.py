#t1 = "motyw"
t1 = "motyl"
t2 = "lokomotywownia"

start = 0
wynik = t2.find(t1, start)
if wynik >= 0:
    print("Tak")
else:
    print("Nie")
