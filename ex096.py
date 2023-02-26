'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retângular
(largura e comprimento) e mostre a área do terreno.
'''


def area():
    largura = float(input('Digite a largura do terreno: '))
    comprimento = float(input('Digite o comprimento do terreno: '))
    areaterreno = largura * comprimento
    print('A área do terreno é {} m²'.format(areaterreno))


area()
