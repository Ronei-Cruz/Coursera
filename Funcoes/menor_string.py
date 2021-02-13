def tranformar_string(nomes):
    nome = []
    for i in range(len(nomes)):
        nome.append(nomes[i].strip().capitalize())
    return nome

def menor_nome(nomes):
    nome = tranformar_string(nomes)
    n_curto = len(nome)
    for i in range(len(nome)):
        j = len(nome[i])
        if j <= n_curto:
            n_curto = len(nome[i])
            curto = nome[i]
    return curto
