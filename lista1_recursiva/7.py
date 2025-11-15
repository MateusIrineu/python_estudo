
def divisores_r(n, k):
    if k == 1:
        divs = [1]
        return divs
    else:
        lista_divs = divisores_r(n, k - 1)
        if n % k == 0:
            lista_divs.append(k)
        return lista_divs
    
def divisores(n):
    return divisores_r(n, n)

print(divisores(6))