n = int(input())

sequencia_array = []
acumulador = 1

for i in range(0, n):
    sequencia = int(input())
    sequencia_array.append(sequencia)
    # print(sequencia_array)
    if (len(sequencia_array) >= 2):
        if (sequencia_array[-1] != sequencia_array[-2]):
            acumulador += 1
print(acumulador)
