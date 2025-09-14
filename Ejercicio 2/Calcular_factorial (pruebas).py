def calcular_factorial(n):
    n = int(n)
    if n == 0:
        return 1
    else:
        if n < 0:
            return "El factorial de un numero negativo no existe"
        else:
            for i in range(n - 1, 0, -1):
                n = n * i
            return n

print(calcular_factorial(input("Introduzca el numero para calcular el factorial\n")))

# ============ 
# Unit tests   
# ============ 

# Caso 1: factorial de 0
assert calcular_factorial(0) == 1

# Caso 2: factorial positivo
assert calcular_factorial(5) == 120

# Caso 3: número negativo
assert calcular_factorial(-3) == "El factorial de un numero negativo no existe"

# Caso 4: factorial de 1
assert calcular_factorial(1) == 1

print("Todas las pruebas pasaron correctamente.")
