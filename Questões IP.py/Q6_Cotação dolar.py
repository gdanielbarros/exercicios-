'''6. Criar o algoritmo de um programa que leia um valor em real e
apresente o mesmo em dolar, a cotação do dolar é R$ 3.50
'''
real_atual = float(input('Qual é a cotação atual? \n Valor em reais (Ex.: R$ 30.00). \n \n digite aqui ao lado: '))

dola_atual = 3.50

converte = (real_atual * dola_atual)

print (f'Sua cotação atual em dolar é {converte}')