a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
total_a = a1 - a2
total_b = b1 - b2
total_c = c1 - c2
if (total_a < 0 and total_b < 0 and total_c < 0):
    print(abs(total_a + total_b + total_c))
elif ((total_a > 0 and total_b < 0 and total_c < 0)):
    print(abs(total_b + total_c))
elif (total_a > 0 and total_b > 0 and total_c < 0):
    print(abs(total_c))
else:
    print(0)