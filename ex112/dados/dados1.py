def leiadinheiro(msg):
    entrada = str(input(msg)).replace(',', '.').strip()
    while entrada.isalpha() or entrada == '':
        print('Erro: "{}" não é um preço válido. '.format(entrada))
        entrada = str(input('Digite novamente o valor: ')).replace(',', '.').strip()
    return float(entrada)


