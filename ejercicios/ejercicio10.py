def buscar_primera_aparicion(arr: list[int], valor: int) -> int:
    try:
        return arr.index(valor)
    except ValueError:
        return -1

def ejercicio10():
    arr = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
    valor = int(input("Número a buscar: "))
    pos = buscar_primera_aparicion(arr, valor)
    if pos == -1:
        print("No se encuentra")
    else:
        print(f"Se encuentra en la posición {pos}")