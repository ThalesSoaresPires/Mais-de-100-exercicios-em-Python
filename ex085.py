'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e impares. No final, mostre os valores
pares e ímpares em ordem crescente.
'''
lista = list()
listapar = []
listaimpar = list()
for c in range(0, 7):
    num = float(input('Digite o valor: '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
lista.append(listapar)
lista.append(listaimpar)
listapar.sort()
listaimpar.sort()
lista.sort()
print('A lista com todos os números: {}'.format(lista))
print('A lista com os números pares: {}'.format(listapar))
print('A lista com os números impares: {}'.format(listaimpar))
