#3. Función area_triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2

b = float(input("Ingresa la base del triángulo: "))
h = float(input("Ingresa la altura del triángulo: "))
print(f"El área del triángulo es: {area_triangulo (b, h) }")
