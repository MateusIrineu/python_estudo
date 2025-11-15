def ordenada(lista):
    if (len(lista) <= 1):
        return True
    
    if (lista[-1] > lista[-2]):
        return ordenada(lista[:-1])
    else:
        return False
    