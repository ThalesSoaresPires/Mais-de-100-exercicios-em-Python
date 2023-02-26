'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
nome = input('Digite o seu nome completo:')
nome = nome.split()
print('O seu primeiro nome é: {}'.format(nome[0]))
ultnome = len(nome)-1
print('O seu último nome é : {}'.format(nome[ultnome]))


