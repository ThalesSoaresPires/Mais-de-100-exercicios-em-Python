'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000,00
C) Qual é o nome do produto mais barato.
'''
total = 0
c = 0
barato = 0
c2 = 0
menorpreco = 0
nomemenor = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total = total + preco
    if c2 == 0:
        menorpreco = preco
        nomemenor = nome
        c2 = c2 + 1
    elif preco < menorpreco:
        menorpreco = preco
        nomemenor = nome
    if preco > 1000:
        c = c + 1
    resp = input('Quer continuar? [S/N]')
    resp = resp.upper()
    if resp == 'N':
        break
print('O total gasto na compra foi {}'.format(total))
print('{} produtos custam mais que 1000 reais.'.format(c))
print('O produto mais barato custou {} reais e o seu nome é {}'. format(menorpreco, nomemenor))
