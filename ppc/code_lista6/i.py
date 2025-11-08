def lista_troca_menor_primeiro(lista):
    elementos = 0
    for i in lista:
        elementos += 1
    if (lista[0] < lista[elementos]):
        troca = 1
    else:
        troca = 0
    
    return troca

entrada = list(map(int, input().split()))
resultado = lista_troca_menor_primeiro(entrada)
print(resultado)

# tentar fazer depois