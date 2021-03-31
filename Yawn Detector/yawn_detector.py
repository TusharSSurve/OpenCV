import cv2 
import numpy as np 
import dlib 
from math import hypot

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('Yawn Detector/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)
def get_mouth_ratio(mouth_points,facial_landmarks):
    left_point = facial_landmarks.part(mouth_points[0]).x, facial_landmarks.part(mouth_points[0]).y
    right_point = facial_landmarks.part(mouth_points[2]).x , facial_landmarks.part(mouth_points[2]).y 

    top_point = facial_landmarks.part(mouth_points[1]).x, facial_landmarks.part(mouth_points[1]).y
    bottom_point = facial_landmarks.part(mouth_points[3]).x , facial_landmarks.part(mouth_points[3]).y 

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((top_point[0] - bottom_point[0]), (top_point[1] - bottom_point[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)
    for face in faces:
        landmarks = predictor(imgGray,face)
        mouth_ratio = get_mouth_ratio([48,51,54,57],landmarks)
        
        if mouth_ratio < 1.65:
            cv2.putText(img,"Yawning",(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    
    cv2.imshow('Facial Landmark Detection',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break