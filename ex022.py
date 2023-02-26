'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas
-> O nome com todas as letras minúsculas
-> Quantas letras ao todo (sem considerar espaços)
-> Quantas letras tem o primeiro nome
'''
nome = input('Digite o seu nome completo:')
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Sem considerar os espaços seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))
#Aqui estamos subtraindo o número de espaços do nome
nome = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(nome[0])))
#E por fim separamos todos as palavras da frase e mostramos o tamanho só da palavra na posição 0

