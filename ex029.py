'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limete.
'''
vel = int(input('Digite o valor da velocidade: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em {} reais'.format(multa))
else:
    print('Continue assim você não foi multado obaaa')
