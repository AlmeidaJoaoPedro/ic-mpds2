import serial
from PIL import Image
import numpy as np

# Open the serial port
ser = serial.Serial('/dev/ttyUSB1', 9600) # Replace 'COM3' with the name of your serial port

# Wait for the RASPBERRY 1 to send data
while True:
    if ser.in_waiting > 0:
        # Read the incoming string and decode it
        data = ser.readline().decode('utf-8').rstrip()
        # Print the received string
        print(data)



    # matrix = np.fromstring(data, dtype=np.uint8)
    # new_img = Image.fromarray(matrix)
    # new_img.save("leak-img.png")