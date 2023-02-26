#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prod = float(input('Digite o valor do produto:'))
prec = prod - (prod * 0.05)
print('O preço do produto com 5% de desconto é :{:.3f}'.format(prec))
