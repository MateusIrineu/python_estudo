# Escreva um programa que leia a distância entre duas cidades A e B, em kilômetros, a velocidade, em km/h, do carro e mostre qual o tempo da viagem entre A e B, no formato HH:MM.
# Os segundos devem ser desprezados.

# Input
# A entrada é composta de 2 linhas. A primeira linha contém um inteiro representando a distância D (1 ≤ D ≤ 1000) entras as cidades. 
# A segunda também contém um número inteiro V (1 ≤ V ≤ 250), que representa a velocidade em km/h.

# Output
# Seu programa deve mostrar uma única linha com o tempo de deslocamento no formato HH:MM. Os segundos devem ser desprezados.

distancia = int(input())
velocidade = int(input())
horas_inteiras = distancia // velocidade
horas = distancia / velocidade
minutos = int((horas - horas_inteiras) * 60)
print(f'{horas_inteiras:02d}:{minutos:02d}')
