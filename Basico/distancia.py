import math

x1 = int(input("Digite a primeira cordenada de X: "))
y1 = int(input("Digite a primeira cordenada de Y: "))
x2 = int(input("Digite a segunda cordenada de X: "))
y2 = int(input("Digite a segunda cordenada de Y: "))
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if distancia >= 10:
    print("Longe")
else:
    print("Perto")