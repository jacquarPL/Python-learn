tajnyNumer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
ok = 1
while ok:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba != tajnyNumer:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    else:
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
        ok = 0
for i in range(7):
	