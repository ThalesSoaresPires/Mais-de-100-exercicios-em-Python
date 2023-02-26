'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = list()
linha1 = []
linha2 = []
linha3 = list()
somapares = 0
maiorvalor2 = 0
c = 0
for c in range(0, 9):
    num = int(input('Digite o valor: '))
    if c < 3:
        linha1.append(num)
    elif c < 6:
        linha2.append(num)
    else:
        linha3.append(num)
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
print(linha1)
print(linha2)
print(linha3)
for lista in matriz:
    for valor in lista:
        if valor % 2 == 0:
            somapares = somapares + valor
for c in range(0, 3):
    if c == 0:
        maiorvalor2 = linha2[c]
    elif maiorvalor2 < linha2[c]:
        maiorvalor2 = linha2[c]
print('A soma de todos os números pares é {}'.format(somapares))
print('A soma de todos os valores da coluna 3 é {}'.format(matriz[0][2] + matriz[1][2] + matriz[2][2]))
print('O maior valor da segunda linha é {}'.format(maiorvalor2))
