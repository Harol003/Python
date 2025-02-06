# Mostrar el nombre, asignatura y tema
print("Nombre: Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Abstracción")

from abc import ABC, abstractmethod

class Guerrero(ABC):
    @abstractmethod
    def atacar(self):
        pass  # Método abstracto que debe ser implementado por clases hijas

class Goku(Guerrero):
    def atacar(self):
        return "Kamehameha"

class Vegeta(Guerrero):
    def atacar(self):
        return "Final Flash"

# Crear instancias de las clases
goku = Goku()
vegeta = Vegeta()

# Abstracción: los detalles internos del ataque son ocultos, solo sabemos el nombre del ataque
print(f"Goku ataca con: {goku.atacar()}")
print(f"Vegeta ataca con: {vegeta.atacar()}")
