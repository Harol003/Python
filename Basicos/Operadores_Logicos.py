# Programa: IEMB | Operadores Logicos (Mejorado)
print("Bienvenido a IEMB | Evaluacion con Operadores Logicos")
# Entrada de datos
edad = int(input("Escribe tu edad: "))
nota = float(input("Escribe tu nota (0.0 a 5.0): "))
asistencia = int(input("Escribe tu asistencia (0 a 100): "))
# Operadores logicos
cumple_and = (edad >= 11) and (nota >= 3.5)
cumple_or = (nota >= 4.0) or (asistencia >= 80)
cumple_not = not (asistencia < 60)
# Salidas explicativas
print("\n--- RESULTADOS ---")
print("Condicion AND (edad >= 11 y nota >= 3.5):", cumple_and)
print("Esto significa que cumples ambas condiciones al mismo tiempo.\n")
print("Condicion OR (nota >= 4.0 o asistencia >= 80):", cumple_or)
print("Esto significa que cumples al menos una de las condiciones.\n")
print("Condicion NOT (no tener asistencia menor a 60):", cumple_not)
print("Esto significa que se invierte el resultado de una condicion.\n")
print("Gracias por usar el programa")