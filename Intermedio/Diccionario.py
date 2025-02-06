# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Diccionarios")

# Crear un diccionario con información clave-valor
persona = {
    "nombre": "Harol",
    "edad": 40,
    "ciudad": "Soacha"
}

# Acceder a los valores mediante las claves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# Agregar un nuevo par clave-valor
persona["profesion"] = "Profesor"
print("Profesión:", persona["profesion"])
