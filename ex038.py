'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os 2 são iguais
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2 and n1 != n2:
    print('O primeiro valor "{}" é o maior número.'.format(n1))
elif n2 > n1 and n2 != n1:
    print('O segundo valor "{}" é o maior número.'.format(n2))
else:
    print('Não existe valor maior, os 2 são iguais.')
