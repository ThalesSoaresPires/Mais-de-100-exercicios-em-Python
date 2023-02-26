'''
faça um programa que ajuda um jogador da mega-sena a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
'''
from random import randrange
resp = 'S'
jogo = []
listadejogos = []
while resp == 'S':
    quantidade = int(input('Deseja criar quantos jogos? '))
    for c in range(0, quantidade):
        for cont in range(0, 6):
            num = randrange(60)
            jogo.append(num)
        listadejogos.append(jogo[:])
        jogo.clear()
    print(listadejogos)
    resp = str(input('Deseja continuar? [S/N]'))
    resp = resp.upper()
    listadejogos.clear()
