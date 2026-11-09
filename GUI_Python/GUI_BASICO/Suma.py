
# Importamos la biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

# Función para sumar los dos números
def sumar():
    # Obtenemos los valores ingresados
    num1 = float(caja1.get())
    num2 = float(caja2.get())

    # Realizamos la suma
    resultado = num1 + num2

    # Mostramos el resultado
    etiqueta_resultado.config(text="Resultado: " + str(resultado))

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("SUMA DE DOS NUMEROS")
ventana.geometry("350x300")

# Título del programa
tk.Label(ventana, text="SUMADORA", font=("Arial", 18)).pack(pady=10)

# Primera caja de texto
tk.Label(ventana, text="Primer número").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

# Segunda caja de texto
tk.Label(ventana, text="Segundo número").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

# Botón para ejecutar la suma
tk.Button(ventana, text="SUMAR", command=sumar).pack(pady=15)

# Etiqueta donde aparece el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

# Ejecutamos la ventana
ventana.mainloop()
