import math

def delta(a, b, c):
    return (b ** 2) - 4 * a * c

def main():
    print("Sendo que ax²+bx+c é uma equação do segundo grau, então...")
    print("Determine os valores da equações de segundo grau!")
    a = float(input("Qual o valor de a? "))
    b = float(input("Qual o valor de b? "))
    c = float(input("Qual o valor de c? "))
    imprime_raizes(a, b, c)
    
def imprime_raizes(a, b, c):
    resp_delta = delta(a, b, c)
    if delta(a, b, c) == 0:
        x1 = ((-b + math.sqrt(resp_delta))/ (2 * a))
        print("Formula: X = (-b +- sqrt: Delta)/2*a")
        print("A função do 2º grau possui apenas uma raiz REAL")
        print(f"X1 = {x1:.2f}")
    elif resp_delta > 0:
        x1 = ((-b + math.sqrt(resp_delta))/ (2 * a))
        x2 = ((-b - math.sqrt(resp_delta))/ (2 * a))
        print("Formula: X = (-b +- sqrt: Delta)/2*a")
        print("A função do 2º grau possui duas raízes reais distintas.")
        print(f"X1 = {x1:.2f}")
        print(f"X2 = {x2:.2f}")
    elif resp_delta < 0:
        print("a função do 2º grau não possui nenhuma raiz REAL.")
