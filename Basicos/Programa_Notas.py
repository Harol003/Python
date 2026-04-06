# ============================================
# PROGRAMA: Registro de notas usando listas
# ============================================
# Mensaje de bienvenida
print("=====================================")
print("   BIENVENIDO AL SISTEMA DE NOTAS   ")
print("=====================================")
# Pedir nombre del estudiante (tipo str)
nombre = input("Ingrese el nombre del estudiante: ")
# Crear una lista vacia para guardar las notas
notas = []
# Pedir cuantas notas desea ingresar (tipo int)
cantidad = int(input("Cuantas notas desea ingresar? "))
# Ciclo para ingresar las notas
for i in range(cantidad):
    # Pedir cada nota (tipo float)
    nota = float(input(f"Ingrese la nota {i+1}: "))
    # Agregar la nota a la lista
    notas.append(nota)
# Calcular la suma de las notas
suma = sum(notas)
# Calcular el promedio
promedio = suma / cantidad
# Mostrar resultados
print("\n========== RESULTADOS ==========")
print("Estudiante:", nombre)
print("Notas ingresadas:", notas)  # Muestra la lista completa
print("Promedio final:", promedio)
# Mensaje final
print("=====================================")
print("Gracias por usar este software,", nombre)
print("=====================================")