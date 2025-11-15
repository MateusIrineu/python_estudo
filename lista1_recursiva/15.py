def polinomio(coeficientes,x):
    if (len(coeficientes) == 1):
        return coeficientes[0]
    
    elemento = coeficientes[-1]
    p = x * polinomio(coeficientes[:-1], x) + elemento

    return p
