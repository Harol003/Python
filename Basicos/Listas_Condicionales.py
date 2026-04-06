# Programa: IEMB | Listas + Condicionales (Explicado)
# Mensaje de bienvenida
print("Bienvenido | Evaluacion de Notas")
# Creamos una lista vacia
# Aqui se van a guardar todas las notas que ingrese el usuario
notas = []
# Preguntamos cuantas notas desea ingresar
# Convertimos el dato a entero porque es un numero
n = int(input("Cuantas notas deseas ingresar: "))
# Usamos un ciclo para repetir el proceso varias veces
# Se repite segun la cantidad de notas que el usuario eligio
for i in range(n):
    # Pedimos una nota en cada repeticion
    # Convertimos a decimal (float) porque las notas pueden tener decimales
    nota = float(input("Ingresa la nota: "))
    # Guardamos la nota dentro de la lista
    notas.append(nota)
# Calculamos el promedio
# sum(notas) suma todos los valores de la lista
# len(notas) cuenta cuantas notas hay
promedio = sum(notas) / len(notas)
# Aqui usamos condicionales para tomar una decision
# Segun el valor del promedio, se asigna un resultado
if promedio >= 4.6:
    resultado = "Desempeno Superior"
elif promedio >= 4.0:
    resultado = "Desempeno Alto"
elif promedio >= 3.3:
    resultado = "Desempeno Basico"
else:
    resultado = "Desempeno Bajo"
# Mostramos los resultados al usuario
print("\n--- RESULTADOS ---")
# Mostramos todas las notas guardadas en la lista
print("Notas ingresadas:", notas)
# Mostramos el promedio calculado
print("Promedio:", promedio)
# Mostramos el nivel segun las condiciones
print("Nivel:", resultado)
# Mensaje final
print("Gracias por usar el programa")