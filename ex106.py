'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
'''
from time import sleep


def fuction():
    funcao = ''
    while funcao != 'FIM':
        print('\033[44m~\033[m'*30)
        print('\033[44m Interactive Help Python \033[m')
        print('\033[44m~\033[m'*30)
        funcao = str(input('Digite a função ou biblioteca -> '))
        print('\033[42m Acessando o manual do {}\033[m'.format(funcao))
        sleep(2)
        print('\033[45m', help(funcao), '\033[m')


fuction()
