
# Importamos tkinter
import tkinter as tk

# Función para multiplicar
def multiplicar():
    # Obtenemos los números
    num1 = float(caja1.get())
    num2 = float(caja2.get())

    # Multiplicamos
    resultado = num1 * num2

    # Presentamos el resultado
    resultado_label.config(text=f"Resultado: {resultado}")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("MULTIPLICACION")
ventana.geometry("350x300")

# Título
tk.Label(ventana, text="MULTIPLICADOR",
         font=("Arial", 18)).pack(pady=10)

# Primer número
tk.Label(ventana, text="Primer número").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

# Segundo número
tk.Label(ventana, text="Segundo número").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

# Botón multiplicar
tk.Button(ventana, text="MULTIPLICAR",
          command=multiplicar).pack(pady=15)

# Etiqueta del resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()

# Ejecutar
ventana.mainloop()
