# Programa: Politecnico Internacional: Operaciones Matematicas
# Descripcion: Captura dos numeros e imprime la suma, resta, multiplicacion y division.

# Funcion principal del programa
def main():
    # Solicitar al usuario que ingrese dos numeros
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Error: Ingrese valores numericos validos.")
        return

    # Realizar las operaciones matematicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    # Verificar que el segundo numero no sea cero antes de dividir
    if num2 != 0:
        division = num1 / num2
    else:
        division = "No se puede dividir por cero"
    
    # Mostrar los resultados
    print("\nResultados:")
    print(f"1. Suma: {num1} + {num2} = {suma}")
    print(f"2. Resta: {num1} - {num2} = {resta}")
    print(f"3. Multiplicacion: {num1} * {num2} = {multiplicacion}")
    print(f"4. Division: {division}")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()
