def soma_matrizes(m1, m2):
    lista = []
    #Chama a função verificar_matriz comparadando se elas tem a mesma dimenssão
    resultado = verificar_matriz(m1, m2) 
    if resultado == True:
        for x in range(len(m1)):
            lista.append([])
            for y in range(len(m1[x])):
                lista[x].append(m1[x][y] + m2[x][y])
        return lista
    elif resultado == False:
        return False

def verificar_matriz(m1, m2):
    if len(m1) == len(m2):
        x = 0
        for v in range(len(m1[x])):
            i = range(len(m1[x]))
            j = range(len(m2[x]))
            x += 1
            if i != j:
                return False
            else:
                continue
        return True
    else:
        return False
