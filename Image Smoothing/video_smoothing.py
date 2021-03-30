import cv2 

cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    imgMedian = cv2.medianBlur(img,3)

    cv2.imshow('Image',img)
    cv2.imshow('median',imgMedian)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break