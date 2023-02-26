'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão
'''
primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão :'))
resposta = 0
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ')


