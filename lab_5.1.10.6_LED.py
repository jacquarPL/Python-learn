def digit(number):
    digits = [['***','* *','* *','* *','***'],['  *','  *','  *','  *','  *'],['***','  *','***','*  ','***'],['***','  *','***','  *','***'],['* *','* *','***','  *','  *'],['***','*  ','***','  *','***'],['***','*  ','***','* *','***'],['***','  *','  *','  *','  *'],['***','* *','***','* *','***'],['***','* *','***','  *','***']]
    
    for i in range(5):
        for n in str(number):
            print(digits[int(n)][i], " ", end="")
        print()
    
digit(13698742)
