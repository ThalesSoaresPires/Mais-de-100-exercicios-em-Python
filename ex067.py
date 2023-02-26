'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.
'''
c = 1
while True:
    num = float(input('Digite um número:'))
    if num < 0:
        break
    while c <= 10:
        if c < 10:
            print(num * c, end=' - ')
            c = c + 1
        else:
            print(num*c)
            c = c + 1
    c = 1
print('Fim')
