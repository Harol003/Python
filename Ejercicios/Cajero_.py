# Programa: Politecnico Internacional: Cajero Automatico
# Descripcion: Simula un cajero automatico con opciones para ingresar dinero, retirar dinero y mostrar saldo.

# Inicializar el saldo de la cuenta
saldo = 1000000

# Funcion para mostrar el menu
def mostrar_menu():
    print("\nCajero Automatico")
    print("1. Ingresar Dinero a la cuenta")
    print("2. Retirar Dinero de la cuenta")
    print("3. Mostrar Dinero de la cuenta")
    print("4. Salir")

# Funcion principal del programa
def main():
    global saldo
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: Ingrese un numero valido.")
            continue
        
        if opcion == 1:
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                if cantidad > 0:
                    saldo += cantidad
                    print(f"Se han ingresado ${cantidad:.2f} correctamente.")
                else:
                    print("Error: La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un valor numerico valido.")
        
        elif opcion == 2:
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                if 0 < cantidad <= saldo:
                    saldo -= cantidad
                    print(f"Se han retirado ${cantidad:.2f} correctamente.")
                elif cantidad > saldo:
                    print("Error: Fondos insuficientes.")
                else:
                    print("Error: La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un valor numerico valido.")
        
        elif opcion == 3:
            print(f"El saldo actual es: ${saldo:.2f}")
        
        elif opcion == 4:
            print("Gracias por usar el Cajero Automatico. Hasta luego!")
            break
        
        else:
            print("Error: Opcion no valida, intente de nuevo.")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()