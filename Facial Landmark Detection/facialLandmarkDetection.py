import dlib
import cv2 
import numpy as np 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('Facial Landmark Detection/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)

    for face in faces:
        landmarks = predictor(imgGray,face)
        for i in range(0,68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(img, (x, y), 2, (0,255,0), cv2.FILLED)
    
    cv2.imshow('Facial Landmark Detection',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break