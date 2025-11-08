def dia(dia, mes, ano):
    bool_date = True
    meses = ['janeiro', 'fevereiro', ' marco', 'abril', 'maio', 'junho', 'julho',
              'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    
    if (mes < 1) or (mes > 12):
        bool_date = False

    if bool_date:
        if (mes == 2) and ((dia < 1) or (dia > 28)): 
            bool_date = False
        
        elif (mes in [4, 6, 9, 11]) and ((dia < 1) or (dia > 30)):
            bool_date = False
    
    if bool_date:
        mes = meses[mes - 1]
        data = f'{dia:02d} de {mes} de {ano}'
    else:
        return 'Data Invalida'
    return data

print(dia(1, 1, 901))
print(dia(22, 4, 1500))
print(dia(15, 11, 1889))
print(dia(32, 5, 2018))