
# Importamos tkinter
import tkinter as tk

# Función para convertir temperatura
def convertir():
    # Obtenemos los grados Celsius
    celsius = float(caja.get())

    # Aplicamos la fórmula de conversión
    fahrenheit = (celsius * 9/5) + 32

    # Mostramos el resultado
    resultado.config(text=f"Fahrenheit: {fahrenheit:.2f} °F")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("CONVERTIDOR DE TEMPERATURA")
ventana.geometry("350x250")

# Título
tk.Label(ventana, text="CONVERTIDOR",
         font=("Arial", 18)).pack(pady=10)

# Entrada de temperatura
tk.Label(ventana, text="Grados Celsius").pack()
caja = tk.Entry(ventana)
caja.pack()

# Botón convertir
tk.Button(ventana, text="CONVERTIR",
          command=convertir).pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

# Ejecutar ventana
ventana.mainloop()
