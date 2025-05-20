sal = float(input('Qual o seu salario: R$'))
rea = float(input('Qual o valor do reajuste: '))

final = sal + (sal * rea / 100)

print('Seu Salário antes do reajuste era de {}, e passou a ser {}'.format(sal, final))