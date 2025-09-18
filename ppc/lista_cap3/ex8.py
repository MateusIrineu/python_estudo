# Escreva um programa que leia a hora de início e de fim de um evento e mostre
# o tempo do evento no formato HH:MM. A hora de início e fim é dada em minutos
# desde o início do dia.

inicio = int(input('Informe o tempo de início: '))
fim = int(input('Informe o tempo de término: '))

hora = 60

h = (fim - inicio) // hora

m = (fim - inicio) % hora

print('Duração:',h,':',m, sep='')