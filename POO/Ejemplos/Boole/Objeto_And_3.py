# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Ejemplo de Álgebra de Boole con AND usando una clase
class Numero:
    """
    Clase que representa un número y permite verificar si es par y mayor a 10.
    """
    def __init__(self, valor):
        """
        Constructor de la clase.
        Parámetros:
        - valor (int): Número a evaluar.
        """
        self.valor = valor  # Atributo de la clase

    def es_par_y_mayor_a_diez(self):
        """
        Método que verifica si el número es par y mayor a 10.
        Retorna:
        - bool: True si cumple ambas condiciones, False en caso contrario.
        """
        return self.valor % 2 == 0 and self.valor > 10

# Pruebas de la clase Numero
print("Pruebas de la clase Numero:")
n1 = Numero(12)
print("Número: 12 ->", n1.es_par_y_mayor_a_diez())  # True, es par y mayor a 10

n2 = Numero(8)
print("Número: 8 ->", n2.es_par_y_mayor_a_diez())  # False, es par pero menor o igual a 10

n3 = Numero(15)
print("Número: 15 ->", n3.es_par_y_mayor_a_diez())  # False, es mayor a 10 pero impar

n4 = Numero(10)
print("Número: 10 ->", n4.es_par_y_mayor_a_diez())  # False, es par pero no mayor a 10

# Interpretación del código:
# Se ha creado la clase Numero con un atributo 'valor'.
# El método 'es_par_y_mayor_a_diez' evalúa si el número es par y mayor que 10.
# Se crean instancias de la clase para probar su funcionamiento.
