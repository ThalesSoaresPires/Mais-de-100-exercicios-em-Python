#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área
#de 2m²
alt = float(input('Digite a altura da sua parede:'))
larg = float(input('Digite a largura da sua parede:'))
area = alt * larg
tinta = area/2
print('Para pintar sua parede seria necessário {} litros de tinta'.format(tinta))
