
# Importamos tkinter
import tkinter as tk

# Función para realizar la resta
def restar():
    # Capturamos los números
    num1 = float(caja1.get())
    num2 = float(caja2.get())

    # Calculamos la resta
    resultado = num1 - num2

    # Mostramos el resultado
    resultado_label.config(text=f"Resultado: {resultado}")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("RESTA")
ventana.geometry("350x300")

# Título
tk.Label(ventana, text="RESTA DE DOS NUMEROS",
         font=("Arial", 16)).pack(pady=10)

# Entrada del primer número
tk.Label(ventana, text="Primer número").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

# Entrada del segundo número
tk.Label(ventana, text="Segundo número").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

# Botón para restar
tk.Button(ventana, text="RESTAR",
          command=restar).pack(pady=15)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()

# Iniciamos el programa
ventana.mainloop()
