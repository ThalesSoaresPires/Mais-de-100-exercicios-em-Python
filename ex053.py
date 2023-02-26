'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços.
ex: Apos a sopa
'''
frase = input('Digite uma frase: ')
frase2 = ''
frase = frase.split()
frase = ''.join(frase)
print(frase)
for c in range(len(frase) - 1, -1, -1):
    frase2 = frase2 + frase[c]
print(frase2)
if frase == frase2:
    print('A frase é palíndromo')
else:
    print('A frase não é palíndromo')
