# Programa: Politecnico Internacional: Vocal o No Vocal
# Descripcion: Captura un caracter e identifica si es una vocal o no.

# Funcion principal del programa
def main():
    # Solicitar al usuario que ingrese un caracter
    caracter = input("Ingrese un caracter: ").lower()
    
    # Verificar si es una sola letra
    if len(caracter) != 1 or not caracter.isalpha():
        print("Error: Ingrese un solo caracter alfabetico.")
        return
    
    # Definir si es una vocal o no
    if caracter in "aeiou":
        print(f"El caracter capturado es: Vocal")
        print("El caracter ingresado es una Vocal")
    else:
        print(f"El caracter capturado es: No Vocal")
        print("El caracter ingresado NO es una Vocal")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()
