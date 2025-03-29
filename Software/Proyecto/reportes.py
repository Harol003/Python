### reportes.py - Módulo para generación de reportes en PDF y CSV
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from db import leer_usuarios

def generar_reporte():
    usuarios = leer_usuarios()
    
    if not usuarios:
        print("No hay datos para generar el reporte.")
        return

    archivo_pdf = "reporte_usuarios.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    c.drawString(30, 750, "Reporte de Usuarios")
    c.drawString(30, 735, "-" * 80)

    y = 720
    encabezados = ["ID", "Nombres", "ID", "Tipo ID", "Correo", "Edad", "Género", "Fecha Registro"]
    c.drawString(30, y, " | ".join(encabezados))
    c.drawString(30, y - 5, "-" * 80)

    y -= 20

    for usuario in usuarios:
        c.drawString(30, y, " | ".join(map(str, usuario)))
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()
    print(f"Reporte generado: {archivo_pdf}")

if __name__ == "__main__":
    generar_reporte()
