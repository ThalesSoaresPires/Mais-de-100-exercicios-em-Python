'''
Faça um programa que leia uma frase pelo teclado e mostre:
->Quantas vezes aparece a letra "a".
->Em que posição ela aparece a primeira vez.
->Em que posição ela aparece pela última vez.
'''
frase = input('Digite uma frase:')
print('A letra a apareceu {} vez(es) na sua frase'.format(frase.count('a')))
print('A posição que ela apareceu a primeira vez foi {}'.format(frase.find('a')+1))
print('A vez que a letra a apareceu foi na posição {}'.format(frase.rfind('a')+1))


