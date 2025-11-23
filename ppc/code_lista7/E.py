numero = int(input())
numeros_lidos = list(map(int, input().split()))

soma = 0
acumulador_acima = 0
acumulador_abaixo = 0

for i in numeros_lidos:
    soma += i
    media = soma / numero

for a in numeros_lidos:
    if (a < media):
        acumulador_abaixo += 1

for b in numeros_lidos:
    if (b >= media):
        acumulador_acima += 1

print(f'{media:.1f}')
print(acumulador_abaixo)
print(acumulador_acima)
