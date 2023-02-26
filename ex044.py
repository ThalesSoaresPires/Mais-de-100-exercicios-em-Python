'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros.
'''
preco = float(input('Digite o preço do produto: '))
metodo = str(input('Qual o meio de pagamento?'))
metodo = metodo.upper()
vezes = 0
if metodo == 'DINHEIRO' or metodo == 'CHEQUE':
    preco = preco - (preco*0.1)
    print('O preço do seu produto ficou {}'.format(preco))
elif metodo == 'CARTÃO':
    vezes = int(input('Quantas vezes você vai querer parcelar?'))
    if metodo == 'CARTÃO' and vezes == 0 or vezes == 1:
        preco = preco - (preco*0.05)
        print('O preço do seu produto ficou {}'.format(preco))
    elif vezes == 2:
        print('O preço do seu produto não teve desconto nem cobrou juros ele ficou {} reais.'.format(preco))
    elif vezes > 2:
        preco = preco + (preco*0.2)
        print('O preço do seu produto ficou {} reais.'.format(preco))




