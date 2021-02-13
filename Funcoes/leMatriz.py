def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) -> matriz (listas de linhas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemenro é digitadp pelo úsuario.'''

    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento linha [" + str(i + 1) + "] coluna[" + str(j + 1) + "] -> "))
            linha.append(valor)

        # adiciona linhas a matriz
        matriz.append(linha)
    return linha

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)


