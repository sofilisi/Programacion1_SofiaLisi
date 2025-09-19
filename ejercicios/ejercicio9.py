def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def reemplazar_pares_por_ceros(arr: list[int]) -> list[int]:
    return [0 if n % 2 == 0 else n for n in arr]

def ejercicio9():
    arr = cargar_array(10)
    arr_resultante = reemplazar_pares_por_ceros(arr)
    print("Array resultante:", arr_resultante)