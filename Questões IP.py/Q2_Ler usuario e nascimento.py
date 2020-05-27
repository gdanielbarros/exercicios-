#2. Escreva um programa que leia o nome e o ano de nascimento do
#usuário, e calcule a sua idade.
nome = input('Seu nome: ')
ano_nasceu = int(input('Ano do nascimento: '))
atual = int(input('Atualmente, em que ano estamos? '))

idade2 = (ano_nasceu - atual)

print (f'Você {nome}, tem {idade2}')