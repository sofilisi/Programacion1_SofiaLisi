#1. 
#Ingreso de datos secuenciales 
# Pedir el nombre y edad de un visitante. 
# Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña 
#Rusa, Casa del Terror y Carrusel). 

nombre_visitante = input("ingrese su nombre:  ")
edad_visitante = int(input("ingrese su edad: "))

opcion_atraccion = input("ingrese su atraccion favorita: (montaña rusa, casa del terror o carrusel): ")

#2. Uso de condicionales 
# Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más). 
# Si el visitante tiene menos de 6 años, solo puede subir al Carrusel. 
# Los demás pueden acceder a todas las atracciones.
# > <

if edad_visitante >= 12:
    print("puede acceder a todas las atracciones (incluida la montaña rusa)")

elif edad_visitante < 6:
    print("solo puede acceder al carrusel")

else:
    print("puede acceder a la casa del terror y al carrusel")

#3. Uso de ciclos 
# Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según su edad. 
#○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror = 
#$1200, Carrusel = $800).

total_precios = 0

cantidad_atracciones = int(input("a cuantas atracciones quiere ingresar?  "))

precio_atraccion = {"montaña rusa": 1500, "casa del terror": 1200, "carrusel": 800}

for numero_atraccion in range (cantidad_atracciones):
    
    opcion_atraccion = input("ingrese su atraccion favorita: (montaña rusa, casa del terror o carrusel): ")

    if edad_visitante >= 12:
        print(f"Puede subir a {opcion_atraccion}")
        total_precios += precio_atraccion

    elif edad_visitante < 6:
        if opcion_atraccion == "carrusel":
            print(f"Puede subir a {opcion_atraccion}")
            total_precios += precio_atraccion

    else:
            print("No puede subir a esa atracción. Solo puede usar el carrusel.")
            
else:
        # Edad entre 6 y 11
        if opcion_atraccion == "casa del terror" or opcion_atraccion == "carrusel":
            print(f"Puede subir a {opcion_atraccion}")
            total_precios += precio_atraccion
        else:
            print("No puede subir a esa atracción. Solo puede usar la casa del terror y el carrusel.")

# Mostrar costo total
print(f"El costo total de las entradas es: ${total_precios}")
