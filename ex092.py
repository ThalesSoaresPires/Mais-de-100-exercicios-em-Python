'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar (considere 35 anos de contribuição). 
'''
dados = {}
dados['nome'] = str(input('Digite seu nome: '))
dados['anodenascimento'] = int(input('Digite o ano do seu nascimento: '))
dados['idade'] = 2022 - dados['anodenascimento']
dados['ctps'] = int(input('Digite sua carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['anocontratado'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o seu salário: '))
    dados['aposentadoria'] = (dados['anocontratado'] + 35) - dados['anodenascimento']
for c in dados:
    print('O dado {} tem valor {}'.format(c, dados[c]))

