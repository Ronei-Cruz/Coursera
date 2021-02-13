import Bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()

    @pytest.mark.parametrize(("b.calcula_raizes, esperado")[
        (1, 0, 0,1, 0),
        (1, -5, 6,2, 3, 2),
        (10, 10, 10, 0),
        (10, 20, 10,1, -1)
        ])
    
    def testa_raiz(self, b.calcula_raizes, esperado):
        assert b.calcula_raizes == esperado
