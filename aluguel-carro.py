# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('quantos km foi rodado com o carro: '))
dia = int(input('Quantos dias ficou com o carro: '))
novod = dia *60
novokm = km *0.15
total = novod + novokm

print('o preço a pagar pelo aluguel do carro por {} dias, e por {} km rodados fica: R${:.2f}'.format(dia, km, total))