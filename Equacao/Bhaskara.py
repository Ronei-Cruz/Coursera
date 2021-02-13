import math

class Bhaskara:

    
    def delta(self, a, b, c):
        return (b ** 2) - 4 * a * c

    def main(self):
        a = float(input("Qual o valor de a? "))
        b = float(input("Qual o valor de b? "))
        c = float(input("Qual o valor de c? "))
        print(self.calcula_raizes(a, b, c))
        
    def calcula_raizes(self, a, b, c):
        resp_delta = self.delta(a, b, c)
        if resp_delta == 0:
            x1 = ((-b + math.sqrt(resp_delta))/ (2 * a))
            return 1, x1
        elif resp_delta > 0:
            x1 = ((-b + math.sqrt(resp_delta))/ (2 * a))
            x2 = ((-b - math.sqrt(resp_delta))/ (2 * a))
            return (2, x1, x2)
        elif resp_delta < 0:
            return 0
