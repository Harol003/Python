# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Manejo de Errores")

# Intentamos dividir entre cero, lo cual generaría un error
try:
    numero = 10 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
