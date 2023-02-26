#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode
#comprar. Considere US$1,00 = R$3,27.
din = float(input('Quanto de dinheiro você tem na carteira?'))
dor = din/5.26
print('Em dolar você teria:{:.2f}'.format(dor))