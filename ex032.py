'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
ano = int(input('Digite o ano: '))
x = ano % 100
#Aqui estou pegando somente os 2 ultimos número do ano.
if x == 0 and ano % 400 != 0:
    print('O ano {} não é bissexto'.format(ano))
#aqui estou checando se os 2 últimos numeros do ano são 0 para checar se o resto da divisão
#por 400 é diferente de 0.Porque se for igual ele vai ser bissexto
elif x % 4 == 0:
    print('O ano {} é bissexto'.format(ano))
#aqui estou checando se os 2 últimos números do ano são divisiveis por 4 porque essa é a segunda condição
#para que o ano seja bissexto
else:
    print('O ano não é bissexto')
