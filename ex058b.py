'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número de 0 até 10. Só que agora
o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randrange
num = randrange(1, 10)
resp = int(input('Tente advinhar o número que o pc escolheu de 1 a 10: '))
c = 1
if resp == num:
    print('Parabéns você acertou na {}ª tentativa.'.format(c))
while resp != num:
    print('Você errou :(. Tente novamente :D')
    resp = int(input('Tente advinhar o número que o pc escolheu de 1 a 10: '))
    c = c + 1
print('Parabéns você acertou!! E precisou de {} tentativas.'.format(c))
