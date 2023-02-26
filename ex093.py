'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.
'''
dados = dict()
dados['nome'] = str(input('Digite o nome do jogador: '))
dados['partidas'] = int(input('Digite quantas partidas ele jogou: '))
totalgols = 0
for c in range(1, dados['partidas'] + 1):
    gols = int(input('Quantos gols ele fez na {} partida: '.format(c)))
    totalgols = totalgols + gols
dados['total de gols'] = totalgols
print(dados)
