'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
num = float(input('Digite um número qualquer para ver o seu fatorial: '))
soma = 1
if num == 0:
    print('O fatorial de 0 é 1!!')
while num < 0:
    num = float(input('Digite novamente por favor: '))
num1 = num
while num1 - 1 >= 1:
    soma = soma * (num1 * (num1 - 1))
    num1 = num1 - 2
print('O fatorial de {} é {}'.format(num, soma))



