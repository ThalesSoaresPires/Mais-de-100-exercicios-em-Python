'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
n = int(input('Quantos elementos da sequência de fibonacci você quer ver? '))
flag = 1
t1 = 0
t2 = 1
while flag <= n - 2:
    if flag == 1:
        print(t1, end='->')
        print(t2, end='->')
    t3 = t1 + t2
    print(t3, end='->')
    t1 = t2
    t2 = t3
    flag = flag + 1
print('Fim')
