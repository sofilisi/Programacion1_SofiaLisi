def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def comparar_arrays(arr1: list[int], arr2: list[int]) -> bool:
    return arr1 == arr2

def ejercicio8():
    print("Cargar primer array:")
    arr1 = cargar_array(5)
    print("Cargar segundo array:")
    arr2 = cargar_array(5)
    if comparar_arrays(arr1, arr2):
        print("Los arrays son iguales")
    else:
        print("Los arrays son distintos")