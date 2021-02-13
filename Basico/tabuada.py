linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(coluna, "x", linha, "= ",linha * coluna, end = "\t")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1

##i = 0
##while i < 3:
##    j = 0
##    while j < 3:
##        print(3* i + j + 1, end="")  
##        #expressão
##        j = j + 1
##    i = i + 1
