import pytest

def busca_binaria(lista, elemento, min=0,max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2
        
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio

a = [1,3,4,6,7,9]

@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 6, 3),
    (a, 4, 2),
    (a, 7, 4),
    (a, 3, 1),
    (a, 9, 5),
    (a, 2, False),
    (a, 5, False),
    (a, 8, False)
    ])

def testa_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado
    
