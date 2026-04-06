# -----------------------------------------------------------
# Programa: Calculadora IEMB
# Descripcion: Calculadora basica en modo consola
# Autor: hhtorresn@manuelabeltransoacha.edu.co
# -----------------------------------------------------------
# Mensaje de bienvenida
print("=======================================")
print("Bienvenido al programa Calculadora IEMB")
print("=======================================")
# Solicitar nombre del usuario
nombre = input("Ingrese su nombre: ")
# Solicitar los numeros al usuario
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
# Operaciones aritmeticas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
# Validar que el segundo numero no sea cero para la division
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero"
# Mostrar resultados
print("\n----------------------------------")
print("Datos registrados")
print("----------------------------------")
print("Nombre del usuario:", nombre)
print("Numero 1:", numero1)
print("Numero 2:", numero2)
print("\nResultados de las operaciones:")
print("Suma:", numero1, "+", numero2, "=", suma)
print("Resta:", numero1, "-", numero2, "=", resta)
print("Multiplicacion:", numero1, "*", numero2, "=", multiplicacion)
print("Division:", numero1, "/", numero2, "=", division)
# Mensaje final
print("\nGracias por utilizar este software,", nombre)
print("Desarrollado por: hhtorresn@manuelabeltransoacha.edu.co")