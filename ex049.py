'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.
'''
num = int(input('Digite um número inteiro:'))
for c in range(0, 11):
    conta = c * num
    print(" {} x {} é igual a {}".format(c, num, conta))

