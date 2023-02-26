'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos
pesos lidos.
'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o seu peso:'))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {}.'.format(maior))
print('O menor peso é {}.'.format(menor))
