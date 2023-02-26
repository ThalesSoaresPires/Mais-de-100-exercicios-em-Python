'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''
num = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razao: '))
final = 0
somatoria = 0
print(num, end=' - ')
while final < 9:
    if final == 0:
        somatoria = num + razao
        print(somatoria, end=' - ')
        final = final + 1
    else:
        somatoria = somatoria + razao
        final = final + 1
        print(somatoria, end=' - ')


