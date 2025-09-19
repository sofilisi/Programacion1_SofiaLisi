def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def invertir_array(arr: list[int]) -> list[int]:
    return arr[::-1]

def ejercicio7():
    arr = cargar_array(6)
    print("Array invertido:", invertir_array(arr))