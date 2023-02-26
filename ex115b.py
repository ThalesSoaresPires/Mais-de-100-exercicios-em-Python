'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas
cadastradas.
'''
lista1 = ['João', 11, 'Luiza', 19, 'Luiz', 2, 'Júlia', 22, 'Thales', 24]


def cadastrar(lista):
    tamanho = len(lista[0])
    for c in range(0, len(lista)):
        if c == 0:
            print('NOME', ' ' * (14 - tamanho), 'IDADE')
        if c % 2 == 0:
            print(lista[c], end='')
            tamanho = len(lista[c])
        else:
            print(' ' * (15 - tamanho), '{}'.format(lista[c]))


def adicionar(lista):
    resp = 'S'
    while resp == 'S':
        nome = str(input('Digite o nome da pessoa: '))
        idade = str(input('Digite a idade da pessoa: '))
        lista.append(nome)
        lista.append(idade)
        resp = str(input('Deseja adicionar mais pessoas? [S/N]'))
        resp = resp.upper()


respo = ''
while respo != 3:
    print('Opção 1 -> ver lista')
    print('Opção 2 -> cadastrar pessoas')
    print('Opção 3 -> encerra o programa')
    respo = int(input('Selecione a opção desejada: '))
    if respo == 3:
        print('FIM DO PROGRAMA')
    elif respo == 1:
        cadastrar(lista1)
    else:
        adicionar(lista1)
