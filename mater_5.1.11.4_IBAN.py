# walidator IBAN 

iban = input("Proszę, podaj IBAN: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Wprowadzono niepoprawne znaki.")
elif len(iban) < 15:
    print("Wprowadzony IBAN jest za krótki.")
elif len(iban) > 31:
    print("Wprowadzony IBAN jest za długi.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("Wprowadzony IBAN jest poprawny.")
    else:
        print("Wprowadzony IBAN jest niepoprawny.")
