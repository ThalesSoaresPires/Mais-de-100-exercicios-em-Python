'''
Reescreva a função LeiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função LeiaFloat() com a mesma funcionalidade
'''


def leiaint():
    flag = True
    while flag:
        try:
            num = int(input('Digite um valor inteiro: '))
        except KeyboardInterrupt:
            print('\033[31mErro, você não digitou nenhum valor\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mErro, você não digitou um número inteiro\033[m')
        else:
            return num


def leiafloat():
    flag = True
    while flag:
        try:
            num = float(input('Digite um valor real: '))
        except (ValueError, TypeError):
            print('\033[31mErro, você não digitou um número real\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mErro, você não digitou nenhum valor\033[m')
            return 0
        else:
            return num


print('O valor inteiro digitado foi {} e o valor real digitado é {}'.format(leiaint(), leiafloat()))

