import cv2 
import mediapipe as mp 

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                print(id,lm) # lm produce output in ratio format
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                cv2.circle(img,(cx,cy),4,(0,0,255),cv2.FILLED)
                
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break