'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
termos = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
cont = 0
print(t1, end=', ')
print(t2, end=', ')
while cont < termos - 2:
    t3 = t1 + t2
    print(t3, end=', ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')