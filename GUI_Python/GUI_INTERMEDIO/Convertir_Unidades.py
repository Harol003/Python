
import tkinter as tk
from tkinter import messagebox

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

# Funcion para convertir las unidades
def convertir():
    try:
        # Obtenemos la cantidad en metros
        metros = float(entrada.get())

        # Calculamos las conversiones
        centimetros = metros * 100
        kilometros = metros / 1000
        milimetros = metros * 1000

        # Mostramos los resultados
        resultado.config(
            text=f"METROS: {metros:g} m\n\n"
                 f"CENTIMETROS: {centimetros:g} cm\n\n"
                 f"KILOMETROS: {kilometros:g} km\n\n"
                 f"MILIMETROS: {milimetros:g} mm"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese una cantidad numerica valida."
        )

# Funcion para limpiar
def limpiar():
    entrada.delete(0, tk.END)
    resultado.config(text="Esperando conversion...")

# Ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de longitud")
ventana.configure(bg=GRIS)
ventana.resizable(False, False)

centrar(ventana, 450, 490)

# Encabezado
tk.Label(
    ventana,
    text="CONVERTIDOR DE LONGITUD",
    font=("Arial", 17, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=20
).pack(fill="x")

# Panel central
panel = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
panel.pack(padx=25, pady=20, fill="both")

# Instrucciones
tk.Label(
    panel,
    text="Ingrese la cantidad en metros",
    font=("Arial", 12, "bold"),
    bg=BLANCO,
    fg=NEGRO
).pack(pady=8)

# Entrada de datos
entrada = tk.Entry(
    panel,
    font=("Arial", 15),
    bg=GRIS,
    fg=NEGRO,
    justify="center",
    relief="flat"
)
entrada.pack(fill="x", ipady=8)

# Boton convertir
tk.Button(
    panel,
    text="CONVERTIR UNIDADES",
    command=convertir,
    bg=AZUL,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
).pack(fill="x", pady=12)

# Resultados
resultado = tk.Label(
    panel,
    text="Esperando conversion...",
    font=("Arial", 11, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    justify="left",
    anchor="w",
    padx=20,
    pady=15
)
resultado.pack(fill="x", pady=5)

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
).pack(fill="x", pady=5)

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
).pack(fill="x", pady=5)

# Ejecutar programa
ventana.mainloop()
