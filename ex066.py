'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor de 999, que é a condição de parada. No final mostre quantos números foram
 digitados e qual foi a soma entre eles. (desconsiderando o flag) '''
c = 0
soma = 0
while True:
    num = int(input('digite um número inteiro, para parar digite 999:'))
    if num == 999:
        break
    c = c + 1
    soma = soma + num
print(f'A quantidade de números digitados foi {c}.')
print(f'A soma entre os números deu {soma}.')
