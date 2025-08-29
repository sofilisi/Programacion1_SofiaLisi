#8. Función calcular_edad
def calcular_edad(año_nacimiento):
    año_actual = 2025  
    return año_actual - año_nacimiento

año = int(input("Ingresa tu año de nacimiento: "))
print(f"Tienes {calcular_edad(año)} años")