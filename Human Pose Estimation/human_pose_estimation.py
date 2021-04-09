import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    success,img = cap.read()
    if not success:
        break
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break