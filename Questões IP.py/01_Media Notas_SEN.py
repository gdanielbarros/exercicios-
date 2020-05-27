#Faça um algoritmo para calcular a média aritmética entre duas notas
#de um aluno e mostrar sua situação, que pode ser aprovado ou
#reprovado
#Ecudando: Daniel A. Barros
mensagem = print('.' * 35,'Seja bem-vinda(o) ao Sistema Eletronico de Notas - Sen', '.' *35)
print ()
n1 = int(input('Sua segunda nota - VA1: '))
n2 = int(input('Segunda nota - VA2: '))

media  = (n1 + n2)/2

if media >= 7:
    print ('Aprovado, parabéns! :)')
else:
    print('Você tá na FINAL! Terá que fazer a VA3')

n3 = int(input('Terceira nota - VA3: '))
final = int(input('nota da VA FINAL: '))

finalmedia = (n3 + final)/2

if finalmedia >= 7:
    print ('aprovado, parabéns! :)')
else:
    print ('Após final, infelizmente, você foi reprovado :(')
