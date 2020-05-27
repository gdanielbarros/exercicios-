#4. Criar um algoritmo de um programa que lê um número e apresenta o quadrado e o cubo desse número.
print ('.' * 35, 'A seguir, digite o número que será elevado ao quadrado / cubo', 35 * '.')
'\n'
n1 = int(input('Número: '))

quadrado = (n1 ** 2)
cubo = (n1 ** 3)

print (f'O número digitado ao quadrado é {quadrado} e ao cubo {cubo}')