a, b, c, d = map(int, input().split())
menor = 9999
if (menor % 2 == 0 and menor < b):
    menor = a
if (b % 2 == 0 and b < menor):
    menor = b
if (c % 2 == 0 and c < menor):
    menor = c
if (d % 2 == 0 and d < menor):
    menor = d
print(menor)