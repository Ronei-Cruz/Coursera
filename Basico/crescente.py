n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 < n2 and n2 < n3 and n1 < n3:
    print("Crescente.")
else:
    print("não está em ordem crescente.")