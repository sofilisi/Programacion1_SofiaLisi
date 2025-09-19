def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def sumar_elementos(arr: list[int]) -> int:
    return sum(arr)

def ejercicio2():
    arr = cargar_array(10)
    print("La suma es:", sumar_elementos(arr))