'''Faça um algoritmo para calcular o novo salário de um funcionário.
Sabe-se que os funcionários que recebem atualmente salário de até
R$500 terão aumento de 20%; os demais terão aumento de 10%
Educando: Daniel A. Barros - BSI/UFRPE.'''
mensagem = print('.' * 40,'Seja bem-vindo ao Contabiz', '.' * 40)

salario = float(input('Seu salário atual: '))

novo_salario = (0.2 *2) #aumento para os colaboradores que ganham R$ 500.00
aumento10 = (0.1 * 2) #Aumento para os demais colaboradores de 10%

if salario >= 500:
    print (salario * novo_salario)
else:
    print (salario * aumento10)