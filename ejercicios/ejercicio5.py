def cargar_array(tamaño: int) -> list[int]:
    arr = []
    for i in range(tamaño):
        arr.append(int(input(f"Ingrese el entero {i+1}: ")))
    return arr

def buscar_valor(arr: list[int], valor: int) -> int:
    if valor in arr:
        return arr.index(valor)
    else:
        return -1

def ejercicio5():
    arr = cargar_array(10)
    valor = int(input("Ingrese el número a buscar: "))
    pos = buscar_valor(arr, valor)
    if pos == -1:
        print("No se encuentra en el array")
    else:
        print(f"Se encuentra en la posición {pos}")