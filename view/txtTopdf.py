# import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
import os
# writePDf = PyPDF2.PdfFileWriter()


# def textTopdf(textfile, pdfPath):
#     with open(textfile, 'r',encoding='utf-8') as rfile:
#         data = rfile.read
#         writePDf.addAttachment(pdfPath, data)

def txtTopdfConvert(textData, pdfPath):
    canvas = Canvas(pdfPath, pagesize=A4)
    print(f'path basename is {pdfPath}')
    canvas.setFont('Times-Roman', 12)
    # print(textData)
    with open('newFile.txt', 'wb') as wfile:
        wfile.write(textData)
    canvas.drawString(0.5 * cm, 5 * cm, textData)
    canvas.save()
    print('this is txtTopdf')

# def examle(oldfile,newfile):
#     with open(oldfile,'r') as rfile:
#         data = rfile.read()
#         print(data)
    # with open(newfile,'w') as wfile:
    #     wfile.write(data)
#             print('success to make file')

# examle('ssdel.py','newFile.txt')
