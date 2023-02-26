'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-A média de idade do grupo.
-Qual o nome do homem mais velho.
-Quantas mulheres têm menos de 20 anos.
'''
nomevelho = ''
mediaidade = 0
maioridade = 0
quantidade = 0
for c in range(1, 5):
    idade = int(input('Digite sua idade: '))
    mediaidade = mediaidade + idade
    nome = input('Digite o seu nome: ')
    sexo = input('Digite o seu sexo: ')
    sexo = sexo.upper()
    if c == 1 and sexo in 'MASCULINO':
        maioridade = idade
        nomevelho = nome
    if sexo in 'MASCULINO' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
#aqui o "in" significa dentro então se dentro de sexo tiver masculino então retorna true
    if sexo in 'FEMININO' and idade < 20:
        quantidade = quantidade + 1
print('A maior idade masculina é {} e o nome dele é {}.'.format(maioridade, nomevelho))
mediaidade = mediaidade / 4
print('A média da idade das pessoas é de {}'.format(mediaidade))
print('O número de mulheres abaixos de 20 anos é {}.'.format(quantidade))
