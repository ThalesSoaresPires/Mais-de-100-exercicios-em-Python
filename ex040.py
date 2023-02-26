'''
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO.
-Média entre 5.0 e 6.9: RECUPERAÇÃO.
-Média 7.0 ou superior: APROVADO.
'''
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif 7 > media >= 5:
    print('Recuperação')
else:
    print('Aprovado')

