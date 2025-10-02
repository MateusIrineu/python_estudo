c, q = map(int, input().split())
if (c == 1):
    resultado = q * 4
elif (c == 2):
    resultado = q * 4.50
elif (c == 3):
    resultado = q * 5
elif(c == 4):
    resultado = q * 2
else:
    resultado = q * 1.5
print(f'Total: R$ {resultado:.2f}')