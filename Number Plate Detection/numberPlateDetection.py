import cv2
import pytesseract 

cap = cv2.VideoCapture(0)
noPlateCascade = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nPlates = noPlateCascade.detectMultiScale(imgGray,1.1,3)
    for (x, y, w, h) in nPlates:
        area = w*h
        if area > 500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
            imgRoi = img[y:y+h,x:x+w]
            img_rgb = cv2.cvtColor(imgRoi, cv2.COLOR_BGR2RGB)
            numberPlate = pytesseract.image_to_string(img_rgb)
            if len(numberPlate)>=7:
                print(numberPlate)
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            cv2.imshow('ROI',imgRoi)
    cv2.imshow('Number Plate Detection',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break