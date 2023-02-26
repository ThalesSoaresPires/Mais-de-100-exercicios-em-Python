'''
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem,
cobrando R$0.50 por KM para viagens até 200KM e R$0.45 para viagens mais longas.
'''
dist = int(input('De quantos KM vai ser a viagem? '))
if dist <= 200:
    preco = 0.5 * dist
    print('O preço da viagem vai ser: {} reais!'.format(preco))
else:
    preco = 0.45 * dist
    print('O preço da viagem vai ser: {} reais!'.format(preco))
