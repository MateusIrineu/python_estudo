def media_lista(lista):
    soma = 0
    elementos = 0
    for numero in lista:
        soma += numero # vai iterando
        elementos += 1 # vai aumentando o tamanho da list
    media = soma // elementos
    return media

entrada = list(map(int, input().split()))
resultado = media_lista(entrada) # entrada se torna o parâmetro lista
print(resultado)