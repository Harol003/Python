# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Herencia")

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase derivada
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.puertas = puertas

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Puertas: {self.puertas}"

# Crear una instancia de la clase Automovil
auto = Automovil("Toyota", "Corolla", 4)
print(auto.mostrar_informacion())
