def media_ponderada(v1, p1, v2, p2):
    media = ((v1 * p1) + (v2 * p2)) / (p1 + p2)
    return media

print(media_ponderada(10, 2, 20, 3))
print(media_ponderada(54, 9, 65, 10))