# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Bucle for con range()")

# Usar range() para repetir una acción varias veces
for i in range(1, 6):  # range(1, 6) genera los números 1, 2, 3, 4, 5
    print(f"Contador: {i}")

# También se puede usar el paso en range() para contar de 2 en 2
for i in range(0, 10, 2):  # Genera los números 0, 2, 4, 6, 8
    print(f"Número par: {i}")
