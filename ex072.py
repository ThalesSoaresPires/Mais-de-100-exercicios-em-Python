'''
Crie um programa que tenha uma tupla completamente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso
'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Qual número você quer ver por extenso de 0 até 20?'))
print('O número digitado foi o {}! :D'.format(contagem[num]))
