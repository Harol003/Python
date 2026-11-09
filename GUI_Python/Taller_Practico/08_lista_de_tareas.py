import tkinter as tk
from tkinter import messagebox

def agregar():
    tarea = entrada_tarea.get().strip()
    if not tarea:
        messagebox.showwarning("Tarea vacía", "Escribe una tarea antes de agregarla.")
        return
    lista_tareas.insert(tk.END, tarea)
    entrada_tarea.delete(0, tk.END)
    entrada_tarea.focus()

def eliminar():
    seleccion = lista_tareas.curselection()
    if not seleccion:
        messagebox.showwarning("Sin selección", "Selecciona una tarea para eliminar.")
        return
    lista_tareas.delete(seleccion[0])

def limpiar():
    entrada_tarea.delete(0, tk.END)
    lista_tareas.delete(0, tk.END)
    entrada_tarea.focus()

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("450x450")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="MIS TAREAS", font=("Arial", 17, "bold"),
         bg="#FFFFFF", fg="#003366").pack(pady=18)

tk.Label(ventana, text="Escribe una tarea:", bg="#FFFFFF").pack()
entrada_tarea = tk.Entry(ventana, width=35, font=("Arial", 11))
entrada_tarea.pack(pady=7)

tk.Button(ventana, text="AGREGAR", width=20, bg="#198754", fg="white",
          command=agregar).pack(pady=5)

tk.Label(ventana, text="Tareas pendientes:", bg="#FFFFFF").pack(pady=5)
lista_tareas = tk.Listbox(ventana, width=42, height=10, font=("Arial", 10))
lista_tareas.pack(pady=5)

tk.Button(ventana, text="ELIMINAR SELECCIONADA", width=25, bg="#FD7E14", fg="white",
          command=eliminar).pack(pady=5)
tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
