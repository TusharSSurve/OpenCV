import cv2 
import dlib 
from scipy.spatial import distance
from imutils import face_utils

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('Eye Blink Count Detection/shape_predictor_68_face_landmarks.dat')

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])

	C = distance.euclidean(eye[0], eye[3])
	eye = (A + B) / (2.0 * C)

	return eye

count = 0
total = 0

while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)

    for face in faces:
        landmarks = predictor(imgGray,face)

        landmarks = face_utils.shape_to_np(landmarks)
        leftEye = landmarks[42:48]
        rightEye = landmarks[36:42]

        leftEye = eye_aspect_ratio(leftEye)
        rightEye = eye_aspect_ratio(rightEye)

        eye = (leftEye + rightEye) / 2.0

        if eye<0.3:
            count+=1
        else:
            if count>=3:
                total+=1

            count=0
        
    cv2.putText(img, "Blink Count: {}".format(total), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break