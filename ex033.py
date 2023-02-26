'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
if n1 > n2 and n1 > n3:
    print('O valor {} é o maior.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O valor {} é o maior.'.format(n2))
else:
    print('O valor {} é o maior.'.format(n3))
if n1 < n2 and n1 < n3:
    print('O valor {} é o menor.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O valor {} é o menor.'.format(n2))
else:
    print('O valor {} é o menor.'.format(n3))

