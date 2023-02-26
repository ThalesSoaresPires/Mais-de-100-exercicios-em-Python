'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''
from random import randrange
from operator import itemgetter
resultados = dict()
resultados['jogador1'] = randrange(1, 7)
resultados['jogador2'] = randrange(1, 7)
resultados['jogador3'] = randrange(1, 7)
resultados['jogador4'] = randrange(1, 7)
'''
for c in sorted(resultados, key=resultados.get, reverse=True):# A função key serve como parametro que vai 
# ser utilizado no sorted (na ordenação do dicionario), e o get para pegar o valor dentro do indice  
    print(c, resultados[c])
'''
for c in sorted(resultados, key=resultados.get, reverse=True):
    print('O {} tirou {} nos dados'.format(c, resultados[c]))
resultados = sorted(resultados, key=resultados.get, reverse=True)
print(resultados)

