import ListaOrdenada
import random
import time

class ContaTempos:
    def lista_aleatoria(self, numero):
        lista = [random.randrange(1000) for x in range(numero)]
        return lista

    def lista_quase_ordenada(self, numero):
        lista = [x for x in range(numero)]
        lista [numero//10] = -32
        return lista
        
    def compara(self, numero):
        lista1 = self.lista_aleatoria(numero)
        lista2 = lista1[:]

        o = ListaOrdenada.Ordenador()

        print("Comparando com lista aleatória")
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha Curta demorou ", depois - antes)

        antes = time.time()
        o.insercao_ordenada(lista2)
        depois = time.time()
        print("Ordena demorou ", depois - antes)
        
        print("\nComparando com lista quase ordenadas")
        
        lista1 = self.lista_quase_ordenada(numero)
        lista2 = lista1[:]
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha Curta demorou ", depois - antes)

        antes = time.time()
        o.insercao_ordenada(lista2)
        depois = time.time()
        print("Ordena demorou ", depois - antes)
