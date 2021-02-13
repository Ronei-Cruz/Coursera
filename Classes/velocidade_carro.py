def main():
    carro1 = Carro('Brasilia', 1968, 'amarela', 80)
    carro2 = Carro('Fusca', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_max = velocidade_max

    def imprima(self):
        if self.velocidade == 0: #Parado da pra ver o ano
            print( "%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_max:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.velocidade))
        else:
            print( "%s %s indo muito raaaapiiiiiiidooooo!"%(self.modelo, self.cor))

    def acelere(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()
