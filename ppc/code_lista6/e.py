def dia_da_semana(h, d):
    semana = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    hoje = semana.index(h)
    resto_semana = (hoje + d) % 7
    resultado = semana[resto_semana]
    return resultado

print(dia_da_semana("Domingo", 10))
print(dia_da_semana("Sabado", 21))
print(dia_da_semana("Quarta-feira", 30))