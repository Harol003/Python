# -----------------------------------------------------------
# Programa: Programa IEMB
# Descripcion: Ejemplo de programa en Python que trabaja en
# consola utilizando conceptos basicos del lenguaje.
# Incluye: variables, input, operaciones, listas y condicionales.
# -----------------------------------------------------------

# Mostrar titulo del programa
print("===================================")
print("        PROGRAMA IEMB")
print("Institucion Educativa Manuela Beltran")
print("===================================")

# Solicitar el nombre del usuario utilizando input
nombre_usuario = input("Ingrese su nombre: ")

# Mostrar saludo utilizando la variable
print("Hola", nombre_usuario, "bienvenido al programa.")

# -----------------------------------------------------------
# Ejemplo 1: Operaciones matematicas basicas
# -----------------------------------------------------------

# Solicitar dos numeros al usuario
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

# Realizar una operacion de suma
suma = numero1 + numero2

# Mostrar el resultado
print("La suma de los numeros es:", suma)

# -----------------------------------------------------------
# Ejemplo 2: Uso de condicionales
# -----------------------------------------------------------

# Verificar si el resultado es mayor que 10
if suma > 10:
    print("El resultado es mayor que 10")
else:
    print("El resultado es menor o igual a 10")

# -----------------------------------------------------------
# Ejemplo 3: Uso de listas
# -----------------------------------------------------------

# Crear una lista para guardar tres numeros
numeros = []

# Pedir tres numeros y agregarlos a la lista
for i in range(3):
    dato = int(input("Ingrese un numero para la lista: "))
    numeros.append(dato)  # Agregar el numero a la lista

# Mostrar los numeros guardados en la lista
print("Los numeros almacenados en la lista son:", numeros)

# Calcular la suma de los numeros de la lista
suma_lista = sum(numeros)

# Mostrar resultado
print("La suma de los numeros de la lista es:", suma_lista)

# -----------------------------------------------------------
# Mensaje final del programa
# -----------------------------------------------------------

print("-----------------------------------")
print("Gracias por usar este software", nombre_usuario)
print("Desarrollado por hhtorresn@manuelabeltransoacha.edu.co")
print("-----------------------------------")