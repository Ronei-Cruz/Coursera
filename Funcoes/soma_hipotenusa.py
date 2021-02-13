from math import hypot

##def e_hipotenusa(n1, n2, n3):
##    x = n1 ** 2
##    y = ((n2 ** 2) + (n3 ** 2))
##    if x == y:
##        print("Hipotenusa!")
##        print("X =", x)
##        print("Y =", y)
##    else:
##        print("X =", x)
##        print("Y =", y)
        
def teste():
    n = int(input("Digite um número inteiro n1: "))
    i = 1
    j = 1
    hipo = n ** 2
    while i <= n:
        while j <= n:
            if hipo == soma_hipotenusas(i,j):
                print(soma_hipotenusas(i,j))
                break
            j = j + 1
        i = i + 1
        j = 1

def soma_hipotenusas(i, j):
    hipo = int(hypot(i, j))
    return hipo

##def triagulo(): 
##    n1 = int(input("Digiteum número interiro n1: "))
##    n2 = int(input("Digiteum número interiro n2: "))
##    n3 = int(input("Digiteum número interiro n3: "))
##    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
##        if n1 > n2 and n1 > n3:
##            print("Hipotenusa =", n1)
##        elif n2 > n1 and n2 > n3:
##            print("Hipotenusa =", n2)
##        elif n3 > n1 and n3 > n2:
##            print("Hipotenusa =", n3)
##    else:
##        return False
##    return n1, n2, n3

##triagulo()

teste()
