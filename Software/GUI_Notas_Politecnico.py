import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.font import Font

# Nombre del archivo CSV donde se guardarán los datos
ARCHIVO_CSV = "estudiantes.csv"
# Contraseña para acceder al módulo de profesor
CONTRASENA_PROFESOR = "politecnico"

# Función para centrar ventanas
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"+{x}+{y}")

# Función para inicializar el archivo CSV si no existe
def inicializar_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="") as file:
            csv.writer(file).writerow(["Nombre", "Nota1", "Nota2", "Nota3", "NotaFinal"])

# Función para cargar los datos del archivo CSV
def cargar_datos():
    with open(ARCHIVO_CSV, "r") as file:
        return list(csv.DictReader(file))

# Función para guardar los datos en el archivo CSV
def guardar_datos(datos):
    with open(ARCHIVO_CSV, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Nombre", "Nota1", "Nota2", "Nota3", "NotaFinal"])
        writer.writeheader()
        writer.writerows(datos)

# Función para calcular la nota final basada en los pesos asignados
def calcular_nota(n1, n2, n3):
    return (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)

# Función para validar que las notas ingresadas estén entre 0 y 5
def validar_nota(nota):
    try:
        nota = float(nota)
        if 0 <= nota <= 5:
            return True
        else:
            messagebox.showerror("Error", "La nota debe estar entre 0 y 5.")
            return False
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")
        return False

# Función para agregar un nuevo estudiante y sus notas
def agregar_estudiante():
    def guardar():
        nombre = entry_nombre.get()
        nota1 = entry_nota1.get()
        nota2 = entry_nota2.get()
        nota3 = entry_nota3.get()

        if not nombre or not nota1 or not nota2 or not nota3:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if not all(validar_nota(nota) for nota in [nota1, nota2, nota3]):
            return

        notas = [float(nota1), float(nota2), float(nota3)]
        datos = cargar_datos()
        datos.append({
            "Nombre": nombre,
            "Nota1": notas[0],
            "Nota2": notas[1],
            "Nota3": notas[2],
            "NotaFinal": calcular_nota(*notas)
        })
        guardar_datos(datos)
        messagebox.showinfo("Éxito", "Estudiante agregado exitosamente.")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Estudiante")
    ventana_agregar.configure(bg="#1e1e2f")
    ventana_agregar.geometry("300x400")
    
    # Centrar la ventana
    centrar_ventana(ventana_agregar)

    tk.Label(ventana_agregar, text="Nombre:", bg="#1e1e2f", fg="white").pack(pady=5)
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_agregar, text="Nota 1 (30%):", bg="#1e1e2f", fg="white").pack(pady=5)
    entry_nota1 = tk.Entry(ventana_agregar)
    entry_nota1.pack(pady=5)

    tk.Label(ventana_agregar, text="Nota 2 (30%):", bg="#1e1e2f", fg="white").pack(pady=5)
    entry_nota2 = tk.Entry(ventana_agregar)
    entry_nota2.pack(pady=5)

    tk.Label(ventana_agregar, text="Nota 3 (40%):", bg="#1e1e2f", fg="white").pack(pady=5)
    entry_nota3 = tk.Entry(ventana_agregar)
    entry_nota3.pack(pady=5)

    # Botón con tamaño fijo
    btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar, bg="white", fg="black", relief="raised", bd=3)
    btn_guardar.pack(pady=10, ipadx=50)  # ipadx para ajustar el ancho

# Función para ver el consolidado de calificaciones de todos los estudiantes
def ver_consolidado():
    datos = cargar_datos()
    if not datos:
        messagebox.showinfo("Información", "No hay registros.")
        return

    ventana_consolidado = tk.Toplevel()
    ventana_consolidado.title("Consolidado de Calificaciones")
    ventana_consolidado.configure(bg="#1e1e2f")
    ventana_consolidado.geometry("600x400")

    # Centrar la ventana
    centrar_ventana(ventana_consolidado)

    # Crear una tabla con ttk.Treeview
    tabla = ttk.Treeview(ventana_consolidado, columns=("Nombre", "Nota1", "Nota2", "Nota3", "NotaFinal"), show="headings")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Nota1", text="Nota 1")
    tabla.heading("Nota2", text="Nota 2")
    tabla.heading("Nota3", text="Nota 3")
    tabla.heading("NotaFinal", text="Nota Final")
    tabla.pack(fill="both", expand=True, padx=10, pady=10)

    for est in datos:
        tabla.insert("", "end", values=(est["Nombre"], est["Nota1"], est["Nota2"], est["Nota3"], f"{float(est['NotaFinal']):.2f}"))

