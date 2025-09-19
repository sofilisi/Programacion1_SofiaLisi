from ejercicios.ejercicio1 import ejercicio1
from ejercicios.ejercicio2 import ejercicio2
from ejercicios.ejercicio3 import ejercicio3
from ejercicios.ejercicio4 import ejercicio4
from ejercicios.ejercicio5 import ejercicio5
from ejercicios.ejercicio6 import ejercicio6
from ejercicios.ejercicio7 import ejercicio7
from ejercicios.ejercicio8 import ejercicio8
from ejercicios.ejercicio9 import ejercicio9
from ejercicios.ejercicio10 import ejercicio10

def mostrar_menu():
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Cargar y mostrar array")
    print("2. Sumar todos los elementos")
    print("3. Promedio de valores")
    print("4. Contar mayores a 100")
    print("5. Buscar un valor")
    print("6. Mayor y su posición")
    print("7. Invertir orden")
    print("8. Comparar dos arrays")
    print("9. Intercambiar pares por ceros")
    print("10. Buscar primera aparición")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "0":
        print("¡Chau! 👋")
        break
    else:
        print("Opción no válida, intentá de nuevo.")