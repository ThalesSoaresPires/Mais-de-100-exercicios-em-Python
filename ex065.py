'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média de
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
'''
maior = 0
menor = 0
soma = 0
c = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número inteiro: '))
    resposta = input('Você deseja continuar digitando números? [S/N] ')
    resposta = resposta.upper()
    c = c + 1
    soma = soma + num
    if c == 1:
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = soma / c
print('A média dos valores digitados foi: {}'.format(media))
print('O maior número digitado foi {}, e o menor foi {}.'.format(maior, menor))

