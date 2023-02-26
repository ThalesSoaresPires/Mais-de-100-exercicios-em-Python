'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas(maior peso).
C) Uma listagem com as pessoas mais leves(menor peso).
'''
pessoas = list()
resp = 'S'
dados = list()
c = 0
maiorpeso = 0
menorpeso = 0
while resp == 'S':
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]'))
    resp = resp.upper()
for p in pessoas:
    if c == 0:
        menorpeso = pessoas[c][1]
    elif pessoas[c][1] < menorpeso:
        menorpeso = pessoas[c][1]
    if pessoas[c][1] > maiorpeso:
        maiorpeso = pessoas[c][1]
    c = c + 1
print('Ao todo, você cadastrou {} pessoas'.format(c))
c = 0
for p in pessoas:
    if menorpeso == pessoas[c][1]:
        print('O menor peso é da pessoa {} que pesa {} kilos '
              .format(pessoas[c][0], pessoas[c][1]))
    elif maiorpeso == pessoas[c][1]:
        print('O maior peso é da pessoa {} que pesa {} kilos'
              .format(pessoas[c][0], pessoas[c][1]))
    c = c + 1

