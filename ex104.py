'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um num: ')
'''


def leiaint(mensagem):
    num = input(mensagem)
    while not num.isnumeric():
        print('\033[31mErro\033[m')
        num = input('Digite novamente:')
    return num
# Programa Principal


n = leiaint('Digite um num:')
print('O número digitado foi {}'.format(n))
