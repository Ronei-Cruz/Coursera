n = int(input("Digite o valor de n: "))
i = 0
while n != 0:
    i += n % 10 
    n //= 10
print(i)