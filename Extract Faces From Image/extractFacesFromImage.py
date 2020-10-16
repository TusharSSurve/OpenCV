import cv2
import os

img = cv2.imread('Resources/Face1.jpg') #Path of an image
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
faces = faceCascade.detectMultiScale(img,1.1,4)

directory = os.getcwd()+r'\Extract Faces From Image\Faces'

try:
    os.mkdir(directory)
except FileExistsError as fee:
    print('Exception Occured',fee)
os.chdir(directory)
i=1
for (x, y, w, h) in faces:
    FaceImg = img[y:y+h,x:x+w]
    # To save an image on disk
    filename = 'Face'+str(i)+'.jpg'
    cv2.imwrite(filename,FaceImg)
    i+=1

