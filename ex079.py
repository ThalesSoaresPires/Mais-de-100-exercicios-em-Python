'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
'''
lista = list()
resp = 'S'
while resp == 'S':
    num = float(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    resp = input('Deseja continuar? [S/N]')
    resp = resp.upper()
lista.sort()
print(lista)
