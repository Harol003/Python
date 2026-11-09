
import tkinter as tk
from tkinter import messagebox
import random

# Colores
AZUL = "#2878C8"
OSCURO = "#142D4E"
GRIS = "#E8EDF3"
BLANCO = "#FFFFFF"
NEGRO = "#171B22"

# Generamos un numero aleatorio
numero_secreto = random.randint(1, 20)

# Contador de intentos
intentos = 0

# Centrar ventana
def centrar(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Funcion para verificar el numero
def verificar():
    global intentos

    try:
        # Capturamos el numero ingresado
        numero = int(entrada.get())

        # Validamos el rango
        if numero < 1 or numero > 20:
            messagebox.showwarning(
                "Atencion",
                "Ingrese un numero entre 1 y 20."
            )
            return

        # Aumentamos los intentos
        intentos += 1

        # Comparamos el numero
        if numero == numero_secreto:
            resultado.config(
                text=f"¡FELICIDADES!\n"
                     f"Acertaste en {intentos} intentos.",
                bg="#176B48"
            )
            boton_verificar.config(state="disabled")

        elif numero < numero_secreto:
            resultado.config(
                text="El numero secreto es MAYOR",
                bg=OSCURO
            )

        else:
            resultado.config(
                text="El numero secreto es MENOR",
                bg=OSCURO
            )

        # Actualizamos el contador
        etiqueta_intentos.config(
            text=f"Intentos realizados: {intentos}"
        )

        # Limpiamos la entrada
        entrada.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un numero entero."
        )

# Funcion para comenzar un nuevo juego
def nuevo_juego():
    global numero_secreto, intentos

    # Generamos otro numero
    numero_secreto = random.randint(1, 20)

    # Reiniciamos intentos
    intentos = 0

    # Limpiamos los datos
    entrada.delete(0, tk.END)

    # Restauramos etiquetas
    resultado.config(
        text="¡Adivina el numero!",
        bg=OSCURO
    )

    etiqueta_intentos.config(text="Intentos realizados: 0")

    # Activamos el boton
    boton_verificar.config(state="normal")

# Ventana principal
ventana = tk.Tk()
ventana.title("Juego de adivinanza")
ventana.configure(bg=GRIS)
ventana.resizable(False, False)

centrar(ventana, 450, 440)

# Encabezado
tk.Label(
    ventana,
    text="JUEGO DE ADIVINANZA",
    font=("Arial", 18, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=20
).pack(fill="x")

# Panel principal
panel = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
panel.pack(padx=25, pady=20, fill="both")

# Instrucciones
tk.Label(
    panel,
    text="Adivina el numero entre 1 y 20",
    font=("Arial", 12, "bold"),
    bg=BLANCO,
    fg=NEGRO
).pack(pady=8)

# Caja de entrada
entrada = tk.Entry(
    panel,
    font=("Arial", 16),
    bg=GRIS,
    fg=NEGRO,
    justify="center",
    relief="flat"
)
entrada.pack(fill="x", ipady=8)

# Boton verificar
boton_verificar = tk.Button(
    panel,
    text="VERIFICAR NUMERO",
    command=verificar,
    bg=AZUL,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
)
boton_verificar.pack(fill="x", pady=12)

# Resultado
resultado = tk.Label(
    panel,
    text="¡Adivina el numero!",
    font=("Arial", 12, "bold"),
    bg=OSCURO,
    fg=BLANCO,
    pady=15
)
resultado.pack(fill="x")

# Intentos
etiqueta_intentos = tk.Label(
    panel,
    text="Intentos realizados: 0",
    font=("Arial", 10),
    bg=BLANCO,
    fg=NEGRO
)
etiqueta_intentos.pack(pady=10)

# Boton nuevo juego
tk.Button(
    panel,
    text="NUEVO JUEGO",
    command=nuevo_juego,
    bg="#65758B",
    fg=BLANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", pady=4)

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
).pack(fill="x", pady=4)

# Ejecutar
ventana.mainloop()
