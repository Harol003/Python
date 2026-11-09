import tkinter as tk
from tkinter import messagebox

def calcular():
    nombre = entrada_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Dato faltante", "Escribe el nombre del estudiante.")
        return
    try:
        notas = [float(campo.get()) for campo in (entrada_nota1, entrada_nota2, entrada_nota3)]
        if any(nota < 0 or nota > 5 for nota in notas):
            raise ValueError
    except ValueError:
        messagebox.showerror("Notas inválidas", "Ingresa notas numéricas entre 0.0 y 5.0.")
        return
    promedio = sum(notas) / 3
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    etiqueta_promedio.config(text=f"Promedio: {promedio:.2f}")
    etiqueta_estado.config(text=f"Estado: {estado}")

def limpiar():
    for campo in (entrada_nombre, entrada_nota1, entrada_nota2, entrada_nota3):
        campo.delete(0, tk.END)
    etiqueta_promedio.config(text="Promedio:")
    etiqueta_estado.config(text="Estado:")
    entrada_nombre.focus()

ventana = tk.Tk()
ventana.title("Sistema de notas")
ventana.geometry("450x450")
ventana.resizable(False, False)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="SISTEMA DE NOTAS", font=("Arial", 16, "bold"),
         bg="#F2F2F2", fg="#1F3A5F").pack(pady=17)

formulario = tk.Frame(ventana, bg="#F2F2F2")
formulario.pack(pady=5)

tk.Label(formulario, text="Nombre del estudiante:", bg="#F2F2F2").grid(row=0, column=0, sticky="e", padx=7, pady=8)
entrada_nombre = tk.Entry(formulario, width=25)
entrada_nombre.grid(row=0, column=1, pady=8)

for fila, texto in enumerate(["Nota 1:", "Nota 2:", "Nota 3:"], start=1):
    tk.Label(formulario, text=texto, bg="#F2F2F2").grid(row=fila, column=0, sticky="e", padx=7, pady=8)
    campo = tk.Entry(formulario, width=25)
    campo.grid(row=fila, column=1, pady=8)
    if fila == 1:
        entrada_nota1 = campo
    elif fila == 2:
        entrada_nota2 = campo
    else:
        entrada_nota3 = campo

tk.Button(ventana, text="CALCULAR", width=22, bg="#198754", fg="white",
          command=calcular).pack(pady=8)
etiqueta_promedio = tk.Label(ventana, text="Promedio:", font=("Arial", 12, "bold"), bg="#F2F2F2")
etiqueta_promedio.pack(pady=5)
etiqueta_estado = tk.Label(ventana, text="Estado:", font=("Arial", 12, "bold"), bg="#F2F2F2")
etiqueta_estado.pack(pady=5)

tk.Button(ventana, text="LIMPIAR", width=22, bg="#808080", fg="white",
          command=limpiar).pack(pady=4)
tk.Button(ventana, text="SALIR", width=22, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=4)

ventana.mainloop()
