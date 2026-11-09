import tkinter as tk
from tkinter import messagebox

def convertir(tipo):
    try:
        temperatura = float(entrada_temperatura.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa una temperatura válida.")
        return
    if tipo == "C-F":
        resultado = (temperatura * 9 / 5) + 32
        texto = f"{temperatura:g} °C equivalen a {resultado:.2f} °F"
    else:
        resultado = (temperatura - 32) * 5 / 9
        texto = f"{temperatura:g} °F equivalen a {resultado:.2f} °C"
    etiqueta_resultado.config(text=texto)

def limpiar():
    entrada_temperatura.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:")
    entrada_temperatura.focus()

ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.geometry("420x350")
ventana.resizable(False, False)
ventana.configure(bg="#EAF4F4")

tk.Label(ventana, text="CONVERSOR DE TEMPERATURA",
         font=("Arial", 15, "bold"), bg="#EAF4F4", fg="#003B46").pack(pady=20)

tk.Label(ventana, text="Ingresa la temperatura:", bg="#EAF4F4").pack()
entrada_temperatura = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada_temperatura.pack(pady=8)

tk.Button(ventana, text="CELSIUS A FAHRENHEIT", width=25,
          bg="#198754", fg="white", command=lambda: convertir("C-F")).pack(pady=5)
tk.Button(ventana, text="FAHRENHEIT A CELSIUS", width=25,
          bg="#198754", fg="white", command=lambda: convertir("F-C")).pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", bg="#EAF4F4",
                              font=("Arial", 11, "bold"), wraplength=380)
etiqueta_resultado.pack(pady=12)

tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
