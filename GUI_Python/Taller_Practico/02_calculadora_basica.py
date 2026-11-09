import tkinter as tk
from tkinter import messagebox

def obtener_numeros():
    try:
        return float(entrada1.get()), float(entrada2.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa dos números válidos.")
        return None

def calcular(operacion):
    datos = obtener_numeros()
    if datos is None:
        return
    a, b = datos
    if operacion == "sumar":
        resultado = a + b
    elif operacion == "restar":
        resultado = a - b
    elif operacion == "multiplicar":
        resultado = a * b
    else:
        if b == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            return
        resultado = a / b
    etiqueta_resultado.config(text=f"Resultado: {resultado:g}")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:")
    entrada1.focus()

ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("400x450")
ventana.resizable(False, False)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="CALCULADORA BÁSICA", font=("Arial", 16, "bold"),
         bg="#F2F2F2", fg="#000000").pack(pady=18)

tk.Label(ventana, text="Primer número:", bg="#F2F2F2").pack()
entrada1 = tk.Entry(ventana, justify="center", font=("Arial", 12))
entrada1.pack(pady=5)

tk.Label(ventana, text="Segundo número:", bg="#F2F2F2").pack()
entrada2 = tk.Entry(ventana, justify="center", font=("Arial", 12))
entrada2.pack(pady=5)

for texto, op in [("SUMAR", "sumar"), ("RESTAR", "restar"),
                  ("MULTIPLICAR", "multiplicar"), ("DIVIDIR", "dividir")]:
    tk.Button(ventana, text=texto, width=22, bg="#2878C8", fg="white",
              command=lambda operacion=op: calcular(operacion)).pack(pady=4)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 14, "bold"),
                              bg="#F2F2F2")
etiqueta_resultado.pack(pady=12)

tk.Button(ventana, text="LIMPIAR", width=22, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=22, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
