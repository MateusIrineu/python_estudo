c = int(input())
d = int(input())
t = int(input())
quantidade = (d / c) - t
if ( quantidade < 0 ):
    print(0.0)
else:
    print(f'{quantidade:.1f}')
