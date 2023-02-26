'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
maior = 0
homens = 0
mulheresjovens = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))
    sexo = sexo.upper()
    if idade > 18:
        maior = maior + 1
    if sexo == 'MASCULINO':
        homens = homens + 1
    if sexo == 'FEMININO' and idade < 20:
        mulheresjovens += 1
    resp = str(input('Você deseja continuar? [Sim ou não?]'))
    resp = resp.upper()
    if resp != 'SIM':
        break
print(f'{maior} pessoas tem mais que 18 anos')
print(f'{homens} pessoas são homens')
print(f'{mulheresjovens} pessoas são mulheres e tem menos de 20 anos.')
