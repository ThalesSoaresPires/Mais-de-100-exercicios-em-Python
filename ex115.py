'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas
cadastradas.
'''


def cadastrar():
    lista = []
    pessoas = dict()
    resp = 'S'
    while resp == 'S':
        pessoas['nome'] = input('Digite o seu nome: ')
        pessoas['idade'] = int(input('Digite a sua idade: '))
        lista.append(pessoas.copy())
        resp = input('Deseja cadastrar novas pessoas? [S/N]')
        resp = resp.upper()
    print(lista)


cadastrar()
