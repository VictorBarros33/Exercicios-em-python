import random

sorteio = int(input('digite a quantidade de alunos que irão participar do sorteio: '))

#Sorteando um numero 
num = random.choice(1, sorteio)

#Mostrando resultado do sorteio 
print(f'O numero do aluno sorteado foi {num}')
