#Crie um sistema onde você possa cadastra jogadores de futebol 
#Cada atleta deve ter: - Id; Nome; Idade.

ide= int(input('Sua identidade ')
nome = input('Seu nome ')
idade = int(input('Quantos anos você têm? '))

if idade >= 18:
    print ('Você, {}, esta cadastro e é maior de idade'.format(nome))
else:
    print ('Seu cadastro não foi autorizado. Você é um atleta de menor'.format(idade))