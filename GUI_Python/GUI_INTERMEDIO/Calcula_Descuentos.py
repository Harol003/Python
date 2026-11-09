
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# COLORES DEL PROGRAMA
# -------------------------------
AZUL = "#2878C8"
AZUL_OSCURO = "#142D4E"
GRIS = "#E8EDF3"
BLANCO = "#FFFFFF"
NEGRO = "#171B22"

# -------------------------------
# FUNCION PARA CENTRAR LA VENTANA
# -------------------------------
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()

    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# -------------------------------
# FUNCION PARA CALCULAR DESCUENTO
# -------------------------------
def calcular():
    try:
        # Capturamos los datos
        precio = float(entrada_precio.get())
        descuento = float(entrada_descuento.get())

        # Validamos los valores
        if precio < 0 or descuento < 0 or descuento > 100:
            messagebox.showwarning(
                "Atencion",
                "Ingrese valores validos."
            )
            return

        # Calculamos el descuento
        valor_descuento = precio * descuento / 100

        # Calculamos el precio final
        total = precio - valor_descuento

        # Mostramos los resultados
        resultado.config(
            text=f"Descuento: ${valor_descuento:,.2f}\n"
                 f"TOTAL A PAGAR: ${total:,.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Debe ingresar valores numericos."
        )

# -------------------------------
# FUNCION PARA LIMPIAR
# -------------------------------
def limpiar():
    entrada_precio.delete(0, tk.END)
    entrada_descuento.delete(0, tk.END)
    resultado.config(text="Esperando calculo...")

# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------
ventana = tk.Tk()
ventana.title("Calculadora de descuentos")
ventana.configure(bg=GRIS)
ventana.resizable(False, False)

centrar_ventana(ventana, 450, 440)

# -------------------------------
# ENCABEZADO
# -------------------------------
tk.Label(
    ventana,
    text="CALCULADORA DE DESCUENTOS",
    font=("Arial", 17, "bold"),
    bg=AZUL_OSCURO,
    fg=BLANCO,
    pady=20
).pack(fill="x")

# -------------------------------
# CONTENEDOR PRINCIPAL
# -------------------------------
panel = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
panel.pack(padx=25, pady=20, fill="both")

# Precio
tk.Label(
    panel,
    text="Precio del producto ($)",
    bg=BLANCO,
    fg=NEGRO,
    font=("Arial", 11, "bold")
).pack(anchor="w")

entrada_precio = tk.Entry(
    panel, font=("Arial", 13),
    bg=GRIS, fg=NEGRO, relief="flat"
)
entrada_precio.pack(fill="x", ipady=8, pady=7)

# Porcentaje de descuento
tk.Label(
    panel,
    text="Descuento (%)",
    bg=BLANCO,
    fg=NEGRO,
    font=("Arial", 11, "bold")
).pack(anchor="w")

entrada_descuento = tk.Entry(
    panel, font=("Arial", 13),
    bg=GRIS, fg=NEGRO, relief="flat"
)
entrada_descuento.pack(fill="x", ipady=8, pady=7)

# Boton calcular
tk.Button(
    panel,
    text="CALCULAR DESCUENTO",
    command=calcular,
    bg=AZUL,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
).pack(fill="x", pady=10)

# Resultado
resultado = tk.Label(
    panel,
    text="Esperando calculo...",
    bg=AZUL_OSCURO,
    fg=BLANCO,
    font=("Arial", 12, "bold"),
    pady=15
)
resultado.pack(fill="x", pady=8)

# Botones inferiores
tk.Button(
    panel, text="LIMPIAR",
    command=limpiar,
    bg="#65758B", fg=BLANCO,
    font=("Arial", 10, "bold"),
    relief="flat", cursor="hand2"
).pack(fill="x", pady=4)

tk.Button(
    panel, text="SALIR",
    command=ventana.destroy,
    bg=NEGRO, fg=BLANCO,
    font=("Arial", 10, "bold"),
    relief="flat", cursor="hand2"
).pack(fill="x", pady=4)

# Ejecutar programa
ventana.mainloop()
