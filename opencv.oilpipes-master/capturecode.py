import cv2
import numpy as np 
import serial as ser
from PIL import Image
import os

#img_path = r"ic-mpds2/opencv.oilpipes-master/Foto.png"
#directory = r"ic-mpds2/opencv.oilpipes-master"

#############################################################################ser = ser.Serial('/dev/ttyUSB1', 9600)

#captura e armazenamento em uma variavel
webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()
cv2.imwrite("Foto.jpeg", frame)
#cv2.imshow("set", frame)

#definindo o diretorio
Path1 = os.path.normpath("Foto.jpeg")
imgPIL = cv2.imread(Path1)

#transformando em array
img = Image.open('Foto.jpeg') 
numpydata = np.asarray(img)

str_image=(str(numpydata))

print(str_image)

chars = '[].\n'
res = str_image.translate(str.maketrans('','', chars))

x = res.split(" ")

print(x)


#fazendo a conversao de volta
####################################################new_img = Image.fromarray(numpydata)
#######################################################new_img.save("teste.jpeg")

#escrevendo no txt
#arquivo = open('image.txt', 'w+')
#str_image=(str(numpydata))
#arquivo.writelines(str_image)

#print(len(numpydata))

# envia matriz 
##########################################################################ser.writelines(str_image.encode('UTF-8'))
# os.remove("/ic-mpds2/Foto.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
