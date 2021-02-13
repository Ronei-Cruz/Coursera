num = int(input("Digite um número inteiro maior que 1: "))
fator = 2
mult = 0
while num > 1:
    while num % fator == 0:
        num = num /  fator
        mult = mult + 1
    if mult > 0:  
        print("fator ", fator, " multiplicidade =", mult)
    fator = fator + 1
    mult = 0
    


    
