'''
Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
-Equilátero: todos os lados iguais.
-Isósceles: dois lados iguais.
-Escaleno: todos os lados diferentes.
'''
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo pode existir')
    if r1 == r2 and r1 == r3:
        print('O triângulo é equilatero')
    elif (r1 == r2 and r1 != r3) or (r2 == r3 and r2 != r1) or (r3 == r1 and r3 != r2):
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('O triângulo não pode existir')
