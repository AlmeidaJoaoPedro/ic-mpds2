import cv2 as cv
import numpy as np 
import serial
from PIL import Image
import os

# captura e armazenamento em uma variavel
webcam = cv.VideoCapture(0)
ret, frame = webcam.read()
cv.imwrite("Foto.png", frame)

# transformando em matriz string
imgPIL = Image.open("Foto.png")
arr = np.asarray(imgPIL)
img_enc = str(arr)
print(img_enc)

# envia matriz para esp
ser = serial.Serial('COM3', 115200)
ser.write(img_enc.encode('UTF-8'))

os.remove("Foto.png")

cv.waitKey(0)
cv.destroyAllWindows()