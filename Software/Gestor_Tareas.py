import tkinter as tk
from tkinter import messagebox
import json
import csv
from datetime import datetime

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Politécnico Internacional - Gestor de Tareas")  # Título de la ventana

# Obtener las dimensiones de la pantalla para centrar la ventana
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()

# Definir las dimensiones de la ventana
ventana_ancho = 400
ventana_alto = 500

# Calcular la posición de la ventana para centrarla
pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")
ventana.config(bg="#003366")  # Fondo de la ventana azul oscuro

# Lista para almacenar tareas
tareas = []

# Función para cargar tareas desde el archivo JSON
def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Función para guardar tareas en el archivo JSON
def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

# Función para agregar una tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        tareas.append({"tarea": tarea, "fecha": "", "completada": False})
        actualizar_lista()
        entry_tarea.delete(0, tk.END)
        guardar_tareas()
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        tareas.pop(index)
        actualizar_lista()
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para eliminar.")

# Función para editar tarea
def editar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        nueva_tarea = entry_tarea.get()
        if nueva_tarea != "":
            tareas[index]["tarea"] = nueva_tarea
            actualizar_lista()
            entry_tarea.delete(0, tk.END)
            guardar_tareas()
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nuevo nombre para la tarea.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para editar.")

# Función para actualizar la lista de tareas en la interfaz
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea["tarea"])

# Función para mostrar un recordatorio de tareas próximas a su vencimiento
def mostrar_recordatorio():
    hoy = datetime.now()
    for tarea in tareas:
        if tarea["fecha"] != "":
            fecha_vencimiento = datetime.strptime(tarea["fecha"], "%Y-%m-%d")
            if fecha_vencimiento.date() == hoy.date():
                messagebox.showinfo("Recordatorio", f"La tarea '{tarea['tarea']}' vence hoy.")

# Función para exportar tareas a un archivo CSV
def exportar_csv():
    with open("tareas.csv", mode="w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Tarea", "Fecha", "Completada"])  # Encabezados
        for tarea in tareas:
            writer.writerow([tarea["tarea"], tarea["fecha"], tarea["completada"]])
    messagebox.showinfo("Éxito", "Las tareas han sido exportadas a tareas.csv")

# Crear los componentes de la ventana
entry_tarea = tk.Entry(ventana, width=30)
entry_tarea.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea, width=20, height=2, bg="#003366", fg="white", font=("Arial", 12))
boton_agregar.pack(pady=5)

boton_editar = tk.Button(ventana, text="Editar tarea", command=editar_tarea, width=20, height=2, bg="#003366", fg="white", font=("Arial", 12))
boton_editar.pack(pady=5)

lista_tareas = tk.Listbox(ventana, width=40, height=10, font=("Arial", 12))
lista_tareas.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea, width=20, height=2, bg="#003366", fg="white", font=("Arial", 12))
boton_eliminar.pack(pady=5)

boton_exportar = tk.Button(ventana, text="Exportar a CSV", command=exportar_csv, width=20, height=2, bg="#003366", fg="white", font=("Arial", 12))
boton_exportar.pack(pady=5)

# Cargar las tareas al iniciar la aplicación
tareas = cargar_tareas()
actualizar_lista()

# Llamar a la función para mostrar recordatorio de tareas
mostrar_recordatorio()

# Ejecutar la aplicación
ventana.mainloop()
