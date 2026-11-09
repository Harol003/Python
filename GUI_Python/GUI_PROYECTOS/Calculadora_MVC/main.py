
# ==========================================
# ARCHIVO PRINCIPAL - main.py
# ==========================================

# Importamos las tres partes del programa

import tkinter as tk

from modelo import ModeloCalculadora

from vista import VistaCalculadora

from controlador import ControladorCalculadora


# ==========================================
# INICIAMOS LA APLICACION
# ==========================================

# Creamos la ventana principal
ventana = tk.Tk()

# Creamos el objeto modelo
modelo = ModeloCalculadora()

# Creamos el objeto vista
vista = VistaCalculadora(ventana)

# Creamos el controlador
# Le entregamos el modelo y la vista
controlador = ControladorCalculadora(
    modelo,
    vista
)

# Iniciamos el ciclo de la interfaz grafica
ventana.mainloop()
