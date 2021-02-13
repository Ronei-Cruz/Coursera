import ListaOrdenada
import ContaTempos
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ListaOrdenada.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = ContaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = ContaTempos.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha(self, o, l_aleat):
        o.bolha(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_insercao_ordenada(self, o, l_aleat):
        o.insercao_ordenada(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_ordenada(self, o, l_aleat):
        o.selecao_ordenada(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bolha_quase(self, o, l_quase):
        o.bolha(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_insercao_ordenada_quase(self, o, l_quase):
        o.insercao_ordenada(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_ordenada_quase(self, o, l_quase):
        o.selecao_ordenada(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_juncao_ordenada(self, o, l_aleat):
        o.juncao_ordenada(l_aleat)
        assert self.esta_ordenada(l_aleat)