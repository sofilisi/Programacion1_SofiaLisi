#5.Función es_par
def es_par(numero):
    return numero % 2 == 0

num = int(input("Ingresa un número: "))
if es_par(num):
    print("El número es par")
else:
    print("El número es impar")