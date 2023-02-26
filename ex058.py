'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número de 0 até 10. Só que agora
o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randrange
num = randrange(0, 11)
resposta = int(input('Tente adivinhar qual número o computador escolheu de 0 a 10: '))
tentativas = 1
if resposta == num:
    print('Parabéns você acertou e precisou de {} tentativa.'.format(tentativas))
else:
    while resposta != num:
        resposta = int(input('Tente novamente: '))
        tentativas = tentativas + 1
    print('Parabéns você acertou e precisou de {} tentativas.'.format(tentativas))
