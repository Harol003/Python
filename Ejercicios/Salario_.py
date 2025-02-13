# Programa: Politecnico Internacional: Calculo de Sueldo
# Descripcion: Captura el nombre de un empleado, las horas trabajadas y el valor por hora para calcular su sueldo.

# Funcion principal del programa
def main():
    # Solicitar el nombre del empleado
    nombre = input("Ingrese el nombre del empleado: ")
    
    # Capturar las horas trabajadas y el valor por hora con validacion de entrada
    try:
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        valor_por_hora = float(input("Ingrese el valor por hora: "))
    except ValueError:
        print("Error: Ingrese valores numericos validos.")
        return
    
    # Calcular el sueldo
    sueldo = horas_trabajadas * valor_por_hora
    
    # Mostrar el resultado
    print("\nResultados:")
    print(f"Señor usuario, usted trabajo {horas_trabajadas} horas.")
    print(f"Señor usuario, el valor por hora es {valor_por_hora}.")
    print(f"Su sueldo es: {sueldo:.2f}")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()
