def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)

def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

def leitura2():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)

