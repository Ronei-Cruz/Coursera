lista = []
while True:
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    if num == 0:
        del lista[-1]
        break
for i in reversed(lista):
    print(i)
