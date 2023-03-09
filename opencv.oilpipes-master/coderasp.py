#as bibliotecas nao estao apresentando mais problemas de importacao
import cv2
import numpy as np 
import serial
from PIL import Image
import os

#img_path = r"ic-mpds2/opencv.oilpipes-master/Foto.png"
#directory = r"ic-mpds2/opencv.oilpipes-master"

ser = serial.Serial('/dev/ttyUSB0', 9600)

#captura e armazenamento em uma variavel
webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()
os.chdir("ic-mpds2/opencv.oilpipes-master")
cv2.imwrite("Foto.png", frame)

#img_path = r"ic-mpds2/opencv.oilpipes-master/Foto.png"

# transformando em matriz string
Path1 = os.path.normpath("Foto.png")
imgPIL = cv2.imread(Path1)

arr = np.asarray(imgPIL)
img_enc = str(arr)

# envia matriz 

ser.write(img_enc.encode('UTF-8'))
os.remove("Foto.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
