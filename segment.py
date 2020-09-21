# Import libraries
import PIL 
from PIL import Image 
import fitz
import dateparser
import pytesseract
from pytesseract import image_to_string 
import sys 
from pdf2image import convert_from_path 
import os 
  
# Path of the image 
path = r"C:\Users\Atharva\Desktop\Incture\Output images\BigRockrot.png"
doc = fitz.open(path)
#Invoice is of only one page
page = doc.loadPage(0) 
zoom_x = 1.0  # horizontal zoom
zomm_y = 1.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zomm_y)  
pix = page.getPixmap(matrix = mat)
output = r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock_output.png"
pix.writePNG(output)
img = Image.open(output)  

width, height = img.size
print (width,height)

appDict = {}

#Extracting issuer
bbox1 = (0,100,800,400)
working_slice = img.crop(bbox1)
issuer = working_slice.save(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-1-issuer.png")
image = Image.open(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-1-issuer.png")
text1 = pytesseract.image_to_string(image)
print("\n ---- Text Extraction ----\n",text1)
info = text1.splitlines()
value1 = info[0]
appDict["issuer"] = value1
print(appDict)

#Extracting invoice date
bbox2 = (1550,330,2050,500)
working_slice = img.crop(bbox2)
invoice = working_slice.save(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-2-invoice.png")
image = Image.open(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-2-invoice.png")
text2 = pytesseract.image_to_string(image)
print("\n ---- Text Extraction ----\n",text2)
info = text2.split(" ")
print(info)
value2 = info[1]
invoice_date = dateparser.parse(value2) 
appDict["invoice_date"] = invoice_date



#Extracting po number
bbox3 = (2050,1200,2500,1300)
working_slice = img.crop(bbox3)
issuer = working_slice.save(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-3-ponumber.png")
image = Image.open(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-3-ponumber.png")
text3 = pytesseract.image_to_string(image)
print("\n ---- Text Extraction ----\n",text3)
info = text3.split(" ")
value3 = info[0]
appDict["PO. Number"] = value3



#Extracting amount
bbox4 = (2000,2500,width,height)
working_slice = img.crop(bbox4)
issuer = working_slice.save(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-4-amount.png")
image = Image.open(r"C:\Users\Atharva\Desktop\Incture\BigRock\BigRock-4-amount.png")
text4 = pytesseract.image_to_string(image)
print("\n ---- Text Extraction ----\n",text4)
appDict["Amount"] = text4

print(appDict)

import json
app_json = json.dumps(appDict)
print(app_json)