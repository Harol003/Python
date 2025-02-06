# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: OOP - Todos los pilares juntos")

from abc import ABC, abstractmethod

# Clase abstracta para animales (Abstracción)
class Animal(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado (Encapsulamiento)

    @abstractmethod
    def hacer_sonido(self):
        pass

    def get_nombre(self):
        return self.__nombre

# Clase derivada de Animal (Herencia)
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Función polimórfica
def hacer_interaccion(animal):
    print(f"{animal.get_nombre()} dice: {animal.hacer_sonido()}")

# Instanciar objetos
perro = Perro("Max")
gato = Gato("Felix")

# Polimorfismo: Diferentes implementaciones de hacer_sonido(), pero la misma función hacer_interaccion
hacer_interaccion(perro)  # Salida: Max dice: Guau
hacer_interaccion(gato)   # Salida: Felix dice: Miau
