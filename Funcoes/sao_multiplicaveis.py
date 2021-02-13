def sao_multiplicaveis(m1, m2):
    if len(m1) != len(m2) or len(m1) == len(m2):
        i = len(m1) # número de linhas
        j = len(m2[0])# número de colunas
        x = len(m1[0])
        y = len(m2)
        if i == j and x == y:
            return True
        else:
            return False
