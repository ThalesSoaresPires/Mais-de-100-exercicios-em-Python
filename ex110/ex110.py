'''
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que
mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até
aqui.
'''
from moduloex110 import resumo
n = float(input('Digite o preço: '))
p = int(input('Digite quantos % você quer aumentar e diminuir do preço: '))
resumo(n, p)
