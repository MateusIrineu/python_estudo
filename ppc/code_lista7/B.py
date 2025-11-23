numero = int(input())

acumulador = 0
for i in range(1, numero + 1):
    resultado = 1 / i
    acumulador += resultado
    
print(f'{acumulador:.4f}')