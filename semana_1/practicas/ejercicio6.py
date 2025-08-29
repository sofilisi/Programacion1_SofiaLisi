#6.convertir_minutos
def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobrantes = minutos % 60
    return horas, minutos_sobrantes

min_totales = int(input("Ingresa la cantidad de minutos: "))
h, m = convertir_minutos(min_totales)
print(f"{h} horas y {m} minutos")