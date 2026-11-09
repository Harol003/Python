
# ================================================
# PROGRAMA DEMOSTRATIVO DE COMPONENTES TKINTER
# ================================================

# Importamos tkinter para crear interfaces gráficas
import tkinter as tk

# Importamos ttk para utilizar componentes adicionales
from tkinter import ttk

# Importamos messagebox para mostrar mensajes emergentes
from tkinter import messagebox

# Importamos filedialog para seleccionar archivos
from tkinter import filedialog

# Importamos colorchooser para seleccionar colores
from tkinter import colorchooser


# ================================================
# FUNCIONES DEL PROGRAMA
# ================================================

# Función que se ejecuta al presionar el botón
def mostrar_mensaje():
    # Obtenemos el texto escrito en el campo de entrada
    nombre = entrada_nombre.get()

    # Verificamos que el campo no esté vacío
    if nombre == "":
        # Mostramos una advertencia
        messagebox.showwarning("Advertencia", "Escriba su nombre")
    else:
        # Mostramos un mensaje de bienvenida
        messagebox.showinfo("Bienvenido", "Hola " + nombre)


# Función para limpiar el campo de entrada
def limpiar():
    # Eliminamos todo el contenido del Entry
    entrada_nombre.delete(0, tk.END)


# Función para abrir una ventana secundaria
def abrir_ventana():
    # Creamos una ventana secundaria
    nueva = tk.Toplevel(ventana)

    # Establecemos el título de la ventana
    nueva.title("Ventana secundaria")

    # Definimos sus dimensiones
    nueva.geometry("300x150")

    # Creamos una etiqueta dentro de la ventana secundaria
    tk.Label(nueva, text="Esta es otra ventana").pack(pady=20)

    # Creamos un botón para cerrar la ventana secundaria
    tk.Button(nueva, text="Cerrar", command=nueva.destroy).pack()


# Función para seleccionar un archivo
def seleccionar_archivo():
    # Abrimos el explorador de archivos
    archivo = filedialog.askopenfilename()

    # Si se seleccionó un archivo, mostramos su ruta
    if archivo:
        messagebox.showinfo("Archivo seleccionado", archivo)


# Función para seleccionar un color
def seleccionar_color():
    # Abrimos el selector de colores
    color = colorchooser.askcolor()

    # Verificamos que se haya elegido un color
    if color[1]:
        # Cambiamos el fondo de la ventana
        ventana.config(bg=color[1])


# Función para actualizar el valor del Scale
def actualizar_escala(valor):
    # Mostramos el valor seleccionado
    etiqueta_escala.config(text="Valor: " + str(int(float(valor))))


# Función para mostrar el valor del Spinbox
def mostrar_numero():
    # Obtenemos el número seleccionado
    numero = spin_numero.get()

    # Mostramos el número seleccionado
    messagebox.showinfo("Número", "Seleccionaste: " + numero)


# ================================================
# CREACIÓN DE LA VENTANA PRINCIPAL
# ================================================

# Creamos la ventana principal
ventana = tk.Tk()

# Establecemos el título
ventana.title("Componentes gráficos de Tkinter")

# Definimos el tamaño de la ventana
ventana.geometry("950x800")

# Evitamos modificar el tamaño de la ventana
ventana.resizable(False, False)


# ================================================
# MENÚ PRINCIPAL
# ================================================

# Creamos una barra de menú
barra_menu = tk.Menu(ventana)

# Creamos un menú llamado Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)

# Agregamos una opción para abrir archivos
menu_archivo.add_command(
    label="Abrir archivo",
    command=seleccionar_archivo
)

# Agregamos una opción para cerrar el programa
menu_archivo.add_command(
    label="Salir",
    command=ventana.destroy
)

# Agregamos el menú Archivo a la barra principal
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Creamos un menú llamado Opciones
menu_opciones = tk.Menu(barra_menu, tearoff=0)

# Agregamos una opción para seleccionar colores
menu_opciones.add_command(
    label="Cambiar color",
    command=seleccionar_color
)

# Agregamos el menú Opciones a la barra principal
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

# Mostramos la barra de menú en la ventana
ventana.config(menu=barra_menu)


# ================================================
# TITULO PRINCIPAL
# ================================================

# Creamos una etiqueta para el título
titulo = tk.Label(
    ventana,
    text="DEMOSTRACIÓN DE COMPONENTES TKINTER",
    font=("Arial", 18, "bold")
)

