# Mostrar el nombre, asignatura y tema
print("Nombre: Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Manejo de Archivos")

# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Podemos escribir varias líneas.\n")

# Leer desde un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
