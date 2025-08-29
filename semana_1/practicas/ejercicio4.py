#4.Función buscar_mayor
def buscar_mayor(a, b, c):
    mayor = max(a, b, c)
    menor = min(a, b, c)
    medio = a + b + c - mayor - menor
    return [mayor, medio, menor]

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
print("Números ordenados de mayor a menor:", buscar_mayor(num1, num2, num3))
