#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0.15 por km rodado.
dia = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos km o carro rodou?'))
preco = (dia * 60) + (km * 0.15)
print('O preço do carro ficou em: R${}'.format(preco))
