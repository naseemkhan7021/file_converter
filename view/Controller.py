from fpdf import FPDF
import img2pdf

# writeble file to pdf file


def txtTopdfConvert(textPath, pdfPath):
    pdf = FPDF()
    pdf.add_page()
    print(pdf.fonts)
    pdf.set_font('Times', size=10)
    rfile = open(textPath, 'r')
    # insert text into pdf

    for i in rfile:
        pdf.cell(100, 10, txt=i, ln=1, align='L')
    pdf.output(pdfPath)

    # print('this is txtTopdf')

# img file to pdf file


def imgTopdf(imgPath, pdfPath):
    print('this is imgTopdf')
    try:
        with open(pdfPath, 'wb') as wfile:
            wfile.write(img2pdf.convert(imgPath))
            return 'Success to creat pdf'

    except Exception:
        return 'Somthing is goes wrong please try again !!'

# def examle(oldfile,newfile):
#     with open(oldfile,'r') as rfile:
#         data = rfile.read()
#         print(data)
    # with open(newfile,'w') as wfile:
    #     wfile.write(data)
#             print('success to make file')

# examle('ssdel.py','newFile.txt')
