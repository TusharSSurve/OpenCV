import cv2

cap = cv2.VideoCapture(0)
def dodge(x,y):
    return cv2.divide(x,255-y,scale=256)
count =1
while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGrayInv = 255-imgGray
    imgBlur = cv2.GaussianBlur(imgGrayInv, ksize=(21, 21),sigmaX=5, sigmaY=0)
    finalImg = dodge(imgGray,imgBlur)
    cv2.imshow('Face',finalImg) # Sketched Image

    key = cv2.waitKey(1)    
    if key & 0xff==ord('q'):
        break
    if key & 0xff==32: # Press spacebar to take photo

        filename = f'Sketches/Image {count}.jpg'
        count+=1
        cv2.imwrite(filename,finalImg)
