# Escreva um programa que leia o valor de um item a venda, a quantidade de
# itens que você vai comprar e o valor que você tem para pagar. Todos os valores
# são inteiros. O programa deve então informar o valor total a ser pago e o valor
# do troco que você vai receber.

item = input('Digite o item que você deseja: ')
item_quantidade = int(input('Digite a quantidade de itens que você deseja: '))
valor = 5 * item_quantidade

print('Você deseja comprar ',item_quantidade,' quantidades de ',item,'. O total a ser pago: ',valor,' reais. Troco para quanto?', sep='')

reais = int(input('Digite o valor em reais para calcular o troco: '))
troco = reais - valor

print('Esse é o seu troco: ',troco,' reais', sep='')