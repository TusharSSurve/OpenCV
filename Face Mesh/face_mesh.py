# import cv2
# import mediapipe as mp

# cap = cv2.VideoCapture(0)

# mpFaceMesh = mp.solutions.face_mesh
# faceMesh = mpFaceMesh.FaceMesh()
# mpDraw = mp.solutions.drawing_utils
# drawing_specs = mpDraw.DrawingSpec(thickness=1,circle_radius=1)

# while True:
#     success,img = cap.read()
#     if not success:
#         break
#     imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     results = faceMesh.process(imgRGB)

#     if results.multi_face_landmarks:
#         for facelandmark in results.multi_face_landmarks:
#             mpDraw.draw_landmarks(img,facelandmark,mpFaceMesh.FACE_CONNECTIONS,drawing_specs,drawing_specs)
#     cv2.imshow('Image',img)
#     if cv2.waitKey(1) & 0xff==ord('q'):
#         break

i =1
while True:
    if i%7==0:
        break
    print(i)
    i+=1