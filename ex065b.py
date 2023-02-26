'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média de
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
'''
n = 0
media = 0
resp = ''
soma = 0
conta = 0
maior = 0
menor = 0
while resp != 'N':
    n = int(input('Digite um número inteiro: '))
    soma = soma + n
    conta = conta + 1
    resp = input('Deseja continuar digitando números? [S/N] ')
    resp = resp.upper()
    if n > maior:
        maior = n
    if conta == 1:
        menor = n
    elif n < menor:
        menor = n
print('A média de todos os números é {}.'.format(soma / conta))
print('O maior dos números digitados foi {}.'.format(maior))
print('O menor dos números digitados foi {}.'.format(menor))
