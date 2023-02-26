'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''
dados = []
todosdados = []
resp = 'S'
while resp == 'S':
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(float(input('Digite a primeira nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    todosdados.append(dados[:])
    dados.clear()
    resp = str(input('Deseja adicionar mais alunos? '))
    resp = resp.upper()
for c in range(0, len(todosdados)):
    media = (todosdados[c][1] + todosdados[c][2]) / 2
    print(' Aluno: {}\n Média: {}'.format(todosdados[c][0], media))
resp = 'S'
c = 0
while resp == 'S':
    nome = str(input('Deseja ver a nota de qual aluno? '))
    for aluno in todosdados:
        if todosdados[c][0] == nome:
            print(' Aluno: {}\n primeira nota: {}\n segunda nota: {}'.format(todosdados[c][0],
                                                                           todosdados[c][1], todosdados[c][2]))
        c = c + 1
    resp = str(input('Deseja continuar vendo as notas? '))
    resp = resp.upper()
