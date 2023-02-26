'''
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
'''
resp = 'S'
dados = dict()
lista = list()
while resp == 'S':
    dados['nome'] = str(input('Digite o nome do jogador: '))
    dados['partidas'] = int(input('Quantas partidas o jogador jogou? '))
    dados['totaldegols'] = 0
    for c in range(1, dados['partidas'] + 1):
        gols = int(input('Quantos gols ele fez na {} partida: '.format(c)))
        dados['totaldegols'] = dados['totaldegols'] + gols
    dados['aproveitamento'] = dados['totaldegols'] / dados['partidas']
    lista.append(dados.copy())
    resp = str(input('Deseja continuar adicionando jogadores? [S/N]'))
    resp = resp.upper()
print(lista)
resp2 = 'S'
escolha = ''
while resp2 == 'S':
    escolha = str(input('Digite o nome do jogador que quer ver o aproveitamento:'))
    for c in lista:
        if escolha == c['nome']:
            print('O aproveitamento do jogador {} é de {:.2f} gols/partida'.format(c['nome'], c['aproveitamento']))
    resp2 = str(input('Deseja ver o aproveitamento de mais algum jogador? [S/N]'))
    resp2 = resp2.upper()
