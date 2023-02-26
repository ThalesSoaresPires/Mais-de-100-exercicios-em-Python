'''
Escreva um programa que faça o computador ''pensar'' em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.
O Programa deverá escrever na tela se o usuário acertou ou não.
'''
from random import randrange
num = randrange(1, 6)
#Aqui foi necessário utilizar o randrange para o computador gerar um número aleatório
resp = int(input('Tente adivinhar o número que o computador escolheu de 1 a 5: '))
if resp == num:
    print('Você acertou cabeça de jararaca')
else:
    print('Errou')
