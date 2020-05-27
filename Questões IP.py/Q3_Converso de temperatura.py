#Crie um programa que leia uma temperatura em graus Célsius e
#apresente-a convertida em graus Fahrenheit. A fórmula de conversão é
#� = (9 ∗ c + 160)/5.
tempo1 = float(input('Temperatura atual \n *Em Célsius: '))

converte = (9 * tempo1 + 160)/5

print (f'O tempo atual em Fahrenheit é', converte)