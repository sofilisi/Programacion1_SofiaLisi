def mostrar_atracciones():
    print("Menú de atracciones:")
    print("1. Montaña Rusa")
    print("2. Casa del Terror")
    print("3. Carrusel")
    print("4. Rueda de la Fortuna")

def puede_subir(edad, atraccion):
    if atraccion == "Montaña Rusa":
        return edad >= 12
    elif atraccion == "Casa del Terror" or atraccion == "Carrusel" or atraccion == "Rueda de la Fortuna":
        return edad >= 6
    else:
        return False
    
def calcular_precio(atraccion):
    if atraccion == "Montaña Rusa":
        return 500
    elif atraccion == "Casa del Terror":
        return 400
    elif atraccion == "Carrusel":
        return 300
    elif atraccion == "Rueda de la Fortuna":
        return 350
    else:
        return 0
    
def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    
    mostrar_atracciones()
    
    cantidad = int(input("¿Cuántas atracciones quiere visitar? "))
    
    elecciones = ""
    permitidas = ""
    costo_total = 0
    
    for i in range(1, cantidad + 1):
        atraccion = input(f"Ingrese la atracción {i}: ")
        elecciones += atraccion + " "
        if puede_subir(edad, atraccion):
            permitidas += atraccion + " "
            costo_total += calcular_precio(atraccion)

    # NUEVA FUNCIONALIDAD: descuento del 10% si compra 3 o más atracciones
    descuento = 0
    if cantidad >= 3:
        descuento = costo_total * 0.10
        costo_total -= descuento
    
    return (nombre, elecciones, permitidas, costo_total, descuento)
    
    

def mostrar_resumen(resumen):
    print(f"Resumen del visitante:")
    print(f"Nombre:", resumen[0])
    print(f"Atracciones elegidas:", resumen[1])
    print(f"Atracciones que puede usar:", resumen[2])
    print(f"Costo total a pagar:", resumen[3])
    print(f"Descuento aplicado:", resumen[4])