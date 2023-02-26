'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
from math import tan
from math import sin
from math import cos
from math import radians
ang = int(input('Digite o valor do ângulo:'))
angrad = radians(ang)
print('O valor do cosceno é: {:.2f}'.format(cos(angrad)))
print('O valor do seno é: {:.2f}'.format(sin(angrad)))
print('O valor da tangente é: {:.2f}'.format(tan(angrad)))
#Nesse exercício tivemos que transformar o ang em radiano antes de calcular o cos, o sen e a tangente.

