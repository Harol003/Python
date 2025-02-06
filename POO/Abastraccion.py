# Mostrar el nombre, asignatura y tema
print("Nombre: Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Abstracción")

from abc import ABC, abstractmethod

# Definir una clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # Método abstracto, debe ser implementado por clases hijas

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de clases derivadas
perro = Perro()
gato = Gato()

# Abstracción: No necesitamos saber los detalles internos de cada clase
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())   # Salida: Miau
