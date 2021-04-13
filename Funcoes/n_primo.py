def primo(n):
    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        i = 3
        while (i <= (n / i)):
            if ((n % i) == 0):
                return False
            i += 2
        return True
    return False

       
def n_primo(n):
    if (n < 2): # se numero for menor que 2 não tem primo
        return 0
    elif (n == 2): # se numero for 2 tem primo, sendo assim o proprio 2
        return 1
    else:
        contador = 1
        while (n > 2):
            if (primo(n)):
                contador += 1
            n -= 1
        return contador
    return 0


def menu():
    n = int(input("Digite um número ineiro: "))
    print(n_primo(n))

menu()
