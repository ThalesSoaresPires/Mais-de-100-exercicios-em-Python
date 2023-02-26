'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeada e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote
e mantenha tudo funcionando.
'''
from UtilidadesCeVex111 import moeda

n = float(input('Digite o preço: '))
p = int(input('Digite quantos % você quer aumentar e diminuir do preço: '))
moeda.resumo(n, p)
