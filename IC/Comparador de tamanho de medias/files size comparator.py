import cv2 as cv
import numpy as np 
import base64
import os

directory = r'/home/almeida/Desktop/IC/Comparador de tamanho de medias/media'
os.chdir(directory) 

webcam = cv.VideoCapture(0)
ret, frame = webcam.read()
cv.imwrite("Foto.jpg", frame)

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

cv.imwrite("red.jpg", mask_red)
cv.imwrite("1.jpg", mask1)
cv.imwrite("2.jpg", mask2)


#FOTO ORIGINAL################################################
with open("Foto.jpg", "rb") as img_filefoto:
    my_string = base64.b64encode(img_filefoto.read())

strent= str(my_string)
print(len(strent))


#FOTO EM ESCALA VERMELHA E PRETA##############################
with open("red.jpg", "rb") as img_filered:
    my_stringred = base64.b64encode(img_filered.read())

strentred= str(my_stringred)
print(len(strentred))


#FOTO EM PRETO E BRANCO NORMAL################################
with open("1.jpg", "rb") as img_file1:
    my_string1 = base64.b64encode(img_file1.read())

strent1= str(my_string1)
print(len(strent1))


#FOTO EM PRETO E BRANCO TRATADA#######################################
with open("2.jpg", "rb") as img_file2:
    my_string2 = base64.b64encode(img_file2.read())

strent2= str(my_string2)
print(len(strent2))

cv.waitKey(0)
cv.destroyAllWindows()