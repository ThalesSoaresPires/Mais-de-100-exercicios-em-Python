'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá mundo!')
Saída:
~~~~~~~~~~~~
 Olá,Mundo!
~~~~~~~~~~~~
'''


def escreva():
    texto = str(input('Escreve uma frase: '))
    linha = ('~'*(len(texto)+2))
    print(linha)
    print(' {} '.format(texto))
    print(linha)


escreva()
