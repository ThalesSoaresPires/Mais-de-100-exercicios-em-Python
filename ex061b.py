'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão
'''
prim = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))
soma = 0
flag = 1
while flag <= 10:
    if flag == 1:
        print(prim, end='-')
        flag = flag + 1
    elif flag == 2:
        soma = prim + razao
        print(soma, end='-')
        flag = flag + 1
    elif flag <= 9:
        soma = soma + razao
        print(soma, end='-')
        flag = flag + 1
    else:
        soma = soma + razao
        print(soma)
        flag = flag + 1
