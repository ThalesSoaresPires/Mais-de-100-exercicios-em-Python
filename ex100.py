'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados na função anterior.
'''
from random import randint
lista = list()


def sorteio():
    for c in range(1, 6):
        num = randint(1, 100)
        lista.append(num)
    print(lista)


def somapar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma = soma + c
    print('A soma de todos os valores pares é {}'.format(soma))


sorteio()
somapar()
