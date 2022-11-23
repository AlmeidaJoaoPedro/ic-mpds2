import cv2

captura = cv2.VideoCapture(0)

ret, frame = captura.read()
cv2.imshow("Video", frame)
   
# k = cv2.waitKey(30) & 0xff
# if k == 27:   
#     captura.release()

cv2.waitKey(0)
cv2.destroyAllWindows()