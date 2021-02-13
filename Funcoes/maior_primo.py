def primo(n):
    cont = 0
    i = 0
    while i <= n or cont < 2:
        i = i + 1
        condicao = n % i
        if condicao == 0:
            cont = cont + 1
    if cont <= 2:
        return n
    else:
        return False

def maior_primo(n):
    while primo(n) == False:
        primo(n)
        n = n - 1
    return n

def menu():
    n = int(input("Diegite um número inteiro -> "))
    print(maior_primo(n))

menu()

