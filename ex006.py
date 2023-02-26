#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
dob = n*2
trip = n*3
raiz = n**(1/2)
print('O dobro do seu número é {}, o triplo {} e a raiz quadrada {:.3f}'.format(dob, trip, raiz))
# dentro da chave eu coloquei o ":.3f" que assim limita o número decimal em 3 casas após a vírgula

