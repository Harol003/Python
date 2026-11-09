import tkinter as tk
from tkinter import messagebox

def ingresar():
    usuario = entrada_usuario.get().strip()
    clave = entrada_clave.get()
    if not usuario or not clave:
        messagebox.showwarning("Campos vacíos", "Escribe el usuario y la contraseña.")
    else:
        messagebox.showinfo("Bienvenido", f"Hola, {usuario}. Has ingresado correctamente.")

def limpiar():
    entrada_usuario.delete(0, tk.END)
    entrada_clave.delete(0, tk.END)
    entrada_usuario.focus()

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("400x350")
ventana.resizable(False, False)
ventana.configure(bg="#FFFFFF")

tk.Label(ventana, text="INICIO DE SESIÓN", font=("Arial", 17, "bold"),
         bg="#FFFFFF", fg="#003366").pack(pady=25)

tk.Label(ventana, text="Usuario:", bg="#FFFFFF").pack()
entrada_usuario = tk.Entry(ventana, width=28, font=("Arial", 11))
entrada_usuario.pack(pady=7)

tk.Label(ventana, text="Contraseña:", bg="#FFFFFF").pack()
entrada_clave = tk.Entry(ventana, width=28, font=("Arial", 11), show="*")
entrada_clave.pack(pady=7)

tk.Button(ventana, text="INGRESAR", width=20, bg="#007BFF", fg="white",
          command=ingresar).pack(pady=10)
tk.Button(ventana, text="LIMPIAR", width=20, bg="#808080", fg="white",
          command=limpiar).pack(pady=4)
tk.Button(ventana, text="SALIR", width=20, bg="#DC3545", fg="white",
          command=ventana.destroy).pack(pady=4)

ventana.mainloop()
