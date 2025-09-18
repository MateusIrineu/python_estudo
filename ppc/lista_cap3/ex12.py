# Escreva um programa que calcule a quantidade de postes a serem colocados
# em uma rua. O programa deve ler a distância do início ao fim da rua, em
# quilômetros e a distância entre dois (2) postes, em metros. Seu programa
# deve mostrar a quantidade de postes e a distância entre os dois últimos postes.
# Lembre-se que há sempre um poste no início da rua e outro no final. A distância
# entre cada par de postes é o valor, em metros, lido pelo programa, com exceção
# da distância entre os dois últimos postes da rua.

dist_inicio_fim = int(input('Insira o tamanho da rua: '))
dist_entre_postes = int(input('Insira a distância entre os postes: '))

dist_km = dist_inicio_fim // 1000 # dist em KM

total_postes = (dist_inicio_fim // dist_entre_postes) - dist_entre_postes

print('A rua tem um total de ',dist_km,' km, o total de postes é de ',total_postes,', e a distância entre os dois últimos postes é de: ',dist_entre_postes,' metros' sep='')