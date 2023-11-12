import pytesseract
import cv2
from PIL import Image
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_cv = cv2.imread('testing/test.png')
data = pytesseract.image_to_string(img_cv)
print(data)