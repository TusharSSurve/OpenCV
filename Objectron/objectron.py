import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpObjectron = mp.solutions.objectron
# Currently supports {'Shoe', 'Chair', 'Cup', 'Camera'}
objectron = mpObjectron.Objectron(model_name='Shoe')
mpDraw = mp.solutions.drawing_utils

while True:
    success,img = cap.read()
    if not success:
        break
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = objectron.process(imgRGB)

    if results.detected_objects:
        for detected_object in results.detected_objects:
            mpDraw.draw_landmarks(img,detected_object.landmarks_2d,mpObjectron.BOX_CONNECTIONS)
            mpDraw.draw_axis(img, detected_object.rotation,detected_object.translation)
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

            