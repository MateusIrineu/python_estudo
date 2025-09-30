n = int(input())

a = n // 100
resto = n - a * 100
b = resto // 50
resto = resto - b * 50
c = resto // 20
resto = resto - c * 20
d = resto // 10
resto = resto - d * 10
e = resto // 5
resto = resto - e * 5
f = resto // 2
resto = resto - f * 2
g = resto // 1

print(n)
print(f'{a} nota(s) de R$ 100,00')
print(f'{b} nota(s) de R$ 50,00')
print(f'{c} nota(s) de R$ 20,00')
print(f'{d} nota(s) de R$ 10,00')
print(f'{e} nota(s) de R$ 5,00')
print(f'{f} nota(s) de R$ 2,00')
print(f'{g} nota(s) de R$ 1,00')
