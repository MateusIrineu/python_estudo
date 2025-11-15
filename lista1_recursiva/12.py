def ocorrencias(lista, x):
    if (len(lista) == 0):
        return 0
    if (len(lista) == 1):
        if (lista[0] == x):
            return 1
        else:
            return 0
          
    elemento = lista[-1]

    if (elemento == x):
        return 1 + ocorrencias(lista[:-1], x)
    else:
        return ocorrencias(lista[:-1], x)
    