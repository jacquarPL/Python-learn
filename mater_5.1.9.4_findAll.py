txt = """Odmiana zwyklego tekstu lorem ipsum
byla uzywana w druku od lat szescdziesiatych 
lub wczesniej, kiedy zostala spopularyzowany przez reklamy 
arkuszy transferowych Letraset. Zostala wprowadzony 
do Ery Informatyzacji w polowie lat osiemdziesiatych XX wieku przez Aldus Corporation, 
firme ktora wykorzystała ja w szablonach graficznych i edytorach tekstu
w swoim programie do publikowania PageMaker (z Wikipedii)"""

fnd = txt.find('do') 
while fnd != -1: 
    print(fnd) 
    fnd = txt.find('do', fnd + 1)
