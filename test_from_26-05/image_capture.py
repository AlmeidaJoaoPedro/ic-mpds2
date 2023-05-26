import cv2
import os
import datetime as dt


def switch_case(key):
    switch_dict = {
        '1': "test_from_26-05/1m/leak_1m.jpg",
        '2': "test_from_26-05/10m/leak_10m.jpg",
        '3': "test_from_26-05/25m/leak_25m.jpg",
        '4': "test_from_26-05/40m/leak_40m.jpg",
        '5': "test_from_26-05/100m/leak_100m.jpg"
    }
    return switch_dict.get(key, None)


# Open the default camera
cap = cv2.VideoCapture(2)

# Read frames from the camera
while(True):
    ret, frame = cap.read()
    # resize = cv2.resize(frame,)

    cv2.imshow('frame',frame)
# pressione a tecla 1 para foto em 1 metro
# pressione a tecla 2 para foto em 10 metros
# pressione a tecla 3 para foto em 25 metros
# pressione a tecla 4 para foto em 50 metros
# pressione a tecla 5 para foto em 100 metros

    key = chr(cv2.waitKey(1) & 0xFF)
    filename = switch_case(key)
    if filename:
        break


cap.release()
cv2.destroyAllWindows()

#armazena o horario e data da foto retirada
data = dt.datetime.now()
data_string = data.strftime("%A %d %B %y %I:%M")
data_datetime = dt.datetime.strptime(data_string,"%A %d %B %y %I:%M")

# escrevendo a data-horario na imagem
cv2.putText(frame,"{}".format   (data_datetime),(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))

# Se o arquivo já existe, adicione um número sequencial ao nome
if os.path.exists(filename):
    index = 1
    while os.path.exists(f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"):
        index += 1
    filename = f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"


# Agora, filename contém um nome de arquivo exclusivo
cv2.imwrite('{}'.format(filename), frame)
print(filename)
