### db.py - Módulo para la conexión y operaciones con MySQL
import mysql.connector
from mysql.connector import Error
import pandas as pd
from fpdf import FPDF
import tkinter as tk
from tkinter import ttk, messagebox


def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='192.168.20.122',
            user='politecnico',
            password='politecnico',
            database='gestion_usuarios'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None


def insertar_usuario(nombres, identificacion, tipo_id, correo, edad, genero):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombres, identificacion, tipo_id, correo, edad, genero) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (nombres, identificacion, tipo_id, correo, edad, genero)
            cursor.execute(sql, valores)
            conexion.commit()
            registrar_historial(cursor.lastrowid, "Inserción")
            print("Usuario agregado correctamente")
        except Error as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            conexion.close()


def modificar_usuario(id_usuario, nombres, identificacion, tipo_id, correo, edad, genero):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "UPDATE usuarios SET nombres=%s, identificacion=%s, tipo_id=%s, correo=%s, edad=%s, genero=%s WHERE id=%s"
            valores = (nombres, identificacion, tipo_id, correo, edad, genero, id_usuario)
            cursor.execute(sql, valores)
            conexion.commit()
            registrar_historial(id_usuario, "Modificación")
            print("Usuario modificado correctamente")
        except Error as e:
            print(f"Error al modificar usuario: {e}")
        finally:
            conexion.close()


def eliminar_usuario(id_usuario):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM usuarios WHERE id=%s"
            cursor.execute(sql, (id_usuario,))
            conexion.commit()
            registrar_historial(id_usuario, "Eliminación")
            print("Usuario eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            conexion.close()


def registrar_historial(usuario_id, accion):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO historial_modificaciones (usuario_id, accion) VALUES (%s, %s)"
            valores = (usuario_id, accion)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Historial actualizado correctamente")
        except Error as e:
            print(f"Error al registrar historial: {e}")
        finally:
            conexion.close()


def leer_usuarios():
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            datos = cursor.fetchall()
            return datos
        except Error as e:
            print(f"Error al leer usuarios: {e}")
        finally:
            conexion.close()
    return []


def exportar_excel():
    datos = leer_usuarios()
    df = pd.DataFrame(datos, columns=['ID', 'Nombres', 'Identificación', 'Tipo ID', 'Correo', 'Edad', 'Género', 'Fecha Registro'])
    df.to_excel("usuarios.xlsx", index=False)
    print("Datos exportados a usuarios.xlsx")


def exportar_csv():
    datos = leer_usuarios()
    df = pd.DataFrame(datos, columns=['ID', 'Nombres', 'Identificación', 'Tipo ID', 'Correo', 'Edad', 'Género', 'Fecha Registro'])
    df.to_csv("usuarios.csv", index=False)
    print("Datos exportados a usuarios.csv")


def exportar_pdf():
    datos = leer_usuarios()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte de Usuarios", ln=True, align='C')
    for row in datos:
        pdf.cell(200, 10, txt=str(row), ln=True)
    pdf.output("usuarios.pdf")
    print("Datos exportados a usuarios.pdf")

