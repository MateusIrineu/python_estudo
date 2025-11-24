numero = int(input())
numeros_lidos = list(map(int, input().split()))

soma = 0
acumulador_acima = 0
acumulador_abaixo = 0
a_list = []
b_list = []

for i in numeros_lidos:
    soma += i
    media = soma / numero

for a in numeros_lidos:
    if (a < media):
        acumulador_abaixo += 1
        a_list.append(a)

for b in numeros_lidos:
    if (b >= media):
        acumulador_acima += 1
        b_list.append(b)


print(f'{media:.1f}')
print(acumulador_abaixo, *a_list)
print(acumulador_acima, *b_list)
