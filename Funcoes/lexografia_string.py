def tranformar_string(nomes):
    nome = []
    for i in range(len(nomes)):
        nome.append(nomes[i].strip())
    return nome

def primeiro_lex(nomes):
    nome = tranformar_string(nomes)
    lexo = nome[0]
    for i in range(len(nome)):
        if nome[i] < lexo:
            lexo = nome[i]
    return lexo

# nomes = ["  RoNei", "miChele  ", " RoBsoN  ", "nANCy  ", "JoSé ", "manueLa"]
