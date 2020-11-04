import cv2 
import dlib 
import math 
from imutils import rotate_bound


## 27,30
path = 'Resources/Face.jpg'
img = cv2.imread(path)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('Face Alignment/shape_predictor_68_face_landmarks.dat')
points = []
facePoints = [27,30]
def getAngle(points):
    b,c,a = points[-3:]
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    ang = round(ang + 360 if ang < 0 else ang)
    print(ang)
    # cv2.putText(img,str(ang),(b[0]-40,b[1]-20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
    return ang


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = detector(imgGray)
for face in faces:
    landmarks = predictor(imgGray,face)
    for i in facePoints:
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        points.append([x,y])
        if i==27:
            points.append([x,y+20])
        print(x,y)
        # cv2.circle(img, (x, y), 2, (0,255,0), cv2.FILLED)

ang = getAngle(points)
imgAligned = rotate_bound(img,ang)
cv2.imshow('Image',imgAligned)
cv2.waitKey(0)