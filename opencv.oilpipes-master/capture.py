import serial
import cv2 as cv
from PIL import Image
import numpy as np 

ser = serial.Serial('/dev/ttyUSB1', 9600)

webcam = cv.VideoCapture(0)
ret, frame = webcam.read()
cv.imwrite("Foto.jpg", frame)

#img = Image.open("Foto.jpg")
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

# cropped_image = mask1[120:300, 450:700]
cropped_image = mask1[360:540, 0:960]

list_mask1 = cropped_image.ravel().tolist()
# print(list_mask1)

soma = np.sum(list_mask1)
# print(soma)


if(soma >= 1):
    x = "1"
    print(x)
else:
    x = "0"
    print(x)

ser.write(x.encode("UTF-8"))

cv.waitKey(0)
cv.destroyAllWindows()

