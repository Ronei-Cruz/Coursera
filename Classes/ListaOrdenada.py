class Ordenador:
    def __init__(self):
        pass

    # Insertion Sort
    def insercao_ordenada(self,lista):
        n = len(lista)
        for i in range(1, n):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = chave
        return lista

    # Buble Sort
    def bolha(self, lista):
        n = len(lista)
        for j in range(n-1):
           for i in range(n-1):
               if lista[i] > lista[i+1]:
                   # troca elementos nas posições i e i+1
                   lista[i], lista[i+1] = lista[i+1], lista[i]
        return lista

    #Selection Sort
    def selecao_ordenada(self,lista):
        n = len(lista)
        for j in range(n-1):
            minimo = j
            for i in range(j,n):
                if lista[i] < lista[minimo]:
                    minimo = i
            if lista[j] > lista[minimo]:
                aux = lista[j]
                lista[j] = lista[minimo]
                lista[minimo] = aux
                
        return lista
