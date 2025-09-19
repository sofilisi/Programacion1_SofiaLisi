def cargar_array_float(tamaño: int) -> list[float]:
    arr = []
    for i in range(tamaño):
        arr.append(float(input(f"Ingrese el número {i+1}: ")))
    return arr

def promedio(arr: list[float]) -> float:
    return sum(arr) / len(arr)

def ejercicio3():
    arr = cargar_array_float(6)
    print("El promedio es:", promedio(arr))