# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: OOP - Todos los pilares con Goku")

from abc import ABC, abstractmethod

# Clase abstracta
class Guerrero(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado (Encapsulamiento)

    @abstractmethod
    def atacar(self):
        pass  # Método abstracto

    def get_nombre(self):
        return self.__nombre

# Clases derivadas
class Goku(Guerrero):
    def atacar(self):
        return "Kamehameha"

class Vegeta(Guerrero):
    def atacar(self):
        return "Final Flash"

# Función polimórfica
def realizar_ataque(guerrero):
    print(f"{guerrero.get_nombre()} ataca con: {guerrero.atacar()}")

# Crear instancias
goku = Goku("Goku")
vegeta = Vegeta("Vegeta")

# Polimorfismo y herencia en acción
realizar_ataque(goku)    # Goku ataca con: Kamehameha
realizar_ataque(vegeta)  # Vegeta ataca con: Final Flash
