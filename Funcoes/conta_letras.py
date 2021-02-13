def conta_letras(frase, contar = "vogais"):
    x = frase
    y = contar.strip().lower()
    if y == "vogais":
        qnt = verificar_vogais(x)
        return qnt
    elif y == "consoantes":
        qnt = verificar_consoantes(x)
        return qnt
    
def verificar_vogais(frase):
    vogais = ["a", "e", "i", "o", "u"]
    cont = 0
    for i in range(len(frase)):
        if frase[i].lower() in vogais:
            cont += 1
    return cont

def verificar_consoantes(frase):
    vogais = ["a", "e", "i", "o", "u"]
    cont = 0
    texto = frase.split()
    for i in range(len(texto)):
        texto2 = texto[i]
        for j in range(len(texto2)):
            if texto2[j].lower() not in vogais:
                cont += 1
    return cont
