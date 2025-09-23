# Escreva um programa que leia o raio de um círculo e mostre a área circunfe-
# rência do mesmo, com exatamente 4 casas decimais.

# Considere o valor de π = 3.14159

raio_circulo = float(input('Digite o raio do circulo: '))

area_circulo = 3.14159 * (raio_circulo**2)

print(f'Resultado: {area_circulo:.4f}')