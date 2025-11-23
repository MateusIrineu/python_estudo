n = int(input())


if n <= 1:
    print('Nao')
    exit() 
elif n == 2:
    print('Sim')
    exit() 
i = 3

while i * i <= n:
    if n % i == 0:
        print('Nao')
        exit() 
    i += 1

print('Sim')
