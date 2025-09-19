def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def mayor_y_posicion(arr: list[int]) -> tuple[int,int]:
    mayor = max(arr)
    pos = arr.index(mayor)
    return mayor, pos

def ejercicio6():
    arr = cargar_array(7)
    mayor, pos = mayor_y_posicion(arr)
    print(f"El mayor es {mayor} y está en la posición {pos}")