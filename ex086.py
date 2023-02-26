'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = list()
linha1 = list()
linha2 = []
linha3 = list()
for c in range(0, 9):
    num = int(input('Digite um valor: '))
    if c < 3:
        linha1.append(num)
    elif c < 6:
        linha2.append(num)
    else:
        linha3.append(num)
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
print(matriz[0])
print(matriz[1])
print(matriz[2])
