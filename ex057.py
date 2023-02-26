'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
'''
sexo = input('Digite o seu sexo: [M/F] ')
while sexo != 'M':
    if sexo != 'F':
        sexo = input('Dados inválidos digite novamente: ')
    else:
        sexo = 'M'
'''
sexo = input('Digite o seu sexo: [M/F] ')
flag = 'falso'
while flag == 'falso':
    if sexo != 'M' and sexo != 'F':
        sexo = input('Dados inválidos digite o sexo novamente: [M/F] ')
    else:
        print('Sexo {} registrado com sucesso.'.format(sexo))
        flag = 'true'



