def conta_bits(n):
    if (n <= 1):
        return 1
    else:
        return 1 + conta_bits(n // 2)

x = int(input("Digite um número inteiro: "))

print(f"A quantidade de bits necessários para o numero: {x} é {conta_bits(x)}")