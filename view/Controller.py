from fpdf import FPDF
import img2pdf
import os
from wand.image import Image, Color


# writeble file to pdf file
def txtTopdfConvert(textPath, pdfPath):
    """
    This functions is usefull for making txt file to pdf file 
    generatore
    it's take two paramiter @textPath and pdfPath
    """
    # pdf configrations
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', size=10)
    try:
        rfile = open(textPath, 'r')
        # insert text into pdf
        for i in rfile:
            pdf.cell(100, 10, txt=i, ln=1, align='L')
        pdf.output(pdfPath)
        return True
    except Exception:
        os.remove(pdfPath)
        return 'Please try to input writeble file like who open in notepade'

    # print('this is txtTopdf')
# remove alpha from imgs


def removeAlpha(imgPath):
    """
    This functions is usefully to remove alpha channel frome the imgas
    (png file include the alpha channels)
    """
    with Image(filename=imgPath) as img:
        print('this is alpha img')
        noAlpha = False
        alpha = img.alpha_channel
        if not alpha:
            noAlpha = True
            return noAlpha
        else:
            try:
                img.alpha_channel = 'remove'
                img.background_color = Color('white')
                img.save(imgPath)
                noAlpha = True
                
            except Exception as error:
                print('error on line 37 ', error)
                noAlpha = False
                
    return noAlpha

# img file to pdf file


def imgTopdf(imgPath, pdfPath):
    '''
    this fungtions is use to conver img file in to pdf file
    '''
    print('this is imgTopdf')
    print('img path is ', imgPath)
    if not removeAlpha(imgPath):
        os.remove(pdfPath)
        return 'Please try another image'
    try:
        with open(pdfPath, 'wb') as wfile:
            wfile.write(img2pdf.convert(imgPath))
        return True
    except Exception:
        os.remove(pdfPath)
        return 'try to change thare background or use anothor imgage'

# def examle(oldfile,newfile):
#     with open(oldfile,'r') as rfile:
#         data = rfile.read()
#         print(data)
    # with open(newfile,'w') as wfile:
    #     wfile.write(data)
#             print('success to make file')

# examle('ssdel.py','newFile.txt')
