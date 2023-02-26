'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão
'''
'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
prim = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))
flag = 1
soma = 0
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
flag = 1
termos = float(input('Você quer ver mais termos? Se sim digite quantos, se não digite 0: '))
while termos != 0:
    while flag <= termos:
        soma = soma + razao
        print(soma, end='-')
        flag = flag + 1
        if flag == termos:
            soma = soma + razao
            print(soma)
            flag = flag + 1
    termos = float(input('Você quer ver mais termos? Se sim digite quantos, se não digite 0: '))
    flag = 1
print('Fim do programa.')
