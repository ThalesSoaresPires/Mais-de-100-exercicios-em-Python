'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número inteiro: '))
divisor = 0
for c in range(1, num+1):
    if num % c == 0:
        divisor = divisor + 1
if divisor == 2:
    print('o número é primo')
else:
    print('O número não é primo')
