def conta_divisores_r(n, d):
    if d == 0:
        return 0
    
    divisores = conta_divisores_r(n, d - 1)
    
    if (n % d == 0):
           total = 1 + divisores
           return total
    else:
         n % d != 0
         return divisores
    
def conta_divisores(n):
    return conta_divisores_r(n, n)

print(conta_divisores(6))