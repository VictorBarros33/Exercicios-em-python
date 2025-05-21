import math
angulo = float(input('Digite um angulo qualquer: '))

#converter graus para radiano e obter os valores
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

#Mostrando os resultados 

print(f'O seno, cosseno e a tangente do ângulo {angulo} é: {sen}, {cos} e {tan} respectivamente.')