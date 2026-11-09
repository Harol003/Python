import tkinter as tk
from tkinter import messagebox

def enviar():
    nombre = entrada_nombre.get().strip()
    observaciones = entrada_observaciones.get("1.0", tk.END).strip()
    if not nombre:
        messagebox.showwarning("Falta información", "Escribe tu nombre.")
        return
    calificacion = opcion.get()
    if not calificacion:
        messagebox.showwarning("Falta información", "Selecciona una calificación.")
        return
    messagebox.showinfo("Encuesta enviada",
                        f"Nombre: {nombre}\\nCalificación: {calificacion}\\n"
                        f"Observaciones: {observaciones or 'Sin observaciones'}")

def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_observaciones.delete("1.0", tk.END)
    opcion.set("")
    entrada_nombre.focus()

ventana = tk.Tk()
ventana.title("Encuesta de satisfacción")
ventana.geometry("450x400")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="ENCUESTA DE SATISFACCIÓN", font=("Arial", 15, "bold"),
         bg="#FFFFFF", fg="#563D7C").pack(pady=15)

tk.Label(ventana, text="Nombre:", bg="#FFFFFF").pack()
entrada_nombre = tk.Entry(ventana, width=32)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="¿Cómo califica nuestro servicio?", bg="#FFFFFF",
         font=("Arial", 11, "bold")).pack(pady=8)

opcion = tk.StringVar(value="")
for calificacion in ["Excelente", "Bueno", "Regular", "Malo"]:
    tk.Radiobutton(ventana, text=calificacion, variable=opcion, value=calificacion,
                   bg="#FFFFFF", activebackground="#FFFFFF").pack(anchor="center")

tk.Label(ventana, text="Observaciones:", bg="#FFFFFF").pack(pady=(8, 2))
entrada_observaciones = tk.Text(ventana, width=38, height=3)
entrada_observaciones.pack()

tk.Button(ventana, text="ENVIAR", width=18, bg="#563D7C", fg="white",
          command=enviar).pack(pady=6)
tk.Button(ventana, text="LIMPIAR", width=18, bg="#808080", fg="white",
          command=limpiar).pack(pady=2)
tk.Button(ventana, text="SALIR", width=18, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=2)

ventana.mainloop()
