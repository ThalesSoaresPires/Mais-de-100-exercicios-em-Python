'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
num = int(input('Digite o valor que vai começar a progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
final = 0
soma = 0
print('A progressão começa agora : {}'.format(num), end='-')
while final < 9:
    if final == 0:
        soma = num + razao
        print(soma, end='-')
        final = final + 1
    else:
        soma = soma + razao
        print(soma, end='-')
        final = final + 1
termos = int(input('Você quer mostrar mais termos? Se sim quantos? Caso não queira digite 0: '))
final2 = 0
while final2 < termos:
    if termos == 0:
        print('O programa acabou.')
        final2 = termos
    else:
        soma = soma + razao
        print(soma, end='-')
        final2 = final2 + 1

