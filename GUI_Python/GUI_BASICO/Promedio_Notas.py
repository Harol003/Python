
# Importamos tkinter
import tkinter as tk

# Función para calcular el promedio
def calcular():
    # Capturamos las tres notas
    nota1 = float(caja1.get())
    nota2 = float(caja2.get())
    nota3 = float(caja3.get())

    # Calculamos el promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Verificamos si el estudiante aprobó
    if promedio >= 3.3:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    # Mostramos promedio y estado
    resultado.config(
        text=f"Promedio: {promedio:.2f}\n{estado}"
    )

# Creamos ventana
ventana = tk.Tk()
ventana.title("PROMEDIO DE NOTAS")
ventana.geometry("350x350")

# Título
tk.Label(ventana, text="CALCULAR PROMEDIO",
         font=("Arial", 16)).pack(pady=10)

# Entrada nota 1
tk.Label(ventana, text="Nota 1").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

# Entrada nota 2
tk.Label(ventana, text="Nota 2").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

# Entrada nota 3
tk.Label(ventana, text="Nota 3").pack()
caja3 = tk.Entry(ventana)
caja3.pack()

# Botón calcular
tk.Button(ventana, text="CALCULAR",
          command=calcular).pack(pady=15)

# Resultado final
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

# Ejecutar
ventana.mainloop()
