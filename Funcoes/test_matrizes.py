import pytest
import soma_matrizes
import multiplica_matrizes

def test_soma():
    assert soma_matrizes.soma_matrizes([[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == [[3, 4, 5], [6, 7, 8], [9, 10, 11]]

def test_mult():
    assert multiplica_matrizes.multiplica_matrizes([[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
