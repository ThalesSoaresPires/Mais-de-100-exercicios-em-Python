'''
Faça um programa para calcular o divend yeld em determinado preço de uma ação.
Primeiro pegamos o quanto foi pago em dividendos nos últimos 10 anos.
Depois a média do preço da ação a cada ano.
Então para cada ano descobrimos o Dividend yeld com base no preço da ação, o preço da ação equivale
a 100% e o dividendo a x%.
'''
lista = []
dados = {}
mediady = 0
for c in range(1, 11):
    ano = int(input('Deseja calcular o d.y de qual ano? '))
    dividendo = float(input('Quanto foi pago de dividendo em {}: '.format(ano)))
    preco = float(input('Qual foi o preço médio da ação em {}: '.format(ano)))
    dividendyeld = (dividendo * 100) / preco
    lista.append('No ano {} foi pago um Dividendyeld de {}%'.format(ano, round(dividendyeld, 2)))
    mediady = mediady + round(dividendyeld, 2)
mediady = mediady / 10
print(lista)
print('A média de dividend yeld em 10 anos é {}'.format(mediady))
