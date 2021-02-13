lista = [21, 15 , 14, 8, 98, 1, 54, 68]
def maior_elemento(lista):
    maximo = lista[0]
    for x in lista:
        if x > maximo:
            maximo = x
    return maximo
