#9. Fazer um programa que solicite 2 números e informe:
#a) A soma dos números OK;
#b) O produto do primeiro número pelo quadrado do segundo OK;
#c) O quadrado do primeiro número;
#d) A diferença do quadrado do primeiro número pelo dobro do segundo

n1 = float(input('Primeiro número'))
n2 = float(input('Segundo número'))

soma = (n1 + n2)
protudo1 = (n1 ** n2)
quadrado1 = (n1 ** 3)
quadrado2 = (quadrado1 - 2 * n2)

print(f'A) A soma dos número: {soma}')
print(f'B) O protudo do primeiro número pelo quadrado do segundo: {protudo1}')
print(f'C) O quadrado do primeiro número: {quadrado1}')
print(f'D) A difrença do quadrado do primeiro número pelo dobro do segundo: {quadrado2}')