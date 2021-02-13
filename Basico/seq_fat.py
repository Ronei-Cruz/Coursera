def menu():
    j = 0
    x = int(input("Quantos numeros quer fatorar? -> "))
    while j < x:
        fatorial()
        j = j + 1
            
def fatorial():
    fat = 1
    i = 1
    n = int(input("Digite o valor de número: "))
    while i <= n:        
        fat = fat * i
        i = i + 1
    print(fat)    
   
menu()
