'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        soma += num
        contador += 1
print('O total de números pares digitados foi {}'.format(contador))
print('A somatória dos números pares foi {}'.format(soma))
