import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text=f"Hola, {entrada.get()}!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")
ventana.geometry("300x150")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack(pady=5)

# Campo de entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón para mostrar mensaje
boton = tk.Button(ventana, text="Mostrar saludo", command=mostrar_mensaje)
boton.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

