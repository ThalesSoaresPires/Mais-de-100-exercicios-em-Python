'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
'''
cida = input('Digite o nome de uma cidade:')
cida = cida.split()
print('SANTO' in cida[0].upper())

