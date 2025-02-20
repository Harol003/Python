# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Definicion de la clase Automovil
class Automovil:
    """Clase que representa un automovil."""
    
    # Constructor de la clase (metodo especial __init__)
    def __init__(self, marca, modelo, color, velocidad_maxima):
        """
        Constructor de la clase Automovil.
        Atributos:
        - marca (str): Marca del automovil
        - modelo (str): Modelo del automovil
        - color (str): Color del automovil
        - velocidad_maxima (int): Velocidad maxima del automovil
        """
        self.marca = marca  # Atributo de la marca del auto
        self.modelo = modelo  # Atributo del modelo del auto
        self.color = color  # Atributo del color del auto
        self.velocidad_maxima = velocidad_maxima  # Atributo de la velocidad maxima
        self.velocidad_actual = 0  # Se inicializa en 0 km/h
    
    # Metodo para mostrar la informacion del automovil
    def mostrar_info(self):
        """Metodo que muestra la informacion del automovil."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad Maxima: {self.velocidad_maxima} km/h")
    
    # Metodo para acelerar el automovil
    def acelerar(self, velocidad):
        """Metodo que aumenta la velocidad del automovil."""
        if self.velocidad_actual + velocidad <= self.velocidad_maxima:
            self.velocidad_actual += velocidad
        else:
            self.velocidad_actual = self.velocidad_maxima
        print(f"El automovil ha acelerado. Velocidad actual: {self.velocidad_actual} km/h")
    
    # Metodo para frenar el automovil
    def frenar(self):
        """Metodo que detiene el automovil."""
        self.velocidad_actual = 0
        print("El automovil se ha detenido.")

# Captura de datos desde el usuario
marca = input("Ingrese la marca del automovil: ")
modelo = input("Ingrese el modelo del automovil: ")
color = input("Ingrese el color del automovil: ")
velocidad_maxima = int(input("Ingrese la velocidad maxima del automovil (km/h): "))

# Instanciacion del objeto Automovil con los datos ingresados
mi_auto = Automovil(marca, modelo, color, velocidad_maxima)

# Uso de los metodos de la clase
mi_auto.mostrar_info()
mi_auto.acelerar(int(input("Ingrese la velocidad para acelerar (km/h): ")))
mi_auto.frenar()