# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Encapsulamiento")

class Goku:
    def __init__(self, poder, energia):
        self.__poder = poder  # Atributo privado
        self.__energia = energia  # Atributo privado

    # Métodos para acceder y modificar atributos privados
    def get_poder(self):
        return self.__poder

    def set_poder(self, poder):
        self.__poder = poder

    def get_energia(self):
        return self.__energia

    def set_energia(self, energia):
        if energia >= 0:  # Aseguramos que la energía no sea negativa
            self.__energia = energia

# Crear un objeto de Goku
goku = Goku(5000, 100)

# Acceder y modificar los atributos a través de métodos
print(f"Poder de Goku: {goku.get_poder()}")
goku.set_poder(6000)
goku.set_energia(120)
print(f"Nuevo poder de Goku: {goku.get_poder()}, Nueva energía de Goku: {goku.get_energia()}")
