'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: Considere que o caixa possui notas de R$50.00 , R$20.00, R$10.00, e R$1.
'''
while True:
    valor = int(input('qual valor você deseja sacar? '))
    nota50 = valor // 50
    print('O número de notas de 50 reais é {}'.format(nota50))
    nota20 = (valor % 50) // 20
    print('O número de notas de 20 reais é {}'.format(nota20))
    nota10 = ((valor % 50) % 20) // 10
    print('O número de notas de 10 reais é {}'.format(nota10))
    nota1 = (((valor % 50) % 20) % 10) // 1
    print('O número de notas de 1 real é {}'.format(nota1))
    resp = input('Deseja sacar algum outro valor? [S/N]')
    resp = resp.upper()
    if resp != 'S':
        break

