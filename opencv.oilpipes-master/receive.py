import cv2 as cv
import serial
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
    print("Vazamento")

if str(z) == "0":
    print("Sem vazamento")
        


# while True:
#     data = ser.readline().decode("UTF-8").rstrip() # Read the data from the serial port and remove any trailing whitespace
#     print(data) 


#while True:
    #Espera até receber dados serial
    #if ser.in_waiting > 0:
        # Lê a linha de dados recebida
        #linha = ser.readline().decode('utf-8').rstrip()
        # Imprime a linha recebida
        #print(linha)
        #img = imread(io.BytesIO(base64.b64decode(b64_string)))
        #cv2_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        #cv.imwrite("reconstructed.png", cv2_img)
