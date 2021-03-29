import cv2 
import numpy as np 

with open('Human Activity Detection/action_recognition_kinetics.txt') as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture(0)
duration = 15

model = cv2.dnn.readNet('Human Activity Detection/resnet-34_kinetics.onnx')

while True:
    images = []
    for i in range(duration):
        success,img = cap.read()
        images.append(img)

    blob = cv2.dnn.blobFromImages(images, 1.0,(112, 112), (114.7748, 107.7354, 99.4750),True,True)
    blob = np.transpose(blob, (1, 0, 2, 3))
    blob = np.expand_dims(blob, axis=0)

    model.setInput(blob)
    outputs = model.forward()
    label = classes[np.argmax(outputs)]

    for img in images:
        cv2.putText(img, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,0.8, (255, 255, 255), 2)
        cv2.imshow('Image',img)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break