'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.
'''
casa = float(input('Digite o valor da casa:'))
sal = float(input('Digite o valor do seu salário:'))
tempo = int(input('Digite em quantos anos você quer pagar:'))
meses = tempo * 12
prest = float(casa / meses)
if prest <= 0.3 * sal:
    print('O valor da sua prestação será de: R${}'.format(prest))
else:
    print('Empréstimo negado.')
