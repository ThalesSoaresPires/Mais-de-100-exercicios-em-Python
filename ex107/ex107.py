'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
metade().(as funções aumentar e diminuir é relativas a um preço que vai aumentar ou diminuir x%)
Faça também um programa que importe esse módulo e use algumas dessas funções
'''
from moduloex107 import aumentar, diminuir, dobro, metade, moeda
num = float(input('Digite o preço: '))
porcentagem = int(input('Digite quantos % você quer aumentar e diminuir do preço: '))
print(f'O {moeda(num)} aumentado {porcentagem}% é {moeda(aumentar(num, porcentagem))}')
print(f'O {moeda(num)} diminuindo {porcentagem}% é {moeda(diminuir(num, porcentagem))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'A metade de {moeda(num)} é {moeda(metade(num))}')

