def nome_curto(nomes):
    n_curto = string_curta(nomes)
    lexo = string_lexografica(nomes)
    print(f"O nome mais curto é: {n_curto}")
    print(f"O menor nome em lexograma é: {lexo}")
    
def tranformar_string(nomes):
    nome = []
    for i in range(len(nomes)):
        nome.append(nomes[i].strip().capitalize())
    return nome

def string_curta(nomes):
    nome = tranformar_string(nomes)
    n_curto = len(nome)
    for i in range(len(nome)):
        j = len(nome[i])
        if j < n_curto:
            n_curto = len(nome[i])
            curto = nome[i]
    return curto

def string_lexografica(nomes):
    nome = tranformar_string(nomes)
    lexo = nome[0]
    for i in range(len(nome)):
        if nome[i] < lexo:
            lexo = nome[i]
    return lexo
            
    
    '''len(nomes) # Conta a quantidades de nomes dentro da lista
    len(nomes[0]) # Conta a quantidade de caracteres de uma string
    nomes.strip() # Retira os espaços do começo e do fim de uma string'''
    
# nome = ['Ronei', 'Michele', 'Robson', 'Nancy', 'José', 'Manuela']
# nomes = ["  RoNei", "miChele  ", " RoBsoN  ", "nANCy  ", "JoSé ", "manueLa"]
