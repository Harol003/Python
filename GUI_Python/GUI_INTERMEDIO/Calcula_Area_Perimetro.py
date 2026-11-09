
import tkinter as tk
from tkinter import messagebox
import math

# Colores
AZUL = "#2878C8"
OSCURO = "#142D4E"
GRIS = "#E8EDF3"
BLANCO = "#FFFFFF"
NEGRO = "#171B22"

# Funcion para centrar la ventana
def centrar(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Funcion para calcular
def calcular():
    try:
        # Obtenemos el radio
        radio = float(entrada.get())

        # Validamos que sea positivo
        if radio <= 0:
            messagebox.showwarning(
                "Advertencia",
                "El radio debe ser mayor que cero."
            )
            return

        # Calculamos el area
        area = math.pi * radio ** 2

        # Calculamos el perimetro
        perimetro = 2 * math.pi * radio

        # Mostramos resultados
        resultado.config(
            text=f"AREA: {area:.2f}\n"
                 f"PERIMETRO: {perimetro:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un numero valido."
        )

# Funcion para limpiar
def limpiar():
    entrada.delete(0, tk.END)
    resultado.config(text="Ingrese el radio")

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora de circulo")
ventana.configure(bg=GRIS)
ventana.resizable(False, False)

centrar(ventana, 430, 390)

# Encabezado
tk.Label(
    ventana,
    text="GEOMETRIA DEL CIRCULO",
    font=("Arial", 17, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=20
).pack(fill="x")

# Panel central
panel = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
panel.pack(padx=25, pady=20, fill="both")

# Descripcion
tk.Label(
    panel,
    text="Ingrese el radio del circulo",
    font=("Arial", 12, "bold"),
    bg=BLANCO,
    fg=NEGRO
).pack(pady=8)

# Entrada
entrada = tk.Entry(
    panel,
    font=("Arial", 14),
    bg=GRIS,
    fg=NEGRO,
    justify="center",
    relief="flat"
)
entrada.pack(fill="x", ipady=8)

# Boton calcular
tk.Button(
    panel,
    text="CALCULAR",
    command=calcular,
    bg=AZUL,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
).pack(fill="x", pady=15)

# Resultado
resultado = tk.Label(
    panel,
    text="Ingrese el radio",
    font=("Arial", 13, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=18
)
resultado.pack(fill="x")

# Boton limpiar
tk.Button(
    panel,
    text="LIMPIAR",
    command=limpiar,
    bg="#65758B",
    fg=BLANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", pady=8)

# Boton salir
tk.Button(
    panel,
    text="SALIR",
    command=ventana.destroy,
    bg=NEGRO,
    fg=BLANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x")

# Ejecutar
ventana.mainloop()
