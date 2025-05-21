import random 

#recebendo os nomes na lista
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

#colocando os nomes na lista 
lista = [n1, n2, n3, n4]

#mostrando resultado 
print('o aluno sorteado sera: {}'.format(random.choice(lista)))
