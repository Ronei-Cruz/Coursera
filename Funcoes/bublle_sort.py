def bublle_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                print(lista)
    return lista

    
def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) / 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        elif elemento < lista[meio]:
            primeiro = meio + 1
        else: return False
        
    return False

def insertion_sort(lista):
        n = len(lista)
        for i in range(1, n):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = chave
        return lista
