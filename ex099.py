'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''


def maior(*num):
    maiornum = 0
    print('Analisando os valores passados...')
    for c in num:
        if c > maiornum:
            maiornum = c
        print('{}'.format(c), end=' ')
    print('Foram digitados ao todo {} números'.format(len(num)))
    print('O maior número digitado foi {}'.format(maiornum))


maior(2, 5, 9, 10, 50, 99)
maior(4, -3, 55, 26, 78)
maior(2, 4)
