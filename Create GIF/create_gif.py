import cv2 
import imageio

cap = cv2.VideoCapture(cv2.CAP_DSHOW)
images = []

while True:
    success,img = cap.read()
    cv2.imshow('Image',img)
    key = cv2.waitKey(0)
    if key==ord('q'):
        break
    if key==ord('s'):
        images.append(img)

with imageio.get_writer('Create GIF/create_gif.gif',mode='I') as writer:
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        writer.append_data(img)
