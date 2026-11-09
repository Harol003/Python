
# Importamos tkinter
import tkinter as tk

# Función para calcular el área
def calcular_area():
    # Obtenemos la base y la altura
    base = float(caja_base.get())
    altura = float(caja_altura.get())

    # Fórmula del área del rectángulo
    area = base * altura

    # Mostramos el resultado
    resultado.config(text=f"Área: {area}")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("AREA DEL RECTANGULO")
ventana.geometry("350x300")

# Título
tk.Label(ventana, text="AREA DEL RECTANGULO",
         font=("Arial", 16)).pack(pady=10)

# Entrada de la base
tk.Label(ventana, text="Base").pack()
caja_base = tk.Entry(ventana)
caja_base.pack()

# Entrada de la altura
tk.Label(ventana, text="Altura").pack()
caja_altura = tk.Entry(ventana)
caja_altura.pack()

# Botón calcular
tk.Button(ventana, text="CALCULAR AREA",
          command=calcular_area).pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

# Ejecutar
ventana.mainloop()
