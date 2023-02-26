'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atetla e
mostre a sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM.
-Até 14 anos: INFANTIL.
-Até 19 anos: JUNIOR.
-Até 20 anos: SÊNIOR.
-Acima: MASTER.
'''
ano = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
