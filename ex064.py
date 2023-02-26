'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag(o 999)).
'''
num = 0
c = 0
soma = 0
print('Bem vindo ao programa, a seguir vamos pedir um número inteiro, para parar o programa digite 999')
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        c = c + 1
        soma = soma + num
print('O total de números digitados foi {}.'.format(c))
print('A soma de todos os números digitados foi {}.'.format(soma))
