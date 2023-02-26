'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''
'''
from math import trunc
num = float(input('Digite um número real:'))
print('A parte inteira desse número é:', trunc(num))
****** 1 jeito de fazer
'''
import math
num = float(input('Digite um valor real:'))
print('A parte inteira desse número é:', math.trunc(num))
#Segundo jeito de fazer
