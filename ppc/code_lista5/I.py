a = int(input())
b = int(input())
c = int(input())

if (a <= b and b <= c and a <= c) or (b <= a and a <= c and b <= c):
    menor = (a * 4) + (b * 2)
elif (a >= b and b >= c and a >= c) or (a >= c and c >= b and a >= b):
    menor = (c * 4) + (b * 2)
elif (a <= b and c <= a and c <= b) or (c <= b and a <= c and a <= b):
    menor = (c * 2) + (a * 2)

print(menor)