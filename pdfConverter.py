# Convert a PDF file to a image or a image to a PDF file. 

import fitz
import img2pdf
import os
from PIL import Image

print('Do you want to convert a pdf to image or a image to a pdf?')
print('Enter 0 for pdf --> image and 1 for image --> pdf:')
ans = int(input())

if (ans == 0):
    print("Enter the name of the pdf")
    file = input()
    pdf = fitz.open(file)
    print('Enter the page no., for converting that page into a image')
    no = int(input())
    page = pdf.load_page(no)
    pix = page.get_pixmap()
    print('Enter a name, to save this image')
    name = input()
    pix.save(name)
    print('File converted successfully!!')
else:
    print('Please enter the full file path to the image:')
    path = input()
    print('Enter a name with which you want to save this file:')
    finalPDF = input()
    try:
        with Image.open(path) as im:
            if im.mode == "RGBA":
                im = im.convert("RGB")
        im.save(finalPDF, "PDF")
        im.close()
        print("SUCCESSFULLY CONVERTED!!")
    except NameError:
        print('Please enter a valid path to the image')
