# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Encapsulamiento")

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Métodos para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad

# Crear un objeto de la clase Persona
persona = Persona("Harol", 40)

# Acceder y modificar los atributos a través de métodos
print(f"Nombre: {persona.get_nombre()}, Edad: {persona.get_edad()}")
persona.set_nombre("Adriana")
persona.set_edad(34)
print(f"Nombre: {persona.get_nombre()}, Edad: {persona.get_edad()}")
