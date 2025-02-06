import csv
import os

# Nombre del archivo CSV donde se guardarán los datos
ARCHIVO_CSV = "estudiantes.csv"
# Contraseña para acceder al módulo de profesor
CONTRASENA_PROFESOR = "politecnico"

# Función para inicializar el archivo CSV si no existe
def inicializar_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="") as file:
            csv.writer(file).writerow(["Nombre", "Nota1", "Nota2", "Nota3", "NotaFinal"])

# Función para cargar los datos del archivo CSV
def cargar_datos():
    with open(ARCHIVO_CSV, "r") as file:
        return list(csv.DictReader(file))

# Función para guardar los datos en el archivo CSV
def guardar_datos(datos):
    with open(ARCHIVO_CSV, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Nombre", "Nota1", "Nota2", "Nota3", "NotaFinal"])
        writer.writeheader()
        writer.writerows(datos)

# Función para calcular la nota final basada en los pesos asignados
def calcular_nota(n1, n2, n3):
    return (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)

# Función para validar que las notas ingresadas estén entre 0 y 5
def ingresar_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero}: "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Error: Ingrese un número válido.")

# Función para agregar un nuevo estudiante y sus notas
def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    notas = [ingresar_nota(i+1) for i in range(3)]
    datos = cargar_datos()
    datos.append({"Nombre": nombre, "Nota1": notas[0], "Nota2": notas[1], "Nota3": notas[2], "NotaFinal": calcular_nota(*notas)})
    guardar_datos(datos)
    print("Estudiante agregado exitosamente.")

# Función para ver el consolidado de calificaciones de todos los estudiantes
def ver_consolidado():
    datos = cargar_datos()
    if not datos:
        return print("No hay registros.")
    print("\nConsolidado de Calificaciones")
    for est in datos:
        print(f"{est['Nombre']} - {float(est['NotaFinal']):.2f}")

# Función para consultar las notas de un estudiante específico
def consultar_notas():
    nombre = input("Ingrese su nombre: ")
    for est in cargar_datos():
        if est["Nombre"].lower() == nombre.lower():
            return print(f"Notas: {est['Nota1']}, {est['Nota2']}, {est['Nota3']}, Final: {float(est['NotaFinal']):.2f}")
    print("Estudiante no encontrado.")

# Función para mostrar el menú del profesor
def menu_profesor():
    contrasena = input("Ingrese la contraseña del profesor: ")
    if contrasena != CONTRASENA_PROFESOR:
        print("Contraseña incorrecta.")
        return
    while (opcion := input("\n1. Agregar Estudiante\n2. Ver Consolidado\n3. Volver\nOpción: ")) != "3":
        {"1": agregar_estudiante, "2": ver_consolidado}.get(opcion, lambda: print("Opción inválida"))()

# Función principal para mostrar el menú general
def menu_principal():
    while True:
        print("\nBienvenido al sistema de gestión de notas del Politécnico Internacional")
        print("1. Profesor\n2. Estudiante\n3. Salir")
        match input("Opción: "):
            case "1": menu_profesor()
            case "2": consultar_notas()
            case "3":
                print("Gracias por usar el sistema del Politécnico Internacional. ¡Hasta pronto!")
                break
            case _: print("Opción inválida")

# Punto de entrada del programa
if __name__ == "__main__":
    inicializar_csv()
    menu_principal()
