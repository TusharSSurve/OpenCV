import cv2
import numpy as np
modelFile = "Face Detector Advance/models/res10_300x300_ssd_iter_140000.caffemodel"
configFile = "Face Detector Advance/models/deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,(300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    for i in range(faces.shape[2]):
        confidence = faces[0, 0, i, 2]
        if confidence > 0.5:
            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(img, (x, y), (x1, y1), (128,128,128), 2)
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break