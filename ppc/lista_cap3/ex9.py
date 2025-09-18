# Escreva um programa que leia a quantidade de dias desde o início do ano e
# mostre quantas semanas e quantos dias já se passaram desde do dia primeiro
# de janeiro.

dias_passados = int(input('Informe a quantidade de dias: '))

semanas = dias_passados // 7

dias = dias_passados % 7

print('Se passaram:',semanas,'semanas e',dias,'dias')