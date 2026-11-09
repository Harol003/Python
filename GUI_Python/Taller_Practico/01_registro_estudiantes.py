import tkinter as tk
from tkinter import messagebox

def guardar():
    nombre = entrada_nombre.get().strip()
    apellido = entrada_apellido.get().strip()
    edad = entrada_edad.get().strip()
    grado = entrada_grado.get().strip()
    if not all([nombre, apellido, edad, grado]):
        messagebox.showwarning("Datos incompletos", "Completa todos los campos.")
        return
    if not edad.isdigit():
        messagebox.showerror("Dato inválido", "La edad debe ser un número entero.")
        return
    messagebox.showinfo("Registro exitoso",
                        f"Estudiante: {nombre} {apellido}\\nEdad: {edad}\\nGrado: {grado}")

def limpiar():
    for campo in (entrada_nombre, entrada_apellido, entrada_edad, entrada_grado):
        campo.delete(0, tk.END)
    entrada_nombre.focus()

ventana = tk.Tk()
ventana.title("Registro de estudiantes")
ventana.geometry("450x400")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="REGISTRO DE ESTUDIANTES", font=("Arial", 16, "bold"),
         fg="#1F3A5F", bg="#FFFFFF").pack(pady=18)

formulario = tk.Frame(ventana, bg="#FFFFFF")
formulario.pack(pady=5)

campos = ["Nombre:", "Apellido:", "Edad:", "Grado:"]
entradas = []
for fila, texto in enumerate(campos):
    tk.Label(formulario, text=texto, bg="#FFFFFF", font=("Arial", 11)).grid(
        row=fila, column=0, sticky="e", padx=8, pady=8)
    campo = tk.Entry(formulario, width=27, font=("Arial", 11))
    campo.grid(row=fila, column=1, padx=8, pady=8)
    entradas.append(campo)

entrada_nombre, entrada_apellido, entrada_edad, entrada_grado = entradas

tk.Button(ventana, text="GUARDAR", width=18, bg="#198754", fg="white",
          command=guardar).pack(pady=7)
tk.Button(ventana, text="LIMPIAR", width=18, bg="#808080", fg="white",
          command=limpiar).pack(pady=4)
tk.Button(ventana, text="SALIR", width=18, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=4)

ventana.mainloop()
