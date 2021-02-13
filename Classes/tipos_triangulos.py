class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        soma =(self.a + self.b + self.c)
        return soma

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            hipo = self.a ** 2
            cate = (self.b ** 2) + (self.c ** 2)
            if hipo == cate:
                return True
            else:
                return False
        elif self.b > self.a and self.b > self.c:
            hipo = self.b ** 2
            cate = (self.a ** 2) + (self.c ** 2)
            if hipo == cate:
                return True
            else:
                return False
        elif self.c > self.a and self.c > self.b:
            hipo = self.c ** 2
            cate = (self.a ** 2) + (self.b ** 2)
            if hipo == cate:
                return True
            else:
                return False
        else:
            return False

    def semelhantes(self,triangulo):
        t1_sem = (t1.a,t1.b,t1.c)
        t2_sem = (t2.a,t2.b,t2.c)
        tr1 = sorted(t1_sem)
        tr2 = sorted(t2_sem)
        x = t1.perimetro()
        y = t2.perimetro()
        resultado = []
        
        if x < y or x == y:
            for x in range(len(tr1)):
                resultado.append(tr1[x] / tr2[x])
            if resultado[0] == resultado[1] and resultado[0] == resultado[2]:
                return True
            else:
                return False
        elif y < x:
            for x in range(len(tr1)):
                resultado.append(tr2[x] / tr1[x])   
            if resultado[0] == resultado[1] and resultado[0] == resultado[2]:
                return True
            else:
                return False
            
        
