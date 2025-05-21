#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n1 = int(input('Digite a quandidade de numeros para o jogo: '))
n2 = int(input('Digite o numero em que deseje sortear: '))

sorteio = random.randint(1, n1)

if n2 == sorteio:
    print(f'VOCÊ ACERTOU : O NUMERO ESCOLHIDO FOI: {sorteio}')
else: 
    print(f'VOCÊ ERROU INFELIZMENTE: O NUMERO ESCOLHIDO FOI: {sorteio}')


