# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika

slowo_uzytkownika = "asotumie"
nowe = ""
# Uzupełnij pętlę for poniżej:
for litera in slowo_uzytkownika:
    if litera.upper() != "E" and litera.upper() != "A" and litera.upper() != "I" and litera.upper() != "U" and litera.upper() != "O": 
        nowe += (litera.upper())
print(nowe)
