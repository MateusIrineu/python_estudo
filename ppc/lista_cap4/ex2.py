# Escreva um programa que calcule o valor de um salário após um reajuste. O
# programa deve ler da entrada padrão o valor atual do salário e percentual de
# reajuste como números reais. O program deve calcular o novo valor do salário
# e mostrar ambos: o valor atual e o novo valor após o reajuste salarial.

salario = float(input('Digite o seu salário: '))
percentual = float(input('Digite o percentual a ser adicionado ao salário: '))

transformando_cem = percentual / 100
percentagem_vezes_salario = transformando_cem * salario
novo_salario = salario + percentagem_vezes_salario

print(f'Seu novo salário é: {novo_salario:0.2f}')