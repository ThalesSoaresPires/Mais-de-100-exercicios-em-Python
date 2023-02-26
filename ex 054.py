'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Digite o ano em que você nasceu: '))
    idade = atual - ano
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('A quantidade de pessoas maiores de idade é {} e de menores de idade é {}'.format(maiores, menores))