numero = int(input("Digite um número inteiro?: "))
resto = numero % 10
while numero != 0:
    numero = numero // 10
    resto2 = numero % 10
    if resto == resto2:
        print("Sim")
        break
    resto = numero % 10
if numero // 10 == 0 and numero == 0:
    print("Não")