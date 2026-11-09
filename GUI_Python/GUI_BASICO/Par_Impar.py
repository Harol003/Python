
# Importamos tkinter
import tkinter as tk

# Función para determinar si es par o impar
def verificar():
    # Obtenemos el número ingresado
    numero = int(caja.get())

    # Comprobamos el residuo de la división entre 2
    if numero % 2 == 0:
        resultado.config(text="El número es PAR")
    else:
        resultado.config(text="El número es IMPAR")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("PAR O IMPAR")
ventana.geometry("350x250")

# Título
tk.Label(ventana, text="PAR O IMPAR",
         font=("Arial", 18)).pack(pady=10)

# Entrada del número
tk.Label(ventana, text="Ingrese un número").pack()
caja = tk.Entry(ventana)
caja.pack()

# Botón verificar
tk.Button(ventana, text="VERIFICAR",
          command=verificar).pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

# Ejecutar
ventana.mainloop()
