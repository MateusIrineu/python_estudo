A = int(input())
B = int(input())
C = int(input())
distAB = B - A
distBC = C - B
if (distAB < distBC):
    print(1)
elif (distAB == distBC):
    print(0)
elif (distAB > distBC):
    print(-1)