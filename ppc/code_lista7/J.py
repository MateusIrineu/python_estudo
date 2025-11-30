n = int(input())
acumulador = 0
for i in range(0, n):
    tentativa = int(input())
    if (tentativa != 1):
        acumulador += 1
print(acumulador)