'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
num = float(input('Digite um número: '))
num1 = num
somatorio = 1
while num1 - 1 >= 1:
    somatorio = somatorio * num1 * (num1 - 1)
    num1 = num1 - 2
    print(num)
    print(somatorio)
print('O fatorial de {} é {}.'.format(num, somatorio))

