def primo(n):
    cont = 0
    i = 0
    while i <= n:
        i = i + 1
        condicao = n % i
        if condicao == 0:
            cont = cont + 1
    if cont <= 2:
        print("Primo!")
    else:
        return False

def maior_primo():
    n = int(input("Diegite um número inteiro -> "))
    while primo(n) == False:
        if primo(n) == False:
            print("Não é Primo")
            n = int(input("Diegite um número inteiro -> "))
        
maior_primo()