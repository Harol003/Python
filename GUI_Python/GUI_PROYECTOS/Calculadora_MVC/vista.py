
# ==========================================
# VISTA - vista.py
# Interfaz sencilla de la calculadora
# ==========================================

import tkinter as tk

class VistaCalculadora:

    def __init__(self, ventana):

        # Guardamos la ventana principal
        self.ventana = ventana

        # Configuramos la ventana
        self.ventana.title("Calculadora MVC")
        self.ventana.geometry("350x350")
        self.ventana.resizable(False, False)

        # Centramos la ventana
        ancho = 350
        alto = 350

        x = (ventana.winfo_screenwidth() - ancho) // 2
        y = (ventana.winfo_screenheight() - alto) // 2

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        # ==================================
        # TITULO
        # ==================================

        tk.Label(
            ventana,
            text="CALCULADORA BASICA",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==================================
        # PRIMER NUMERO
        # ==================================

        tk.Label(
            ventana,
            text="Primer numero:"
        ).pack()

        self.entrada1 = tk.Entry(
            ventana,
            font=("Arial", 12),
            justify="center"
        )

        self.entrada1.pack(pady=5)

        # ==================================
        # SEGUNDO NUMERO
        # ==================================

        tk.Label(
            ventana,
            text="Segundo numero:"
        ).pack()

        self.entrada2 = tk.Entry(
            ventana,
            font=("Arial", 12),
            justify="center"
        )

        self.entrada2.pack(pady=5)

        # ==================================
        # BOTON SUMAR
        # ==================================

        self.boton_sumar = tk.Button(
            ventana,
            text="SUMAR",
            width=20
        )

        self.boton_sumar.pack(pady=5)

        # ==================================
        # BOTON RESTAR
        # ==================================

        self.boton_restar = tk.Button(
            ventana,
            text="RESTAR",
            width=20
        )

        self.boton_restar.pack(pady=5)

        # ==================================
        # RESULTADO
        # ==================================

        self.resultado = tk.Label(
            ventana,
            text="RESULTADO: 0",
            font=("Arial", 14, "bold")
        )

        self.resultado.pack(pady=10)

        # ==================================
        # BOTON LIMPIAR
        # ==================================

        self.boton_limpiar = tk.Button(
            ventana,
            text="LIMPIAR",
            width=20
        )

        self.boton_limpiar.pack(pady=3)

        # ==================================
        # BOTON SALIR
        # ==================================

        self.boton_salir = tk.Button(
            ventana,
            text="SALIR",
            width=20
        )

        self.boton_salir.pack(pady=3)
