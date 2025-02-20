# Nombre del programa: Politecnico Internacional
print("\Politecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Definicion de la clase Moto
class Moto:
    """Clase que representa una motocicleta."""
    
    # Constructor de la clase (metodo especial __init__)
    def __init__(self, marca, modelo, cilindrada, tipo):
        """
        Constructor de la clase Moto.
        Atributos:
        - marca (str): Marca de la moto
        - modelo (str): Modelo de la moto
        - cilindrada (int): Cilindrada de la moto en cc
        - tipo (str): Tipo de moto (ej. deportiva, cruiser, naked, etc.)
        """
        self.marca = marca  # Atributo de la marca de la moto
        self.modelo = modelo  # Atributo del modelo de la moto
        self.cilindrada = cilindrada  # Atributo de la cilindrada de la moto
        self.tipo = tipo  # Atributo del tipo de moto
    
    # Metodo para mostrar la informacion de la moto
    def mostrar_info(self):
        """Metodo que muestra la informacion de la moto."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}cc, Tipo: {self.tipo}")

# Creacion de instancias de la clase Moto
moto1 = Moto("Yamaha", "R1", 1000, "Deportiva")
moto2 = Moto("Honda", "CB500F", 500, "Naked")
moto3 = Moto("Harley-Davidson", "Iron 883", 883, "Cruiser")

# Uso del metodo mostrar_info para cada moto
moto1.mostrar_info()
moto2.mostrar_info()
moto3.mostrar_info()