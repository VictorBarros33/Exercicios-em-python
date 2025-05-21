import math 

n1 = float(input('Digite qualquer numero com mais de uma casa decimal: '))

arredondadobaixo = math.floor(n1)
arredondarcima = math.ceil(n1)
arredondarproximo = round(n1) 
print(f'\n Arredondado para baixo: {arredondadobaixo}')
print(f'Arredondado para cima:{arredondarcima} ')
print(f'Arredondar para o inteiro mais proximo:{arredondarproximo}')