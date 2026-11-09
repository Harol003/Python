import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    figura = lista_figura.get()
    try:
        a = float(entrada1.get())
        if a <= 0:
            raise ValueError
        if figura == "Cuadrado":
            area = a * a
        else:
            b = float(entrada2.get())
            if b <= 0:
                raise ValueError
            if figura == "Rectángulo":
                area = a * b
            else:
                area = (a * b) / 2
    except ValueError:
        messagebox.showerror("Dato inválido", "Ingresa medidas numéricas mayores que cero.")
        return
    etiqueta_resultado.config(text=f"Área: {area:.2f} unidades²")

def actualizar_campos(event=None):
    if lista_figura.get() == "Cuadrado":
        etiqueta_medida2.grid_remove()
        entrada2.grid_remove()
    else:
        etiqueta_medida2.grid()
        entrada2.grid()

def limpiar():
    lista_figura.set("Cuadrado")
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resultado.config(text="Área:")
    actualizar_campos()

ventana = tk.Tk()
ventana.title("Calculadora de áreas")
ventana.geometry("450x400")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="CALCULADORA DE ÁREAS", font=("Arial", 16, "bold"),
         bg="#FFFFFF", fg="#17365D").pack(pady=18)

tk.Label(ventana, text="Selecciona una figura:", bg="#FFFFFF").pack()
lista_figura = ttk.Combobox(ventana, values=["Cuadrado", "Rectángulo", "Triángulo"],
                            state="readonly", width=25)
lista_figura.set("Cuadrado")
lista_figura.pack(pady=7)
lista_figura.bind("<<ComboboxSelected>>", actualizar_campos)

tk.Label(ventana, text="Primera medida (lado o base):", bg="#FFFFFF").pack()
entrada1 = tk.Entry(ventana, justify="center")
entrada1.pack(pady=5)

etiqueta_medida2 = tk.Label(ventana, text="Segunda medida (altura):", bg="#FFFFFF")
etiqueta_medida2.pack()
entrada2 = tk.Entry(ventana, justify="center")
entrada2.pack(pady=5)
actualizar_campos()

tk.Button(ventana, text="CALCULAR", width=20, bg="#2878C8", fg="white",
          command=calcular).pack(pady=8)
etiqueta_resultado = tk.Label(ventana, text="Área:", font=("Arial", 13, "bold"), bg="#FFFFFF")
etiqueta_resultado.pack(pady=5)
tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
