import re

texto = '''Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".
 Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é 
 necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso 
 tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;
 ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência 
 anímica do meu sangueo propósito impessoal de engrandecer a pátriae contribuirpara a evolução da humanidade.
 É a forma que em mim tomou o misticismo da nossa Raça.'''

print(re.findall(r'[Nn]avegadores|.avegar', texto))