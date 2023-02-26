#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input("Digite o valor em metros: "))
cen = m*100
mil = m*1000
print('{} metros é {} centimetros e {} milimetros'.format(m, cen, mil))
