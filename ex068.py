'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o usuário
perder, mostrando o total de vitórias consecutivas que ele conseguiu no final do jogo. 
'''
from random import randrange
c = 0
while True:
    resp2 = str(input('Você quer escolher par ou ímpar: '))
    resp = int(input('Jogue um número até 10: '))
    resp2 = resp2.upper()
    respcom = randrange(0, 11)
    soma = resp + respcom
    if soma % 2 == 0 and resp2 == 'PAR':
        print(f'O computador jogou {respcom} e você venceu')
        c = c + 1
    elif soma % 2 != 0 and resp2 == 'IMPAR':
        print(f'O computador jogou {respcom} e você venceu')
        c = c + 1
    else:
        break
print(f'O computador jogou {respcom}, você perdeu e o jogo acabou')
print(f'Você venceu {c} vez(es).')
