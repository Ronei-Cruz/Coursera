import re

#findall - search - sub 
# compile

string = 'Este é um teste de expressões regulares, teste.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))         #Posso fazer dessa maneira, mas tendo que compilar
print(re.sub(r'teste', 'TESTE', string))    # todas as vezes que precisar chamar o re...

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('testando', string))
