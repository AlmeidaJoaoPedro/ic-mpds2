import cv2 as cv
import serial
#instalar essas bibs abaixo
import base64
import io
from imageio import imread

# Define a porta serial e a velocidade de comunicação
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    # Espera até receber dados serial
    if ser.in_waiting > 0:
        # Lê a linha de dados recebida
        linha = ser.readline().decode('utf-8').rstrip()
        # Imprime a linha recebida
        print(linha)
        img = imread(io.BytesIO(base64.b64decode(linha)))
        cv2_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imwrite("reconstructed.png", cv2_img)