# Ubicamos el título en la ventana
titulo.pack(pady=10)


# ================================================
# PANEDWINDOW: DIVIDIR LA VENTANA
# ================================================

# Creamos un contenedor que permite dividir la ventana
panel = tk.PanedWindow(
    ventana,
    orient=tk.HORIZONTAL,
    sashwidth=5
)

# Ubicamos el contenedor
panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Creamos el panel izquierdo
izquierdo = tk.Frame(panel, padx=10, pady=10)

# Creamos el panel derecho
derecho = tk.Frame(panel, padx=10, pady=10)

# Agregamos los dos paneles al contenedor
panel.add(izquierdo)

# Agregamos el segundo panel
panel.add(derecho)


# ================================================
# FRAME Y LABELFRAME
# ================================================

# Creamos un Frame para agrupar elementos
marco = tk.Frame(izquierdo)

# Ubicamos el Frame
marco.pack(fill="x", pady=5)

# Creamos un LabelFrame con un título
grupo = tk.LabelFrame(
    izquierdo,
    text="Etiquetas y entradas",
    padx=10,
    pady=10
)

# Ubicamos el LabelFrame
grupo.pack(fill="x", pady=5)


# ================================================
# LABEL: ETIQUETA
# ================================================

# Creamos una etiqueta de texto
tk.Label(grupo, text="Escriba su nombre:").pack(anchor="w")

# ================================================
# ENTRY: CAMPO DE ENTRADA
# ================================================

# Creamos una caja para ingresar texto
entrada_nombre = tk.Entry(grupo, width=30)

# Ubicamos la caja de entrada
entrada_nombre.pack(pady=5)

# ================================================
# BUTTON: BOTONES
# ================================================

# Creamos un botón para mostrar un mensaje
tk.Button(
    grupo,
    text="SALUDAR",
    command=mostrar_mensaje
).pack(pady=3)

# Creamos un botón para limpiar
tk.Button(
    grupo,
    text="LIMPIAR",
    command=limpiar
).pack(pady=3)

# Creamos un botón para abrir otra ventana
tk.Button(
    grupo,
    text="ABRIR VENTANA",
    command=abrir_ventana
).pack(pady=3)


# ================================================
# MESSAGE: MENSAJE DE TEXTO
# ================================================

# Creamos un componente Message
mensaje = tk.Message(
    izquierdo,
    text="Tkinter permite crear aplicaciones gráficas utilizando Python.",
    width=300
)

# Ubicamos el mensaje
mensaje.pack(pady=5)


# ================================================
# CHECKBUTTON: CASILLA DE VERIFICACIÓN
# ================================================

# Creamos una variable para guardar el estado de la casilla
aceptar = tk.BooleanVar()

# Creamos una casilla de selección
casilla = tk.Checkbutton(
    izquierdo,
    text="Acepto las condiciones",
    variable=aceptar
)

# Ubicamos la casilla
casilla.pack(anchor="w", pady=5)


# ================================================
# RADIOBUTTON: BOTONES DE OPCIÓN
# ================================================

# Creamos una variable para guardar la opción seleccionada
opcion = tk.StringVar(value="Python")

# Creamos el primer botón de opción
tk.Radiobutton(
    izquierdo,
    text="Python",
    variable=opcion,
    value="Python"
).pack(anchor="w")

# Creamos el segundo botón de opción
tk.Radiobutton(
    izquierdo,
    text="Java",
    variable=opcion,
    value="Java"
).pack(anchor="w")


# ================================================
# COMBOBOX: LISTA DESPLEGABLE
# ================================================

# Creamos una etiqueta
tk.Label(izquierdo, text="Seleccione una ciudad:").pack(anchor="w")

# Creamos una lista desplegable
lista_desplegable = ttk.Combobox(
    izquierdo,
    values=["Bogotá", "Medellín", "Cali", "Barranquilla"],
    state="readonly"
)

# Seleccionamos el primer elemento
lista_desplegable.current(0)

# Ubicamos la lista desplegable
lista_desplegable.pack(pady=5)


# ================================================
# SPINBOX: SELECTOR NUMÉRICO
# ================================================

# Creamos una etiqueta para el Spinbox
tk.Label(izquierdo, text="Seleccione una edad:").pack(anchor="w")

# Creamos un selector de números entre 1 y 100
spin_numero = tk.Spinbox(
    izquierdo,
    from_=1,
    to=100,
    width=10
)

