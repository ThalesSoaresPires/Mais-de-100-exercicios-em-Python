'''
faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa
hipotenusa² = cateto oposto² + cateto adjacente²
'''
from math import pow
from math import sqrt
catop = float(input('Digite um valor para o cateto oposto:'))
catad = float(input('Digite um valor para o cateto adjacente:'))
hip = sqrt(pow(catop, 2)+pow(catad, 2))
print('O valor da hipotenusa desse triângulo é:{:.2f}'.format(hip))
'''
Outro jeito é importando direto a fuction hypot que serve somente para calcular a hipotenusa.
from math import hypot 
catop = float(input('Digite um valor para o cateto oposto:'))
catad = float(input('Digite um valor para o cateto adjacente:'))
hip = hypot(co, ca)
print('O valor da hipotenusa desse triângulo é: {:.2f}'.format(hip))
'''
