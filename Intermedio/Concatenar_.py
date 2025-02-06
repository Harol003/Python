# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Concatenación y Formato de Cadenas")

# Concatenación de cadenas
nombre = "Harol"
apellido = "Torres"
saludo = "Hola, " + nombre + " " + apellido
print(saludo)

# Uso de f-strings para formatear cadenas
edad = 40
mensaje = f"{nombre} tiene {edad} años."
print(mensaje)

# Uso de .format() para formatear cadenas
mensaje2 = "{} tiene {} años.".format(apellido, edad)
print(mensaje2)
