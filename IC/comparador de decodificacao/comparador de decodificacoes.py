import cv2 as cv
import numpy as np 
import os
import base64
import serial
import time
import base128

inicio = time.time()

#ser = serial.Serial('/dev/ttyUSB1', 9600)
directory = r'/home/almeida/Desktop/IC/comparador de decodificacao/media'
os.chdir(directory) 

webcam = cv.VideoCapture(0)
ret, frame = webcam.read()
cv.imwrite("Foto.jpg", frame)
webcam.release()

img = cv.imread('Foto.jpg')

resize = (960,540)

img_resize = cv.resize(img, resize)

img_color = cv.applyColorMap(img, cv.COLORMAP_JET )
color_resize = cv.resize(img_color, resize)
color2hsv = cv.cvtColor(color_resize, cv.COLOR_BGR2HSV)

lowerRed = np.array([0,50,50])
upperRed = np.array([5,255,255])
mask1 = cv.inRange(color2hsv, lowerRed, upperRed)

lower_orange = np.array([10, 100, 20])
upper_orange = np.array([25, 255, 255])
mask2 = cv.inRange(color2hsv, lower_orange, upper_orange)

mask_red = cv.bitwise_and(color_resize,color_resize, mask= mask1)

cv.imwrite("1.jpg", mask1)

#FOTO EM PRETO E BRANCO NORMAL################################
with open("1.jpg", "rb") as img_file1:
    my_string1 = base64.b64encode(img_file1.read())
    my_string2 = base64.b85encode(my_string1)

dados1= str(my_string1)
dados2= str(my_string2)

print(len(dados1))

print(len(dados2))


cv.waitKey(0)
cv.destroyAllWindows()