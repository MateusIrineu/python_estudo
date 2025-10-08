charrete_numero1, distancia1, velocidade1 = map(int, input().split())
charrete_numero2, distancia2, velocidade2 = map(int, input().split())
resultado_dist1 = distancia1 / velocidade1
resultado_dist2 = distancia2 / velocidade2
if (resultado_dist1 < resultado_dist2):
    print(charrete_numero1)
else:
    print(charrete_numero2)