'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
'''
resp = 'S'
dados = {}
lista = list()
listamulheres = []
listavelhos = []
totalidade = 0
while resp == 'S':
    dados['nome'] = str(input('Digite o seu nome: '))
    dados['sexo'] = str(input('Digite o seu sexo: [M/F]'))
    dados['sexo'] = dados['sexo'].upper()
    dados['idade'] = int(input('Digite a sua idade: '))
    totalidade = totalidade + dados['idade']
    lista.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N]'))
    resp = resp.upper()
print('O total de pessoas cadastradas é: {} pessoas'.format(len(lista)))
media = totalidade / len(lista)
print('A média de idade das pessoas é: {}'.format(media))
for c in lista:
    if c['idade'] > media:
        listavelhos.append(c['nome'])
    if c['sexo'] == 'F':
        listamulheres.append(c['nome'])
print('As pessoas com idade maior que é média são {}'.format(listavelhos))
print('As mulheres cadastradas foram : {}'.format(listamulheres))
