'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-A média de idade do grupo.
-Qual o nome do homem mais velho.
-Quantas mulheres têm menos de 20 anos.
'''
media = 0
idadevelho = 0
nomevelho = ''
sexo = ''
quantidade = 0
for c in range(1, 5):
    idade = int(input('Digite a sua idade: '))
    nome = input('Digite o seu nome: ')
    sexo = input('Digite o seu sexo: ')
    media = media + idade
    sexo = sexo.upper()
    if c == 1 and sexo in 'MASCULINO':
        nomevelho = nome
        idadevelho = idade
    if idade > idadevelho and sexo in 'MASCULINO':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'FEMININO' and idade < 20:
        quantidade = quantidade + 1
media = media / 4
print('a media do grupo é {:.2f}'.format(media))
print('O homem mais velho tem {} anos e ele se chama {}.'.format(idadevelho, nomevelho))
print('O número de mulheres com menos de 20 anos é {}.'.format(quantidade))
