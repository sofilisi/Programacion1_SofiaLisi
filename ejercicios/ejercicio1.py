def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def mostrar_array(arr: list[int]) -> None:
    print("Contenido del array:")
    for n in arr:
        print(n)

def ejercicio1():
    arr = cargar_array(5)
    mostrar_array(arr)