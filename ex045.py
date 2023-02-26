'''
Crie um programa que jogue Jokenpô com você.
'''
from random import choice
from time import sleep
lance = str(input('Qual o seu lance? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
lancepc = choice(['pedra', 'papel', 'tesoura'])
lance = lance.lower()
if lance == 'pedra' and lancepc == 'pedra':
    print('O pc jogou {}, vocês empataram.'.format(lancepc))
elif lance == 'pedra' and lancepc == 'papel':
    print('O pc jogou {} você perdeu.'.format(lancepc))
elif lance == 'pedra' and lancepc == 'tesoura':
    print('O pc jogou {} você ganhou.'.format(lancepc))
elif lance == 'papel' and lancepc == 'pedra':
    print('O pc jogou {} você ganhou.'.format(lancepc))
elif lance == 'papel' and lancepc == 'papel':
    print('O pc jogou {} vocês empataram.'.format(lancepc))
elif lance == 'papel' and lancepc == 'tesoura':
    print('O pc jogou {} você perdeu.'.format(lancepc))
elif lance == 'tesoura' and lancepc == 'pedra':
    print('O pc jogou {} você perdeu.'.format(lancepc))
elif lance == 'tesoura' and lancepc == 'papel':
    print('O pc jogou {} você ganhou.'.format(lancepc))
elif lance == 'tesoura' and lancepc == 'tesoura':
    print('O pc jogou {} vocês empataram.'.format(lancepc))
