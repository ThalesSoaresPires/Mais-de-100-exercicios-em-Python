'''
Crie uma tupla preenchida pelos primeiros 20 colocados na tabela do brasileirão, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time do Santos.
'''
brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corithians', 'Flamengo', 'Athletico-PR',
               'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goias',
               'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(brasileirao[:5])
print(brasileirao[16:])
print(sorted(brasileirao))
print('O Santos ficou em {}'.format(brasileirao.index('Santos') + 1))
