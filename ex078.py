'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.
'''
maior = 0
menor = 0
lista = []
posmaior = 0
posmenor = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    lista.append(num)
    if c == 0:
        menor = num
    elif num < menor:
        menor = num
    if num > maior:
        maior = num
for pos, valor in enumerate(lista):
# Na função enumerate a primeira variavel depois do for corresponde ao
# contador, e a segunda variavel corresponde ao conteudo presente na posição do contador.
    if valor == maior:
        posmaior = pos
    elif valor == menor:
        posmenor = pos
print('O maior número foi {}, e a sua posição foi {}'.format(maior, posmaior))
print('O menor número foi {}, e a sua posição foi {}'.format(menor, posmenor))

