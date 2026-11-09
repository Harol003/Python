
# Importamos tkinter
import tkinter as tk
from tkinter import messagebox

# Función para dividir
def dividir():
    # Capturamos los números
    num1 = float(caja1.get())
    num2 = float(caja2.get())

    # Verificamos que no se divida entre cero
    if num2 == 0:
        messagebox.showerror("Error", "No se puede dividir entre cero")
    else:
        # Realizamos la división
        resultado = num1 / num2

        # Mostramos el resultado
        resultado_label.config(text=f"Resultado: {resultado}")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("DIVISION")
ventana.geometry("350x300")

# Título
tk.Label(ventana, text="DIVISOR",
         font=("Arial", 18)).pack(pady=10)

# Primer número
tk.Label(ventana, text="Dividendo").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

# Segundo número
tk.Label(ventana, text="Divisor").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

# Botón dividir
tk.Button(ventana, text="DIVIDIR",
          command=dividir).pack(pady=15)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()

# Ejecutamos
ventana.mainloop()
