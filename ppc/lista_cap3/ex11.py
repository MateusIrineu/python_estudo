# Escreva um programa que leia a distância entre duas cidades A e B, em kilô-
# metros, a velocidade, em km/h, do carro e mostre qual o tempo da viagem entre
# A e B, no formato HH:MM. Os segundos devem ser desprezados.

dist1 = int(input('Digite em qual KM está a cidade A: '))
dist2 = int(input('Digite em qual KM está a cidade B: '))
velocidade = int(input('Digite a velocidade do carro: '))

dist_total = dist2 - dist1
h = dist_total // velocidade
m = dist_total % velocidade

print('O tempo de viagem entre a cidade A e B, numa velocidade de ',velocidade,' Km/h, é de ',h,'h:',m, sep='')