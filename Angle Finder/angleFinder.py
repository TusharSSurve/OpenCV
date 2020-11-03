import cv2 
import math

path = 'Resources/angle.jpg'
img = cv2.imread(path)

points = []

	
def getAngle(points):
    b,c,a = points[-3:]
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    ang = round(ang + 360 if ang < 0 else ang)
    print(ang)
    cv2.putText(img,str(ang),(b[0]-40,b[1]-20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)


def click_event(event,x,y,flags,params):
    global points,img
    if event==cv2.EVENT_LBUTTONDOWN:
        if len(points)!=0 and len(points)%3!=0:
            cv2.line(img,tuple(points[round((len(points)-1)/3)*3]),(x,y),(0,255,0),2)
        cv2.circle(img,(x,y),4,(0,255,0),-1)
        points.append([x,y])
        cv2.imshow('Image',img)
        if len(points)%3==0 and len(points)!=0:
            getAngle(points)
            cv2.imshow('Image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        points = []
        img = cv2.imread(path)
        cv2.imshow('Image',img)


cv2.imshow('Image',img)
cv2.setMouseCallback('Image',click_event)
cv2.waitKey(0)