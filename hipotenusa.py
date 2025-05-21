import math

#ler os catetos 
catetoOP = float(input('Digite o valor do Cateto oposto: '))
catetoAdj = float(input('Digite o valor do cateto adjacente: '))

#Calculo da hipotenusa 
hip = math.sqrt(catetoOP**2 + catetoAdj**2)

#Exibindo o resultado 
print(f'O valor calculado da hipotenusa é igual a: {hip:.2f}')