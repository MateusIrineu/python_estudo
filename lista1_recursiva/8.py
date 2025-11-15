def indice_do_maior(lista):
    if (len(lista) == 1):
        return 0
    
    maior = indice_do_maior(lista[:-1])
    ultimo = len(lista) - 1

    if (lista[ultimo] > lista[maior]):
        maior = len(lista) - 1
    return maior
