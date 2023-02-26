'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
'''


def voto(ano=0):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = 2022 - ano
    if idade >= 18:
        return print('O seu voto é OBRIGATÓRIO.')
    elif 15 < idade < 18:
        return print('O seu voto é OPCIONAL.')
    else:
        return print('Você ainda não tem idade para votar.')


voto()
