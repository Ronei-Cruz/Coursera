lista = [1, 2, 3, 4, 5, 6, 9, 8, 7, 4, 6, 4, 5, 3, 2, 4]
def remove_repetidos(lista):
    nova =[]
    for x in lista:
        if x not in nova:
            nova.append(x)
    return sorted(nova)



