import cv2
import serial
import os

#instalar esse abaixo
import base64

#definindo a porta serial e o baud rate
ser = serial.Serial('/dev/ttyUSB0', 9600)

#captura e armazenamento em uma variavel
webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()

cv2.imwrite("Foto.png", frame)

Path1 = os.path.normpath("Foto.png")

#transformando a imagem em base64
with open('Foto.png', "rb") as fid:
    data = fid.read()
b64_bytes = base64.b64encode(data)

#transformando em string
b64_string = b64_bytes.decode()

# enviando a string decodificada em utf-8
ser.write(b64_string.encode('UTF-8'))

#os.remove("/ic-mpds2/Foto.png")

cv2.waitKey(0)
cv2.destroyAllWindows()