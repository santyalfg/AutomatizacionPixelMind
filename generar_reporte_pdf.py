# Fecha creacion: 13/11/2025
# Ultima fecha de modificación: 13/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo es el archivo base del reporte PDF

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import os,datetime
from confiest import test_results

def generar_reporte_pdf(nombre_archivo="Reporte_pruebas.pdf")
c= canvas.Canvas(nombre_archivo, pagesizes=A4)
width , height = A4

#Encabezado PDF
c.setFont("Helvetica-Bold",16)
c.drawString(2*cm, height - 2*cm, "Reporte de pruebas automatizadas")
c.setFont("Helvetica",10)
c.drawString(2*cm, height - 2.6*cm,f"fecha de ejecucion:
{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

y = height - 4*cm

for result in test_results:
    c.setFont("Helvetica-Bold",12)
    c.drawString(2*cm,y,f"Test:{result['name']}")
    y- 0,5*cm
    c.setFont("Helvetica",10)
    c.drawString(2*cm,y,f"Resultado:
    {result['outcome'].upper()} | Duracion:
    {result['duration']}s | Hora: {result['timestamp']}")
    y-=0.7*cm

    #Insertar pantallazos 
    screenshots = [f for f in os.listdir("screenshots") if result['name']in f]
        for shot in screenshots:
            path = os.path.join("screenshots",shot)
            if os.path.exists(path):
                y-=9*cm
                c.drawlmage(path,2*cm,y,width=12*cm, height=8*cm)
                y -= 0,5*cm
                if y < 5*cm
                c.showPage()
                y=height - 3*cm

c.save()
print(f"Reporte PDF generado:
{nombre_archivo}")