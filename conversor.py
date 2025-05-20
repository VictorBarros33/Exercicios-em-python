# Solicita ao usuário que digite a medida em metros
metros = float(input("Digite a medida em metros: "))

# Converte para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000
km = metros / 1000
hm = metros / 100
dc = metros/ 10


# Exibe os resultados
print(f"\nMedida em metros: {metros} m")
print(f"Convertido para centímetros: {centimetros} cm")
print(f"Convertido para milímetros: {milimetros} mm")