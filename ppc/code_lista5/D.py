M = int(input())
A = int(input())
B = int(input())
velho = M - A - B
if (velho >= A) and (velho >= B):
    print(velho)
elif (A >= velho ) and (A >= B):
    print(A)
elif (B >= velho) and (B >= A):
    print(B)
