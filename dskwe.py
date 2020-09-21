#Importing the packages
import numpy as np
import argparse
from cv2 import cv2
from PIL import Image
import PIL 
import sys 
from pdf2image import convert_from_path 
import os 

# Path of the pdf 
PDF_file = r"C:\Users\Atharva\Desktop\Digitized PDF\Big Rock.pdf"

# Store all the pages of the PDF in a variable as an image
pages = convert_from_path(PDF_file, 400) 
for page in pages:
     page.save(r'C:\Users\Atharva\Desktop\Incture\Output images\BigRockout.png', 'PNG')

#import the image
img = cv2.imread(r'C:\Users\Atharva\Desktop\Incture\Output images\BigRockout.png')


#convert the image into grayscale and invert the background and the foreground
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray, mask= None)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('thresh',gray)
cv2.waitKey(0)

#Deskew the image by identifying the angle of rotation and correcting it back to straighten the image
coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", thresh)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0) 
filename = r'C:\Users\Atharva\Desktop\Incture\Output images\BigRockrot.png'
cv2.imwrite(filename, rotated)
