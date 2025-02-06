# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Listas con Condiciones")

# Lista de números
numeros = [10, 20, 30, 40, 50, 60, 70]

# Filtrar números mayores a 30 utilizando una condición
numeros_mayores = [num for num in numeros if num > 30]
print("Números mayores a 30:", numeros_mayores)

# Filtrar números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)
