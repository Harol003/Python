# Programa: Politecnico Internacional: Calculo de Promedio
# Descripcion: Captura el nombre de un estudiante y tres notas para calcular su promedio.

# Funcion principal del programa
def main():
    # Solicitar el nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Capturar las tres notas con validacion de entrada
    try:
        nota_matematicas = float(input("Ingrese la nota de Matematicas: "))
        nota_espanol = float(input("Ingrese la nota de Espanol: "))
        nota_sociales = float(input("Ingrese la nota de Sociales: "))
    except ValueError:
        print("Error: Ingrese valores numericos validos para las notas.")
        return
    
    # Calcular el promedio
    promedio = (nota_matematicas + nota_espanol + nota_sociales) / 3
    
    # Mostrar el resultado
    print("\nResultados:")
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()
