'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
listapar = list()
listaimpar = list()
resp = 'S'
while resp == 'S':
    num = float(input('Digite o número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    resp = input('Deseja continuar? [S/N]')
    resp = resp.upper()
lista.sort()
listapar.sort()
listaimpar.sort()
print('A lista com todos os valores ficou: {}'.format(lista))
print('A lista só com os valores pares ficou: {}'.format(listapar))
print('A lista só com os valores impares ficou: {}'.format(listaimpar))
