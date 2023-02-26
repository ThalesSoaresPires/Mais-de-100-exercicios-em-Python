'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será o valor lógico(opcinal) indicando se será mostrado
ou nõa na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show=False):
    fat = 1
    for c in range(1, num+1):
        if show:
            if c < num:
                print('{} x '.format(c), end='')
            else:
                print('{} = '.format(c), end='')
        fat = fat * c
    return fat


print(fatorial(5, True))
