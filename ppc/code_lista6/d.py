def maior5(a, b, c, d, e):
    maior = a
    if (b > maior):
        maior = b
    if (c > maior):
        maior = c
    if (d > maior):
        maior = d
    if (e > maior):
        maior = e
    return maior

print(maior5(10, 40, -80, 120, -160))