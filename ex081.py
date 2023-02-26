'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada em ordem descrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = list()
resp = 'S'
c = 0
while resp == 'S':
    num = float(input('Digite um número: '))
    lista.append(num)
    c = c + 1
    resp = input('Deseja continuar? [S/N]')
    resp = resp.upper()
print('Foram digitados {} valores.'.format(c))
lista.sort(reverse=True)
print('A lista em ordem descrescente ficou {}'.format(lista))
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
