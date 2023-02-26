'''
Faça um programa que leia o nome e a média de um aluno, guardando também a situação(media 7 ou
mais o aluno ta aprovado, abaixo disso reprovado) em um dicionário. No
final, mostre o conteúdo da estrutura na tela.
'''
resp = 'S'
dados = dict()
lista = dict()
c = 1
while resp == 'S':
    dados['nome'] = str(input('Digite o nome do aluno: '))
    dados['media'] = float(input('Digite a media do aluno: '))
    if dados['media'] >= 7:
        dados['situação'] = 'Aprovado'
    else:
        dados['situação'] = 'Reprovado'
    lista[f'{c} aluno'] = dados.copy()
    c = c + 1
    resp = str(input('Deseja continuar adicionando aluno? [S/N]'))
    resp = resp.upper()
print(lista)
