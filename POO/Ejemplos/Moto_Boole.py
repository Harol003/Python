# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Ejemplo básico de Álgebra de Boole con AND
# Definimos una función que verifica si un usuario puede conducir

def puede_conducir(edad, tiene_licencia):
    """
    Función que evalúa si una persona puede conducir.
    Se basa en el operador lógico AND.
    Parámetros:
    - edad (int): Edad de la persona.
    - tiene_licencia (bool): Indica si la persona tiene licencia de conducir.
    Retorna:
    - bool: True si puede conducir, False en caso contrario.
    """
    return edad >= 18 and tiene_licencia  # Ambas condiciones deben ser verdaderas

# Pruebas de la función
print("Pruebas de la función puede_conducir:")
print("Edad: 20, Tiene licencia: True ->", puede_conducir(20, True))  # True, cumple ambas condiciones
print("Edad: 16, Tiene licencia: True ->", puede_conducir(16, True))  # False, edad insuficiente
print("Edad: 25, Tiene licencia: False ->", puede_conducir(25, False))  # False, no tiene licencia
print("Edad: 18, Tiene licencia: True ->", puede_conducir(18, True))  # True, cumple ambas condiciones

# Interpretación del código:
# El operador lógico AND (y lógico) requiere que ambas condiciones sean verdaderas
# Si una de ellas es falsa, la salida será False.

# Ejemplo aplicado a motocicletas en un taller
class Moto:
    """Clase que representa una motocicleta."""
    
    def __init__(self, marca, modelo, cilindrada, tipo, en_reparacion):
        """
        Constructor de la clase Moto.
        Atributos:
        - marca (str): Marca de la moto
        - modelo (str): Modelo de la moto
        - cilindrada (int): Cilindrada de la moto en cc
        - tipo (str): Tipo de moto (ej. deportiva, cruiser, naked, etc.)
        - en_reparacion (bool): Indica si la moto está en reparación
        """
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.tipo = tipo
        self.en_reparacion = en_reparacion
    
    def puede_entregarse(self):
        """Método que indica si la moto puede ser entregada al cliente."""
        return not self.en_reparacion  # Se entrega si no está en reparación

# Creación de instancias de la clase Moto
moto1 = Moto("Yamaha", "R1", 1000, "Deportiva", False)
moto2 = Moto("Honda", "CB500F", 500, "Naked", True)

# Uso del método puede_entregarse para verificar si las motos pueden ser entregadas
print("\nEstado de las motocicletas en el taller:")
print(f"{moto1.marca} {moto1.modelo} puede ser entregada: {moto1.puede_entregarse()}")
print(f"{moto2.marca} {moto2.modelo} puede ser entregada: {moto2.puede_entregarse()}")