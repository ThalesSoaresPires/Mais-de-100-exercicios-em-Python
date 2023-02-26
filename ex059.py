'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]soma
[2]multiplicação
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
resp = int(input('[1]soma\n[2]multiplicação\n[3]maior\n[4]novos números\n[5]sair do programa\nqual alternativa você escolhe: '))
while resp != 5:
    if resp == 1:
        print(' a soma dos dois valores é {}'.format(num1+num2))
    elif resp == 2:
        print('A multiplicação dos dois valores é {}'.format(num1 * num2))
    elif resp == 3:
        if num1 > num2:
            print('O {} é o maior valor.'.format(num1))
        elif num1 == num2:
            print('Os valores são iguais.')
        else:
            print('O {} é o maior valor.'.format(num2))
    elif resp == 4:
        num1 = float(input('Digite o seu novo primeiro valor: '))
        num2 = float(input('Digite o seu novo segundo valor: '))
    resp = int(input('[1]soma\n[2]multiplicação\n[3]maior\n[4]novos números\n[5]sair do programa\nnovamente o que você deseja? '))
print('Fim do programa.')