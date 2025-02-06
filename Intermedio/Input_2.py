# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional") 
print("Asignatura: Algoritmos 2")
print("Tema: Input")

# Capturar datos usando un diccionario
datos_usuario = {}
datos_usuario["nombre"] = input("Ingrese su nombre: ")  # Captura el nombre del usuario
datos_usuario["edad"] = input("Ingrese su edad: ")  # Captura la edad del usuario
datos_usuario["correo"] = input("Ingrese su correo electronico: ")  # Captura el correo electronico del usuario

# Mostrar los datos ingresados por el usuario
print("\nDatos ingresados:")
for clave, valor in datos_usuario.items():
    print(f"{clave.capitalize()}: {valor}")
