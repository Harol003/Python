# Nombre del programa: Politecnico Internacional
print("\nPolitecnico Internacional")
print("Clase: Programacion Orientada a Objetos\n")

# Ejemplo básico de Álgebra de Boole con AND
# Verificar si una persona puede entrar a un evento

def puede_entrar(edad, tiene_entrada):
    """
    Función que verifica si una persona puede entrar a un evento.
    Parámetros:
    - edad (int): Edad de la persona.
    - tiene_entrada (bool): Indica si tiene entrada.
    Retorna:
    - bool: True si cumple ambas condiciones, False en caso contrario.
    """
    return edad >= 18 and tiene_entrada  # Debe ser mayor o igual a 18 y tener entrada

# Pruebas de la función
print("Pruebas de la función puede_entrar:")
print("Edad: 20, Tiene entrada: True ->", puede_entrar(20, True))  # True, cumple ambas condiciones
print("Edad: 16, Tiene entrada: True ->", puede_entrar(16, True))  # False, edad insuficiente
print("Edad: 25, Tiene entrada: False ->", puede_entrar(25, False))  # False, no tiene entrada
print("Edad: 18, Tiene entrada: True ->", puede_entrar(18, True))  # True, cumple ambas condiciones

# Interpretación del código:
# El operador lógico AND requiere que ambas condiciones sean verdaderas.
# Si una de ellas es falsa, la salida será False.
