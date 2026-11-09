
# Importamos tkinter
import tkinter as tk

# Función para generar la tabla
def generar_tabla():
    # Obtenemos el número
    numero = int(caja.get())

    # Variable para almacenar la tabla
    tabla = ""

    # Repetimos desde 1 hasta 10
    for i in range(1, 11):
        # Calculamos cada multiplicación
        tabla += f"{numero} x {i} = {numero * i}\n"

    # Mostramos la tabla
    resultado.config(text=tabla)

# Creamos la ventana
ventana = tk.Tk()
ventana.title("TABLA DE MULTIPLICAR")
ventana.geometry("350x400")

# Título
tk.Label(ventana, text="TABLA DE MULTIPLICAR",
         font=("Arial", 16)).pack(pady=10)

# Entrada del número
tk.Label(ventana, text="Ingrese un número").pack()
caja = tk.Entry(ventana)
caja.pack()

# Botón generar
tk.Button(ventana, text="GENERAR TABLA",
          command=generar_tabla).pack(pady=10)

# Etiqueta donde aparece la tabla
resultado = tk.Label(ventana, text="", justify="left",
                     font=("Arial", 12))
resultado.pack()

# Ejecutamos
ventana.mainloop()
