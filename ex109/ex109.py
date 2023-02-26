''' Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida
no desafio 108
'''
from moduloex109 import aumentar, diminuir, dobro, metade, moeda
n = float(input('Digite o preço: '))
p = int(input('Digite quantos % você quer aumentar e diminuir do preço: '))
print(f'O {moeda(n)} aumentado {p}% é {moeda(aumentar(n, p))}')
print(f'O {moeda(n)} diminuindo {p}% é {moeda(diminuir(n, p))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
print(f'A metade de {moeda(n)} é {moeda(metade(n))}')

