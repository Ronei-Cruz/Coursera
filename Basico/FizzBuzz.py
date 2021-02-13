numero = int(input("Digite um número: "))
resultado1 = numero % 5
resultado2 = numero % 3
if resultado1 == 0 and resultado2 == 0:
    print("FizzBuzz")
else:
    print(numero)