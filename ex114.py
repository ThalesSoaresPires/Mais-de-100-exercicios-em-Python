'''
Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.
'''
import webbrowser
x = False
while not x:
    if webbrowser.open('pudim.com.br'):
        print('O site está acessível.')
        x = True
    else:
        print('O site não está acessíovel.')
        x = True

