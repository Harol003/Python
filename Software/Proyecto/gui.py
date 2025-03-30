import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from db import insertar_usuario, modificar_usuario, eliminar_usuario, leer_usuarios, exportar_excel, exportar_csv, exportar_pdf

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    usuarios = leer_usuarios()
    for usuario in usuarios:
        tabla.insert('', 'end', values=usuario)

def agregar_usuario():
    if not entry_nombres.get().strip() or not entry_identificacion.get().strip() or not entry_correo.get().strip() or not entry_edad.get().strip():
        messagebox.showerror("Error", "Todos los campos deben estar llenos.")
        return
    
    if not entry_edad.get().isdigit():
        messagebox.showerror("Error", "La edad debe ser un número válido.")
        return
    
    try:
        insertar_usuario(entry_nombres.get(), entry_identificacion.get(), combo_tipo_id.get(), entry_correo.get(), entry_edad.get(), combo_genero.get())
        actualizar_tabla()
        messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar usuario: {str(e)}")

def cargar_imagen():
    filename = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
    if filename:
        img = Image.open(filename)
        img = img.resize((100, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label_imagen.config(image=img)
        label_imagen.image = img

def modificar_usuario_gui():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showerror("Error", "Selecciona un usuario para modificar.")
        return
    
    if not entry_nombres.get().strip() or not entry_identificacion.get().strip() or not entry_correo.get().strip() or not entry_edad.get().strip():
        messagebox.showerror("Error", "Todos los campos deben estar llenos.")
        return
    
    if not entry_edad.get().isdigit():
        messagebox.showerror("Error", "La edad debe ser un número válido.")
        return
    
    valores = tabla.item(seleccionado)['values']
    try:
        modificar_usuario(valores[0], entry_nombres.get(), entry_identificacion.get(), combo_tipo_id.get(), entry_correo.get(), entry_edad.get(), combo_genero.get())
        actualizar_tabla()
        messagebox.showinfo("Éxito", "Usuario modificado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al modificar usuario: {str(e)}")

def eliminar_usuario_gui():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showerror("Error", "Selecciona un usuario para eliminar.")
        return
    
    valores = tabla.item(seleccionado)['values']
    confirmar = messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar este usuario?")
    if confirmar:
        try:
            eliminar_usuario(valores[0])
            actualizar_tabla()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar usuario: {str(e)}")

def exportar_excel_gui():
    try:
        exportar_excel()
        messagebox.showinfo("Éxito", "Datos exportados correctamente a Excel.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar a Excel: {str(e)}")

def exportar_csv_gui():
    try:
        exportar_csv()
        messagebox.showinfo("Éxito", "Datos exportados correctamente a CSV.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar a CSV: {str(e)}")

def exportar_pdf_gui():
    try:
        exportar_pdf()
        messagebox.showinfo("Éxito", "Datos exportados correctamente a PDF.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar a PDF: {str(e)}")

root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("900x600")
root.configure(bg="#DDEEFF")

frame = tk.Frame(root, bg="#DDEEFF")
frame.pack(pady=20)

label_imagen = tk.Label(frame, text="Imagen Usuario", bg="#DDEEFF")
label_imagen.grid(row=0, column=3, rowspan=4, padx=20, pady=5)
btn_cargar_imagen = tk.Button(frame, text="Cargar Imagen", command=cargar_imagen, bg="#336699", fg="white", width=20)
btn_cargar_imagen.grid(row=4, column=3, padx=20, pady=5)

labels = ["Nombres y Apellidos", "Número de Identificación", "Correo Electrónico", "Edad"]
entries = []
for i, text in enumerate(labels):
    tk.Label(frame, text=text, bg="#DDEEFF").grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_nombres, entry_identificacion, entry_correo, entry_edad = entries

tk.Label(frame, text="Tipo de Identificación", bg="#DDEEFF").grid(row=4, column=0, padx=10, pady=5)
combo_tipo_id = ttk.Combobox(frame, values=["Cédula", "Tarjeta de Identidad", "PPT"], width=22)
combo_tipo_id.grid(row=4, column=1, padx=10, pady=5)

tk.Label(frame, text="Género", bg="#DDEEFF").grid(row=5, column=0, padx=10, pady=5)
combo_genero = ttk.Combobox(frame, values=["Masculino", "Femenino"], width=22)
combo_genero.grid(row=5, column=1, padx=10, pady=5)

botones = [
    ("Agregar Usuario", agregar_usuario),
    ("Modificar Usuario", modificar_usuario_gui),
    ("Eliminar Usuario", eliminar_usuario_gui),
    ("Exportar a Excel", exportar_excel_gui),
    ("Exportar a CSV", exportar_csv_gui),
    ("Exportar a PDF", exportar_pdf_gui)
]

for i, (text, command) in enumerate(botones):
    tk.Button(frame, text=text, command=command, bg="#336699", fg="white", width=20).grid(row=i, column=2, padx=10, pady=5)

tabla = ttk.Treeview(root, columns=("ID", "Nombres", "Identificación", "Tipo ID", "Correo", "Edad", "Género", "Fecha Registro"), show='headings')
for col in tabla['columns']:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.pack(pady=20)
actualizar_tabla()
root.mainloop()
