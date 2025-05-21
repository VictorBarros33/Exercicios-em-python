#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n1 = int(input('Digite um número: '))
resultado = n1 % 2
if resultado == 0:
    print('Seu número é par')
else:
    print('Seu número é ímpar')    

