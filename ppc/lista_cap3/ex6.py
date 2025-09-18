# Escreva um programa que leia duas notas e mostre a média obtida a partir das
# mesmas, de acordo com as regras do IFRN. Para obter a média use a seguinte
# fórmula:

# media = (nota1 × 2 + nota2 × 3) ÷ 5
# No IFRN as notas são valores inteiros entre 0 e 100

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

media = (n1 * 2) + (n2 * 3) / 5

print('A média é:',media)