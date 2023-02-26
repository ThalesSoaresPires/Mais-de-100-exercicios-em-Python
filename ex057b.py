'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
flag = 'false'
while flag == 'false':
    sexo = input('Digite o sexo: ')
    sexo = sexo.upper()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos, tente novamente.')
    else:
        print('Sexo {} registrado com sucesso.'.format(sexo))
        flag = 'true'

