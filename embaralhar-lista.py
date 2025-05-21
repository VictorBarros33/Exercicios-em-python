import random 

#recebendo itens da lista
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('quarto aluno: '))

#criando lista 
lista = [n1, n2, n3, n4]

#embaralhar e mostrar resultado 
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)