def quadrado_vazio():
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))
    caractere = "#"
    completo = caractere * largura
    if largura > 2:
        espaco = caractere + (" " * (largura - 2 )) + caractere
    else:
        espaco = completo
    if altura >= 1:
        print(completo)    
    for i in range(altura - 2):
        print(espaco)
    if altura >= 2:
        print(completo)

quadrado_vazio()
