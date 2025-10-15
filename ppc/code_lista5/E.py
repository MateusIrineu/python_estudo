consumo = int(input())
media_11_30 = 10
media_31_100 = 30
media_101 = 100
if (consumo <= 10):
    print(7)
elif (consumo >= 11 and consumo <= 30):
    print(((media_11_30 - consumo) * -1) + 7)
elif (consumo >= 31 and consumo <= 100):
    print((((media_31_100 - consumo) * -1) * 2) + 20 + 7)
elif (consumo >= 101):
    print((((media_101 - consumo) * -1) * 5) + 140 + 20 + 7)
