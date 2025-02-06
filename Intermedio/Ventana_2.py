import tkinter as tk

# Función para mostrar el saludo
def mostrar_mensaje():
    etiqueta_mensaje.config(text=f"¡Hola, {entrada.get()}!")

# Función para borrar el texto ingresado
def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_mensaje.config(text="")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz para niños")
ventana.geometry("400x250")
ventana.configure(bg="#87CEEB")  # Fondo azul claro
ventana.resizable(False, False)  # Tamaño fijo

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingrese su nombre:", font=("Arial", 14), bg="#87CEEB", fg="white")
etiqueta.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada.pack(pady=5)

# Botón para mostrar mensaje
boton_mostrar = tk.Button(ventana, text="Mostrar saludo", font=("Arial", 12), bg="blue", fg="white", command=mostrar_mensaje)
boton_mostrar.pack(pady=5)

# Botón para borrar el texto
boton_borrar = tk.Button(ventana, text="Borrar", font=("Arial", 12), bg="red", fg="white", command=borrar_texto)
boton_borrar.pack(pady=5)

# Etiqueta para mostrar el mensaje de saludo
etiqueta_mensaje = tk.Label(ventana, text="", font=("Arial", 14), bg="#87CEEB", fg="white")
etiqueta_mensaje.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
