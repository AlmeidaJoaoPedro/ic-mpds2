import cv2 as cv
import serial
import os
#instalar essas bibs abaixo
# Define a porta serial e a velocidade de comunicação
ser = serial.Serial('/dev/ttyUSB0', 9600)

a = 3


while (a == 3):
    if ser.in_waiting > 0:
        x = ser.read()
        y = x.decode('UTF-8')
        z = str(y)
        a = a + 1
    


if str (z) == "1":
    msg = "Vazamento"
    print(msg)

if str(z) == "0":
    msg = "Sem vazamento"
    print(msg)

#os.chdir("Desktop/IC")

arquivo = open('response.txt', 'w+')
arquivo.writelines(msg)