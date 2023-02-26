'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
num = int(input('Digite um número: '))
escolha = int(input('Escolha uma das opções abaixo:'
                    '\n- 1 para binário '
                    '\n- 2 para octal'
                    '\n- 3 para hexadecimal'
                    '\n'))
if escolha == 1:
    print('O número {} convertido em binário fica: {}'.format(num, bin(num)))
elif escolha == 2:
    print('O número {} convertido em octadecimal fica: {}'.format(num, oct(num)))
elif escolha == 3:
    print('O número {} convertido em hexadecimal fica: {}'.format(num, hex(num)))
else:
    print('Valor inválido.')
#O próprio python já tem funções para transformar as bases decimais, bin, oct e hex.
