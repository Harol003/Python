# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Herencia")

class Saiyajin:
    def __init__(self, nombre, nivel_poder):
        self.nombre = nombre
        self.nivel_poder = nivel_poder

    def transformar(self):
        return f"{self.nombre} se transforma en Super Saiyajin."

# Goku hereda de Saiyajin
class Goku(Saiyajin):
    def __init__(self, nombre, nivel_poder, energia):
        super().__init__(nombre, nivel_poder)
        self.energia = energia

    def transformar(self):
        return f"{self.nombre} se transforma en Super Saiyajin y aumenta su poder."

# Crear un objeto de Goku
goku = Goku("Goku", 5000, 100)
print(goku.transformar())  # Goku usa su transformación especial
