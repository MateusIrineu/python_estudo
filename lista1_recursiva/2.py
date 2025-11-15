def primo_r(n, d):
    if (d == 1):
        return True
    if (n % d == 0):
        return False
    else:
        return primo_r(n, d-1)

def primo(n):
    if (n <= 1):
        return "Não é primo"
    resultado = primo_r(n, n-1)

    if (resultado):
        return "Primo"
    else:
        return "Não é primo"

x = int(input("Valor: "))

print(f"O número {x} {primo(x)}")