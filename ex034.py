'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
sal = float(input('Digite o valor do seu salário:'))
if sal > 1250:
    sal = sal + (sal*0.10)
    print('Seu salário com o aumento ficou: {} reais.'.format(sal))
else:
    sal = sal + (sal*0.15)
    print('Seu salário com o aumento ficou: {} reais.'.format(sal))