# Función para consultar las notas de un estudiante específico
def consultar_notas():
    def buscar():
        nombre = entry_nombre.get()
        if not nombre:
            messagebox.showerror("Error", "Ingrese un nombre.")
            return

        for est in cargar_datos():
            if est["Nombre"].lower() == nombre.lower():
                messagebox.showinfo("Notas", f"Notas de {est['Nombre']}:\nNota 1: {est['Nota1']}\nNota 2: {est['Nota2']}\nNota 3: {est['Nota3']}\nNota Final: {float(est['NotaFinal']):.2f}")
                return
        messagebox.showerror("Error", "Estudiante no encontrado.")

    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("Consultar Notas")
    ventana_consultar.configure(bg="#1e1e2f")
    ventana_consultar.geometry("300x100")

    # Centrar la ventana
    centrar_ventana(ventana_consultar)

    tk.Label(ventana_consultar, text="Nombre del estudiante:", bg="#1e1e2f", fg="white").pack(pady=5)
    entry_nombre = tk.Entry(ventana_consultar)
    entry_nombre.pack(pady=5)

    # Botón con tamaño fijo
    btn_buscar = tk.Button(ventana_consultar, text="Buscar", command=buscar, bg="white", fg="black", relief="raised", bd=3)
    btn_buscar.pack(pady=10, ipadx=50)  # ipadx para ajustar el ancho

# Función para mostrar el menú del profesor
def menu_profesor():
    contrasena = simpledialog.askstring("Contraseña", "Ingrese la contraseña del profesor:", show="*")
    if contrasena != CONTRASENA_PROFESOR:
        messagebox.showerror("Error", "Contraseña incorrecta.")
        return

    ventana_profesor = tk.Toplevel()
    ventana_profesor.title("Menú Profesor")
    ventana_profesor.configure(bg="#1e1e2f")
    ventana_profesor.geometry("300x200")

    # Centrar la ventana
    centrar_ventana(ventana_profesor)

    # Botones con tamaño fijo
    btn_agregar = tk.Button(ventana_profesor, text="Agregar Estudiante", command=agregar_estudiante, bg="white", fg="black", relief="raised", bd=3)
    btn_agregar.pack(pady=10, ipadx=50)

    btn_consolidado = tk.Button(ventana_profesor, text="Ver Consolidado", command=ver_consolidado, bg="white", fg="black", relief="raised", bd=3)
    btn_consolidado.pack(pady=10, ipadx=50)

    btn_volver = tk.Button(ventana_profesor, text="Volver", command=ventana_profesor.destroy, bg="white", fg="black", relief="raised", bd=3)
    btn_volver.pack(pady=10, ipadx=50)

# Función principal para mostrar el menú general
def menu_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Gestión de Notas")
    ventana_principal.configure(bg="#1e1e2f")
    ventana_principal.geometry("400x300")

    # Centrar la ventana
    centrar_ventana(ventana_principal)

    # Estilo de fuente
    fuente = Font(family="Helvetica", size=12, weight="bold")

    tk.Label(ventana_principal, text="Bienvenido al Politécnico Internacional", bg="#1e1e2f", fg="white", font=fuente).pack(pady=20)

    # Botones con tamaño fijo
    btn_profesor = tk.Button(ventana_principal, text="Profesor", command=menu_profesor, bg="white", fg="black", relief="raised", bd=3, font=fuente)
    btn_profesor.pack(pady=10, ipadx=50)

    btn_estudiante = tk.Button(ventana_principal, text="Estudiante", command=consultar_notas, bg="white", fg="black", relief="raised", bd=3, font=fuente)
    btn_estudiante.pack(pady=10, ipadx=50)

    btn_salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.destroy, bg="white", fg="black", relief="raised", bd=3, font=fuente)
    btn_salir.pack(pady=10, ipadx=50)

    ventana_principal.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    inicializar_csv()
    menu_principal()