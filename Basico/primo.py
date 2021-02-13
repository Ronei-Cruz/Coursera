n = int(input("Digite um número inteiro: "))
cont = 0
i = 0
while i <= n:
    i = i + 1
    condicao = n % i
    if condicao == 0:
        cont = cont + 1
if cont == 2:
    print("primo")
else:
    print("não primo")

