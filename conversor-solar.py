real=float(input('Digite quantos reais você tem: R$'))
dolar = real/ 5.65
eu = real / 6.34
peso = real*200.91

print('Com {:.2f} você pode ter dolar {:.2f}, EURO {:.2f} ou PESO {:.2f}'.format(real, dolar, eu, peso))