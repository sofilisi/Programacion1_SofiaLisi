def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def contar_mayores(arr: list[int], valor: int) -> int:
    return sum(1 for n in arr if n > valor)

def ejercicio4():
    arr = cargar_array(8)
    print("Cantidad mayores a 100:", contar_mayores(arr, 100))