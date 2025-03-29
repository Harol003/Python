### gui.py - Interfaz gráfica con Tkinter
### gui.py - Interfaz gráfica con Tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from db import insertar_usuario, modificar_usuario, eliminar_usuario, leer_usuarios, exportar_excel, exportar_csv, exportar_pdf

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    usuarios = leer_usuarios()
    for usuario in usuarios:
        tabla.insert('', 'end', values=usuario)

def agregar_usuario():
    insertar_usuario(entry_nombres.get(), entry_identificacion.get(), combo_tipo_id.get(), entry_correo.get(), entry_edad.get(), combo_genero.get())
    actualizar_tabla()

def modificar_usuario_gui():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado)['values']
        modificar_usuario(valores[0], entry_nombres.get(), entry_identificacion.get(), combo_tipo_id.get(), entry_correo.get(), entry_edad.get(), combo_genero.get())
        actualizar_tabla()

def eliminar_usuario_gui():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado)['values']
        eliminar_usuario(valores[0])
        actualizar_tabla()

def exportar_datos_excel():
    exportar_excel()
    messagebox.showinfo("Exportación", "Datos exportados a Excel correctamente.")

def exportar_datos_csv():
    exportar_csv()
    messagebox.showinfo("Exportación", "Datos exportados a CSV correctamente.")

def exportar_datos_pdf():
    exportar_pdf()
    messagebox.showinfo("Exportación", "Datos exportados a PDF correctamente.")

root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=20)

labels = ["Nombres y Apellidos", "Número de Identificación", "Correo Electrónico", "Edad"]
entries = []
for i, text in enumerate(labels):
    tk.Label(frame, text=text).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_nombres, entry_identificacion, entry_correo, entry_edad = entries

tk.Label(frame, text="Tipo de Identificación").grid(row=4, column=0, padx=10, pady=5)
combo_tipo_id = ttk.Combobox(frame, values=["Cédula", "Tarjeta de Identidad", "PPT"])
combo_tipo_id.grid(row=4, column=1, padx=10, pady=5)

tk.Label(frame, text="Género").grid(row=5, column=0, padx=10, pady=5)
combo_genero = ttk.Combobox(frame, values=["Masculino", "Femenino"])
combo_genero.grid(row=5, column=1, padx=10, pady=5)

botones = [
    ("Agregar Usuario", agregar_usuario),
    ("Modificar Usuario", modificar_usuario_gui),
    ("Eliminar Usuario", eliminar_usuario_gui),
    ("Exportar a Excel", exportar_datos_excel),
    ("Exportar a CSV", exportar_datos_csv),
    ("Exportar a PDF", exportar_datos_pdf)
]

for i, (text, command) in enumerate(botones):
    tk.Button(frame, text=text, command=command).grid(row=i, column=2, padx=10, pady=5)

tabla = ttk.Treeview(root, columns=("ID", "Nombres", "Identificación", "Tipo ID", "Correo", "Edad", "Género", "Fecha Registro"), show='headings')
for col in tabla['columns']:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.pack(pady=20)
actualizar_tabla()
root.mainloop()
