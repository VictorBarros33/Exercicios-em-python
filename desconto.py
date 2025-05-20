# pedindo para o usuario os valores
prod = float(input('Digite o valor do produto: R$'))
des = int(input('Digite o valor do desconto: '))

#calculando o desconto
final = prod - (prod * des / 100)

#entrega de resultados
print('com o produto valendo {} e o desconto sendo {}, você terá o valor final {} '.format(prod, des, final))