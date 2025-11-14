
def divisores_r(n, d):
    if d == 1:
        divs = [1]
        return divs
    else:
        lista_divs = divisores_r(n, d - 1)
        if n % d == 0:
            lista_divs.append(d)
        return lista_divs
    
def divisores(n):
    return divisores_r(n, n)

print(divisores(6))