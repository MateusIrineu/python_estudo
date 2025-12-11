senha = [9842]
digitos = []
while digitos != senha:
    digitos = list(map(int, input().split()))
    if (digitos == senha):
        break
    print('Senha Invalida!')
    
print('Acesso Permitido.')