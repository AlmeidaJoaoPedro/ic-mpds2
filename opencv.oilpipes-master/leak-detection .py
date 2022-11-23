import numpy as np
import cv2 as cv

resize = (480,270)
img = cv.imread('img/lab-2.jpg')
img_resize = cv.resize(img, resize)
cv.imshow("img", img_resize)

img_color = cv.applyColorMap(img, cv.COLORMAP_JET )
color_resize = cv.resize(img_color, resize)
color2hsv = cv.cvtColor(color_resize, cv.COLOR_BGR2HSV)
cv.imshow("color", color_resize)


lowerRed = np.array([0,50,50])
upperRed = np.array([10,255,255])
mask1 = cv.inRange(color2hsv, lowerRed, upperRed)


lower_orange = (10, 100, 20)
upper_orange = (25, 255, 255)
mask2 = cv.inRange(color2hsv, lower_orange, upper_orange)


mask = cv.bitwise_or(mask1, mask2)
result = cv.bitwise_and(color_resize,color_resize, mask=mask1)
cv.imshow('result', result)

cv.waitKey(0)
cv.destroyAllWindows()














# result = img_HSV.copy()
# cv.imshow("img", color2hsv)
# cv.imshow('mask', mask)
# lower_red = np.array([0,50,50])
# upper_red = np.array([10,255,255])
# mask0 = cv.inRange(img_HSV, lower_red, upper_red)

# lower_red = np.array([170,50,50])
# upper_red = np.array([180,255,255])
# mask1 = cv.inRange(img_hsv, lower_red, upper_red)

# mask = mask0+mask1
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (5, 5), 0)
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# cv.imshow("red", mask)


## mask of Red (36,0,0) ~ (70, 255,255)
# mask1 = cv.inRange(color_resize, lower_red, upper_red)

## mask o yellow (15,0,0) ~ (36, 255, 255)
# mask2 = cv.inRange(hsv_resize, (15,0,0), (36, 255, 255))

## final mask and masked
# mask = cv.bitwise_or(mask1, mask2)
# target = cv.bitwise_and(img_color,img_color, mask=mask)


# image = cv.imread('img/dd9tg.jpg')

