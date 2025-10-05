a, g, ra, rg = map(float, input().split())
test_a = ra / a
test_g = rg / g
if ( test_g >= test_a):
    print('G')
else:
    print('A')
