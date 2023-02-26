'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada.(Com parâmetros digitados pelo usuário)
'''


def contador(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            if c < fim:
                print(c, end=' ')
            elif c == fim:
                print(c)
                print('=-'*30)
    else:
        for c in range(inicio, fim - 1, passo):
            if c > fim:
                print(c, end=' ')
            if c == fim:
                print(c)
                print('=-'*30)


contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Digite qual vai ser o início: '))
fim = int(input('Digite qual vai ser o fim: '))
passo = int(input('Digite qual vai ser o passo: '))
contador(inicio, fim, passo)
