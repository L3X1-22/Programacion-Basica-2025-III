def ContarLista(Lista):
    positivos = 0
    negativos = 0
    ceros = 0
    for i in Lista:
        if i > 0:
            positivos = positivos +1
        elif i < 0:
            negativos = negativos +1
        else:
            ceros = ceros +1
    
    return [positivos, negativos, ceros, len(Lista)]

def ObtenerLista():
    Datos = int(input("Ingrese el tamaño de su lista: "))
    Lista = []

    for i in range(Datos):
        Lista.append(int(input(f"Ingrese el dato {i+1}:")))
    
    return Lista

def ImprimirResultados():
    Resultados = ContarLista(ObtenerLista())
    print(f"Cantidad de positivos: {Resultados[0]}\nCantidad de negativos: {Resultados[1]}\nCantidad de ceros: {Resultados[2]}\nCantidad total: {Resultados[3]}")

ImprimirResultados()

# ============ 
# Unit tests   
# ============ 

# Caso 1
assert ContarLista([1, -2, 0, 3, -4, 0]) == [2, 2, 2, 6]

# Caso 2
assert ContarLista([1, 2, 3, 4]) == [4, 0, 0, 4]

# Caso 3
assert ContarLista([-1, -2, -3]) == [0, 3, 0, 3]

# Caso 4
assert ContarLista([0, 0, 0]) == [0, 0, 3, 3]

print("Todas las pruebas pasaron correctamente.")