'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.
'''
lista = []
expressao = str(input('Digite uma expressão:'))
for letra in expressao:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista) == 0:
            lista.append('(')
        else:
            lista.remove('(')
if len(lista) == 0:
    print('A expressao está correta.')
else:
    print('A expressao está incorreta.')


