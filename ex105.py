'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)
Adicione também as docstrings da função.
'''


def notas(situacao=False):
    """

    """
    listanotas = list()
    resp = 'S'
    maior = 0
    menor = 0
    media = 0
    while resp == 'S':
        nota = float(input('Digite a nota do aluno: '))
        media = media + nota
        listanotas.append(nota)
        resp = str(input('Deseja continuar adicionando notas? '))
        resp = resp.upper()
    media = media / len(listanotas)
    dicionario = dict()
    dicionario['Quantidade de notas:'] = len(listanotas)
    for c in listanotas:
        if c == listanotas[1]:
            menor = c
            maior = c
        elif c < menor:
            menor = c
        if c > maior:
            maior = c
    dicionario['Maior nota'] = maior
    dicionario['Menor nota'] = menor
    dicionario['Media da turma'] = media
    if situacao:
        if media > 7:
            situacao = 'Boa'
        elif media > 5:
            situacao = 'Razoável'
        else:
            situacao = 'Ruim'
        dicionario['Situação'] = situacao
    print(dicionario)


notas(situacao=True)
