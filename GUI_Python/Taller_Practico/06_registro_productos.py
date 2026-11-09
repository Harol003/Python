import tkinter as tk
from tkinter import ttk, messagebox

def registrar():
    nombre = entrada_nombre.get().strip()
    precio = entrada_precio.get().strip()
    cantidad = entrada_cantidad.get().strip()
    categoria = lista_categoria.get()
    if not nombre or not precio or not cantidad or not categoria:
        messagebox.showwarning("Datos incompletos", "Completa todos los campos.")
        return
    try:
        precio_num = float(precio)
        cantidad_num = int(cantidad)
        if precio_num < 0 or cantidad_num < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Datos inválidos", "Precio y cantidad deben ser números válidos no negativos.")
        return
    messagebox.showinfo("Producto registrado",
                        f"Producto: {nombre}\\nPrecio: ${precio_num:.2f}\\n"
                        f"Cantidad: {cantidad_num}\\nCategoría: {categoria}")

def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_precio.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)
    lista_categoria.set("")
    entrada_nombre.focus()

ventana = tk.Tk()
ventana.title("Registro de productos")
ventana.geometry("480x420")
ventana.resizable(False, False)
ventana.configure(bg="#F5F5F5")

tk.Label(ventana, text="REGISTRO DE PRODUCTOS", font=("Arial", 16, "bold"),
         bg="#F5F5F5", fg="#145A32").pack(pady=18)

formulario = tk.Frame(ventana, bg="#F5F5F5")
formulario.pack(pady=5)

tk.Label(formulario, text="Nombre del producto:", bg="#F5F5F5").grid(row=0, column=0, sticky="e", padx=8, pady=9)
entrada_nombre = tk.Entry(formulario, width=25)
entrada_nombre.grid(row=0, column=1, pady=9)

tk.Label(formulario, text="Precio:", bg="#F5F5F5").grid(row=1, column=0, sticky="e", padx=8, pady=9)
entrada_precio = tk.Entry(formulario, width=25)
entrada_precio.grid(row=1, column=1, pady=9)

tk.Label(formulario, text="Cantidad:", bg="#F5F5F5").grid(row=2, column=0, sticky="e", padx=8, pady=9)
entrada_cantidad = tk.Entry(formulario, width=25)
entrada_cantidad.grid(row=2, column=1, pady=9)

tk.Label(formulario, text="Categoría:", bg="#F5F5F5").grid(row=3, column=0, sticky="e", padx=8, pady=9)
lista_categoria = ttk.Combobox(formulario, values=["Tecnología", "Hogar", "Ropa", "Alimentos"],
                               state="readonly", width=23)
lista_categoria.grid(row=3, column=1, pady=9)

tk.Button(ventana, text="REGISTRAR", width=20, bg="#198754", fg="white",
          command=registrar).pack(pady=8)
tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=3)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=3)

ventana.mainloop()
