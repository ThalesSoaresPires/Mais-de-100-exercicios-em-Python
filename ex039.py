'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora dele se alistar.
-Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.
'''
ano = int(input('Digite o ano em que você nasceu: '))
idade = 2022 - ano
if idade < 18:
    print('Você ainda vai se alistar e falta {} anos.'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passou do tempo de você se alistar. Passou {} anos.'.format(idade-18))

