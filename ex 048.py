'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''
soma = 0
contagem = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        contagem += +1
print('No total os número impáres e múltiplos de três são {} números.'.format(contagem))
print('O somatório de todos os valores ímpares e múltiplos de 3 é {}.'.format(soma))
