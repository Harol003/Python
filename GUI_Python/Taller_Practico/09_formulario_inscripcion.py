import tkinter as tk
from tkinter import ttk, messagebox

def inscribir():
    nombre = entrada_nombre.get().strip()
    documento = entrada_documento.get().strip()
    correo = entrada_correo.get().strip()
    actividad = lista_actividad.get()
    if not all([nombre, documento, correo, actividad]):
        messagebox.showwarning("Datos incompletos", "Completa todos los campos.")
        return
    if "@" not in correo or "." not in correo:
        messagebox.showerror("Correo inválido", "Escribe un correo electrónico válido.")
        return
    if not acepta.get():
        messagebox.showwarning("Confirmación requerida", "Debes aceptar las condiciones.")
        return
    messagebox.showinfo("Inscripción exitosa",
                        f"Estudiante: {nombre}\\nDocumento: {documento}\\n"
                        f"Correo: {correo}\\nActividad: {actividad}")

def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_documento.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    lista_actividad.set("")
    acepta.set(False)
    entrada_nombre.focus()

ventana = tk.Tk()
ventana.title("Formulario de inscripción")
ventana.geometry("480x450")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="INSCRIPCIÓN EXTRACURRICULAR",
         font=("Arial", 15, "bold"), bg="#FFFFFF", fg="#C65911").pack(pady=17)

formulario = tk.Frame(ventana, bg="#FFFFFF")
formulario.pack(pady=3)

datos = ["Nombre:", "Documento:", "Correo electrónico:"]
entradas = []
for fila, texto in enumerate(datos):
    tk.Label(formulario, text=texto, bg="#FFFFFF").grid(row=fila, column=0, sticky="e", padx=7, pady=8)
    campo = tk.Entry(formulario, width=28)
    campo.grid(row=fila, column=1, padx=7, pady=8)
    entradas.append(campo)

entrada_nombre, entrada_documento, entrada_correo = entradas

tk.Label(ventana, text="Selecciona una actividad:", bg="#FFFFFF").pack(pady=(8, 3))
lista_actividad = ttk.Combobox(ventana, values=["Deportes", "Música", "Danza", "Robótica"],
                              state="readonly", width=25)
lista_actividad.pack(pady=3)

acepta = tk.BooleanVar(value=False)
tk.Checkbutton(ventana, text="Acepto las condiciones de inscripción",
               variable=acepta, bg="#FFFFFF").pack(pady=10)

tk.Button(ventana, text="INSCRIBIR", width=20, bg="#E67E22", fg="white",
          command=inscribir).pack(pady=5)
tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
