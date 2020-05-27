'''7. Fazer um programa que pergunta um valor em metros e imprime o
correspondente em decímetros, centímetros e milímetros'''
metro = float(input('Valor em metros: '))

centi = metro * 100
deci = metro * 0.10000
mili = metro * 0.001000

print ('Os valores convertidos, correspondem à \n Centimetro: {} \n Decimetro: {} \n Militro {}'.format(centi, deci, mili))