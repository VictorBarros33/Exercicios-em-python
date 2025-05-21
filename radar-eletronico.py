#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('LIMITE DE VELOCIDADE 80KM/H')

radar = int(input('Qual foi o limite registrado pelo radar: '))


if radar > 80:
    multa = (radar-80)*7 #calculo da multa separada
    print(f'LIMITE EXCEDIDO, VOCÊ FOI MULTADO EM: R${multa}')
else:
    print('VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE')