# Ubicamos el selector numérico
spin_numero.pack(pady=5)

# Creamos un botón para mostrar el número
tk.Button(
    izquierdo,
    text="MOSTRAR NÚMERO",
    command=mostrar_numero
).pack(pady=3)


# ================================================
# SCALE: CONTROL DESLIZANTE
# ================================================

# Creamos una etiqueta para el control deslizante
tk.Label(derecho, text="Seleccione un valor:").pack(anchor="w")

# Creamos un control para seleccionar valores entre 0 y 100
escala = tk.Scale(
    derecho,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=actualizar_escala
)

# Ubicamos el control deslizante
escala.pack(fill="x", pady=5)

# Creamos una etiqueta para mostrar el valor
etiqueta_escala = tk.Label(derecho, text="Valor: 0")

# Ubicamos la etiqueta
etiqueta_escala.pack()


# ================================================
# LISTBOX: LISTA DE ELEMENTOS
# ================================================

# Creamos una etiqueta para la lista
tk.Label(derecho, text="Lista de materias:").pack(anchor="w")

# Creamos un contenedor para la lista y su barra
contenedor_lista = tk.Frame(derecho)

# Ubicamos el contenedor
contenedor_lista.pack(fill="x", pady=5)

# Creamos una barra de desplazamiento vertical
barra_lista = tk.Scrollbar(contenedor_lista)

# Ubicamos la barra de desplazamiento
barra_lista.pack(side=tk.RIGHT, fill=tk.Y)

# Creamos una lista de elementos
lista = tk.Listbox(
    contenedor_lista,
    height=4,
    yscrollcommand=barra_lista.set
)

# Agregamos materias a la lista
lista.insert(tk.END, "Matemáticas")
lista.insert(tk.END, "Tecnología")
lista.insert(tk.END, "Ciencias")
lista.insert(tk.END, "Inglés")

# Ubicamos la lista
lista.pack(side=tk.LEFT, fill="x", expand=True)

# Conectamos la barra con la lista
barra_lista.config(command=lista.yview)


# ================================================
# TEXT: CAMPO DE TEXTO MULTILÍNEA
# ================================================

# Creamos una etiqueta
tk.Label(derecho, text="Escriba una observación:").pack(anchor="w")

# Creamos un campo de texto de varias líneas
campo_texto = tk.Text(derecho, width=35, height=4)

# Ubicamos el campo de texto
campo_texto.pack(pady=5)


# ================================================
# CANVAS: ÁREA DE DIBUJO
# ================================================

# Creamos una etiqueta
tk.Label(derecho, text="Área de dibujo:").pack(anchor="w")

# Creamos un espacio para dibujar
lienzo = tk.Canvas(
    derecho,
    width=300,
    height=120,
    bg="white",
    highlightthickness=1
)

# Ubicamos el lienzo
lienzo.pack(pady=5)

# Dibujamos un rectángulo
lienzo.create_rectangle(
    20, 20, 120, 90,
    outline="blue",
    width=3
)

# Dibujamos un círculo
lienzo.create_oval(
    150, 20, 230, 90,
    outline="red",
    width=3
)

# Dibujamos una línea
lienzo.create_line(
    240, 20, 280, 90,
    fill="green",
    width=3
)


# ================================================
# MENUBUTTON: BOTÓN CON MENÚ
# ================================================

# Creamos un botón que despliega opciones
boton_menu = tk.Menubutton(
    derecho,
    text="MÁS OPCIONES",
    relief=tk.RAISED
)

# Creamos el menú del botón
menu_desplegable = tk.Menu(
    boton_menu,
    tearoff=0
)

# Agregamos una opción al menú
menu_desplegable.add_command(
    label="Seleccionar archivo",
    command=seleccionar_archivo
)

# Agregamos otra opción al menú
menu_desplegable.add_command(
    label="Seleccionar color",
    command=seleccionar_color
)

# Asociamos el menú al botón
boton_menu.config(menu=menu_desplegable)

# Ubicamos el botón
boton_menu.pack(pady=5)


# ================================================
# BOTÓN FINALIZAR
# ================================================

# Creamos un botón para cerrar el programa
tk.Button(
    ventana,
    text="SALIR DEL PROGRAMA",
    command=ventana.destroy,
    width=25
).pack(pady=10)


# ================================================
# INICIAR EL PROGRAMA
# ================================================

# Mantiene abierta la ventana y espera acciones del usuario
ventana.mainloop()
