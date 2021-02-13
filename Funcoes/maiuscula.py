def maiusculas(frase):
    fim = ""
    x = 0
    for x in range(len(frase)):
        y = ord(frase[x])
        if y < 91 and y > 64:
            caractere = chr(y)
            fim = fim + caractere
    return fim
            
    
   
            
    
'''len(nomes) # Conta a quantidades de nomes dentro da lista
    len(nomes[0]) # Conta a quantidade de caracteres de uma string
    nomes.strip() # Retira os espaços do começo e do fim de uma string'''
    
# nome = ['Ronei', 'Michele', 'Robson', 'Nancy', 'José', 'Manuela']
# frase = ("RoNei miChele RoBsoN nANCy JoSé manueLa")
