def inveter_lista(lista):
    if (len(lista) == 1):
        return [lista[0]]
    return [lista[-1]] + inveter_lista(lista[:-1])
