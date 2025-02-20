# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Ejemplo básico de Álgebra de Boole con AND
# Verificar si un número es par y mayor a 10

def es_par_y_mayor_a_diez(numero):
    """
    Función que verifica si un número es par y mayor a 10.
    Parámetros:
    - numero (int): Número a evaluar.
    Retorna:
    - bool: True si cumple ambas condiciones, False en caso contrario.
    """
    return numero % 2 == 0 and numero > 10  # Debe ser par y mayor que 10

# Pruebas de la función
print("Pruebas de la función es_par_y_mayor_a_diez:")
print("Número: 12 ->", es_par_y_mayor_a_diez(12))  # True, es par y mayor a 10
print("Número: 8 ->", es_par_y_mayor_a_diez(8))  # False, es par pero menor o igual a 10
print("Número: 15 ->", es_par_y_mayor_a_diez(15))  # False, es mayor a 10 pero impar
print("Número: 10 ->", es_par_y_mayor_a_diez(10))  # False, es par pero no mayor a 10

# Interpretación del código:
# El operador lógico AND requiere que ambas condiciones sean verdaderas.
# Si una de ellas es falsa, la salida será False.