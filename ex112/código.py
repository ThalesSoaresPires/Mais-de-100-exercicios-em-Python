'''
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie
uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com
validação de dados para aceitar apenas valores que sejam monetários.
'''
import moeda1
from dados import dados1
n = dados1.leiadinheiro('Digite o preço: ')
p = int(input('Digite quantos % você quer aumentar e diminuir do preço: '))
moeda1.resumo(n, p)

