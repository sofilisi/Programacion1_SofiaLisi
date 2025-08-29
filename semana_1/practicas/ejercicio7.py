#7.Función verificar_acceso
def verificar_acceso(edad):
    return edad >= 18

edad_usuario = int(input("Ingresa tu edad: "))
if verificar_acceso(edad_usuario):
    print("Eres mayor de edad, acceso permitido")
else:
    print("No eres mayor de edad, acceso denegado")