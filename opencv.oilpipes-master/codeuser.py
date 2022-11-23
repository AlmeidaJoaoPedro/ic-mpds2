import cv2 as cv
import numpy as np 
import serial
from PIL import Image
import os


while(1):
    ser = serial.Serial('COM4', 115200)

    arr = ser.read()

    new_img = Image.fromarray(str(arr))

    print(new_img)
    cv.imshow(new_img)

# new_img.save("foto.png")

# resize = (480,270)
# img = cv.imread('foto.png')
# img_resize = cv.resize(img, resize)
# # cv.imshow("img", img_resize)

# img_color = cv.applyColorMap(img, cv.COLORMAP_JET )
# color_resize = cv.resize(img_color, resize)
# color2hsv = cv.cvtColor(color_resize, cv.COLOR_BGR2HSV)
# # cv.imshow("color", color_resize)


# lowerRed = np.array([0,50,50])
# upperRed = np.array([10,255,255])
# mask1 = cv.inRange(color2hsv, lowerRed, upperRed)


# lower_orange = (10, 100, 20)
# upper_orange = (25, 255, 255)
# mask2 = cv.inRange(color2hsv, lower_orange, upper_orange)


# mask = cv.bitwise_or(mask1, mask2)
# result = cv.bitwise_and(color_resize,color_resize, mask=mask1)
# # cv.imshow('result', result)

cv.waitKey(0)
cv.destroyAllWindows()