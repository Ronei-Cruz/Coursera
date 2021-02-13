def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

def encontra_impares(lista, x = []):
    for i in range(len(lista)):
        if lista[0] % 2 == 0:
            lista.remove(lista[i])
            return encontra_impares(lista[:])
        else:
            x.append(lista[0])
            lista.remove(lista[0])
            return encontra_impares(lista[:])
    return x
        
def incomodam(n):
    if n  <= 0:
        return ""
    if n == 1:
        return "incomodam "
    return (incomodam(n-1) + "incomodam ")
        
def elefantes(n):
    if n <= 0 or type(n) == float:
        return ""
    if n == 1:
        return ("Um elefante " + incomodam(n) + "muita gente\n")
    else:
        return(elefantes(n-1)+str(n) + " elefantes incomoda muita gente\n"+str(n)+ " elefantes " + incomodam(n) + "muito mais\n")
