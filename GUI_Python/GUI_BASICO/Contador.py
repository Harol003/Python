
# Importamos tkinter
import tkinter as tk

# Creamos una variable para almacenar el contador
contador = 0

# Función para aumentar el contador
def aumentar():
    global contador

    # Sumamos uno
    contador += 1

    # Actualizamos la pantalla
    etiqueta.config(text=str(contador))

# Función para disminuir el contador
def disminuir():
    global contador

    # Restamos uno
    contador -= 1

    # Actualizamos la pantalla
    etiqueta.config(text=str(contador))

# Función para reiniciar
def reiniciar():
    global contador

    # Volvemos el contador a cero
    contador = 0

    # Actualizamos la pantalla
    etiqueta.config(text=str(contador))

# Creamos ventana
ventana = tk.Tk()
ventana.title("CONTADOR")
ventana.geometry("350x300")

# Título
tk.Label(ventana, text="CONTADOR DIGITAL",
         font=("Arial", 18)).pack(pady=15)

# Pantalla del contador
etiqueta = tk.Label(ventana, text="0",
                    font=("Arial", 35))
etiqueta.pack(pady=10)

# Botón para aumentar
tk.Button(ventana, text="SUMAR +",
          command=aumentar).pack(pady=5)

# Botón para disminuir
tk.Button(ventana, text="RESTAR -",
          command=disminuir).pack(pady=5)

# Botón para reiniciar
tk.Button(ventana, text="REINICIAR",
          command=reiniciar).pack(pady=5)

# Ejecutamos
ventana.mainloop()
