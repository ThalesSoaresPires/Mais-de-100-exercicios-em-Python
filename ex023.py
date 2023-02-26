'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex:  Digite um número:1834
unidade:4
dezena:3
centena:8
milhar:1
'''
num = int(input('Digite um número de 0 a 9999: '))
u = (num % 10)//1
d = (num % 100)//10
c = (num % 1000)//100
m = num//1000
print('unidade:{}'.format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))
'''
num = int(input('Digite um número de 0 a 9999: '))
u = num//1 % 10
d = num//10 % 100
c = num//100 % 1000
m = num//1000
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar:{}'.format(m)) 
'''

