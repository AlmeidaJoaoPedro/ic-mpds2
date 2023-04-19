import cv2 as cv
import numpy as np 
import os
import base64
import serial
import time

inicio = time.time()

ser = serial.Serial('/dev/ttyUSB1', 9600)
directory = r'/home/almeida/Desktop/IC/Teste envio/media'
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

strent= str(my_string1)
print(len(strent))

arquivo = open('image64.txt', 'w+')
arquivo.writelines(strent)


MAX_PACKET_SIZE = 50

packets = [strent[i:i+MAX_PACKET_SIZE] for i in range(0, len(strent), MAX_PACKET_SIZE)]

for packet in packets:
    ser.write(packet.encode("UTF-8"))
    time.sleep(2)


# file = open('image64.txt', 'rb')
# encoded_data = file.read()
# file.close()
fim = time.time()

tempo = fim - inicio

tempo_min = tempo/60

print(tempo_min)


cv.waitKey(0)
cv.destroyAllWindows()