# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Ejemplo básico de Álgebra de Boole con AND
# Definimos una función simple para verificar si un número es positivo y par

def es_positivo_y_par(numero):
    """
    Función que verifica si un número es positivo y par.
    Parámetros:
    - numero (int): Número a evaluar.
    Retorna:
    - bool: True si es positivo y par, False en caso contrario.
    """
    return numero > 0 and numero % 2 == 0  # Debe ser mayor que 0 y divisible por 2

# Pruebas de la función
print("Pruebas de la función es_positivo_y_par:")
print("Número: 4 ->", es_positivo_y_par(4))  # True, es positivo y par
print("Número: -2 ->", es_positivo_y_par(-2))  # False, es par pero negativo
print("Número: 3 ->", es_positivo_y_par(3))  # False, es positivo pero impar
print("Número: 0 ->", es_positivo_y_par(0))  # False, no es positivo

# Interpretación del código:
# El operador lógico AND requiere que ambas condiciones sean verdaderas.
# Si una de ellas es falsa, la salida será False.
