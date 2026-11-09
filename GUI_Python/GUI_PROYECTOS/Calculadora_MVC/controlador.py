
# ==========================================
# CONTROLADOR - controlador.py
# ==========================================

from tkinter import messagebox

class ControladorCalculadora:

    def __init__(self, modelo, vista):

        # Recibimos el modelo y la vista
        self.modelo = modelo
        self.vista = vista

        # ==================================
        # CONECTAMOS LOS BOTONES
        # ==================================

        self.vista.boton_sumar.config(
            command=self.sumar
        )

        self.vista.boton_restar.config(
            command=self.restar
        )

        self.vista.boton_limpiar.config(
            command=self.limpiar
        )

        self.vista.boton_salir.config(
            command=self.salir
        )

    # ======================================
    # FUNCION PARA OBTENER LOS NUMEROS
    # ======================================

    def obtener_numeros(self):

        try:
            # Capturamos el primer numero
            numero1 = float(
                self.vista.entrada1.get()
            )

            # Capturamos el segundo numero
            numero2 = float(
                self.vista.entrada2.get()
            )

            # Retornamos ambos numeros
            return numero1, numero2

        except ValueError:

            # Mostramos un mensaje si hay error
            messagebox.showerror(
                "Error",
                "Debe ingresar dos numeros validos."
            )

            return None

    # ======================================
    # FUNCION PARA SUMAR
    # ======================================

    def sumar(self):

        # Obtenemos los numeros
        numeros = self.obtener_numeros()

        # Verificamos que sean validos
        if numeros is None:
            return

        numero1, numero2 = numeros

        # Solicitamos la suma al modelo
        resultado = self.modelo.sumar(
            numero1,
            numero2
        )

        # Mostramos el resultado en la vista
        self.vista.resultado.config(
            text=f"RESULTADO: {resultado:g}"
        )

    # ======================================
    # FUNCION PARA RESTAR
    # ======================================

    def restar(self):

        # Obtenemos los numeros
        numeros = self.obtener_numeros()

        # Verificamos que sean validos
        if numeros is None:
            return

        numero1, numero2 = numeros

        # Solicitamos la resta al modelo
        resultado = self.modelo.restar(
            numero1,
            numero2
        )

        # Mostramos el resultado
        self.vista.resultado.config(
            text=f"RESULTADO: {resultado:g}"
        )

    # ======================================
    # FUNCION PARA LIMPIAR
    # ======================================

    def limpiar(self):

        # Borramos el contenido de las entradas
        self.vista.entrada1.delete(0, "end")
        self.vista.entrada2.delete(0, "end")

        # Reiniciamos el resultado
        self.vista.resultado.config(
            text="RESULTADO: 0"
        )

    # ======================================
    # FUNCION PARA SALIR
    # ======================================

    def salir(self):

        # Cerramos la ventana principal
        self.vista.ventana.destroy()
