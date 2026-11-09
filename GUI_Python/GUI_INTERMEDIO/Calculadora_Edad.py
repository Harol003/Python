
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Colores
AZUL = "#2878C8"
OSCURO = "#142D4E"
GRIS = "#E8EDF3"
BLANCO = "#FFFFFF"
NEGRO = "#171B22"

# Centrar ventana
def centrar(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Funcion para calcular la edad
def calcular_edad():
    try:
        # Capturamos el año de nacimiento
        nacimiento = int(entrada.get())

        # Obtenemos el año actual
        actual = datetime.now().year

        # Validamos el año
        if nacimiento < 1900 or nacimiento > actual:
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un año de nacimiento valido."
            )
            return

        # Calculamos la edad aproximada
        edad = actual - nacimiento

        # Mostramos resultado
        resultado.config(
            text=f"Tu edad aproximada es:\n{edad} AÑOS"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un año valido."
        )

# Funcion para limpiar
def limpiar():
    entrada.delete(0, tk.END)
    resultado.config(text="Esperando datos...")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de edad")
ventana.configure(bg=GRIS)
ventana.resizable(False, False)

centrar(ventana, 420, 370)

# Encabezado
tk.Label(
    ventana,
    text="CALCULADORA DE EDAD",
    font=("Arial", 18, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=20
).pack(fill="x")

# Panel
panel = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
panel.pack(padx=25, pady=20, fill="both")

# Instrucciones
tk.Label(
    panel,
    text="Ingrese su año de nacimiento",
    font=("Arial", 12, "bold"),
    bg=BLANCO,
    fg=NEGRO
).pack(pady=8)

# Caja de texto
entrada = tk.Entry(
    panel,
    font=("Arial", 15),
    bg=GRIS,
    fg=NEGRO,
    justify="center",
    relief="flat"
)
entrada.pack(fill="x", ipady=8)

# Boton calcular
tk.Button(
    panel,
    text="CALCULAR EDAD",
    command=calcular_edad,
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
    text="Esperando datos...",
    font=("Arial", 14, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=15
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
