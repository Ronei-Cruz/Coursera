def multiplica_matrizes(m1, m2):
    linhas_m1, colunas_m1 = len(m1), len(m1[0])
    linhas_m2, colunas_m2 = len(m2), len(m2[0])
    assert colunas_m1 == linhas_m2
    
    lista = []
    for linha in range(linhas_m1):
        # Começando uma nova linha 
        lista.append([])
        for coluna in range(colunas_m2):
            # Adicionando uma nova colunana linha
            lista[linha].append(0)
            for z in range(colunas_m1):
                lista[linha][coluna] += m1[linha][z] * m2[z][coluna]
    return lista
