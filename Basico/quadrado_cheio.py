def quadrado():
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))
    caractere = "#"
    i = 1
    while i <= altura:
        print(caractere * largura, end = "\n")
        i = i + 1
quadrado()
