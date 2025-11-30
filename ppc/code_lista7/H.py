n = int(input())

maior = 100
maior_somado = 100

for i in range(1, n + 1):
    apostas = int(input())
    maior_somado = maior_somado + apostas
    if (maior > maior_somado):
        maior
    elif (maior_somado > maior):
        maior = maior_somado
print(maior)
