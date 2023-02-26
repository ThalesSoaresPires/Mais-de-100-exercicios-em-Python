'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nõa tenha sido
informado corretamente.
'''


def ficha(nome='', gols=0):
    if nome != '':
        print('O nome do jogador é: {}'.format(nome))
    else:
        print('O jogador ficou sem nome.')
    if gols != 0:
        print('E o jogador fez {} gols'.format(gols))
    else:
        print('E o jogador não fez gols.')


ficha('', 2)
