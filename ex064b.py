'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag(o 999)).
'''
n = 0
soma = 0
flag = 0
while n != 999:
    n = int(input('Digite um número inteiro, se quiser parar digite 999: '))
    if n == 999:
        print('O programa acabou.')
    else:
        soma = soma + n
        flag = flag + 1
print('Foram digitados {} números.'.format(flag))
print('A soma entre eles ficou {}.'.format(soma))
