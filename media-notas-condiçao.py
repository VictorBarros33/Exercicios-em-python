#RECEBENDO VALORES PARA A MEDIA
n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
n3 = float(input('Qual a terceira nota: '))

#CALCULANDO A MEDIA
m = (n1 + n2 +n3)/3

#ESTRUTURA DE CONDIÇÃO E RESULTADO
if m <5:
    print(f'---REPROVADO--- com {m:.2f}')
else:
    print(f'---APROVADO--- com {m:.2f}')
print('---FIM---')