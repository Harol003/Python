# Programa: Politecnico Internacional: Calculadora
# Descripcion: Simula el funcionamiento de una calculadora basica con operaciones matematicas.

# Funcion para mostrar el menu
def mostrar_menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Porcentaje")
    print("6. Potenciar")
    print("7. Salir")

# Funcion principal del programa
def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: Ingrese un numero valido.")
            continue
        
        if opcion in [1, 2, 3, 4, 5, 6]:
            try:
                num1 = float(input("Ingrese el primer numero: "))
                num2 = float(input("Ingrese el segundo numero: "))
                
                if opcion == 1:
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif opcion == 2:
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif opcion == 3:
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif opcion == 4:
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir por cero.")
                elif opcion == 5:
                    print(f"Resultado: {num1} % de {num2} = {(num1 / 100) * num2}")
                elif opcion == 6:
                    print(f"Resultado: {num1} ^ {num2} = {num1 ** num2}")
                
            except ValueError:
                print("Error: Ingrese valores numericos validos.")
        
        elif opcion == 7:
            print("Gracias por usar la Calculadora. Hasta luego!")
            break
        
        else:
            print("Error: Opcion no valida, intente de nuevo.")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()
