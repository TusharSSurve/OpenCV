import cv2
import numpy as np 
# import tkinter as tk
from tkinter import messagebox as mb

def findCanny(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    return imgThres
 
def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,_ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>5000:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest
 
def reorder (myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew
 
def getWidthAndHeight(biggest,imgShape):
    approxWidth = totalWidth = imgShape[1]
    approxHeight = totalHeight = imgShape[0]
    approxWidth = approxWidth-biggest[0][0][0]
    approxWidth =  approxWidth-(totalWidth - biggest[3][0][0])
    
    approxHeight = approxHeight - biggest[0][0][1]
    approxHeight = approxHeight - (totalHeight-biggest[3][0][1])
    return approxWidth + 40,approxHeight + 40


def getWarp(img,biggest):
    biggest = reorder(biggest)
    print(biggest)
    width,height = getWidthAndHeight(biggest,img.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
 
    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
 
    return imgCropped

points = []
def click_event(event,x,y,flags,params):
    global points
    if event==cv2.EVENT_LBUTTONDOWN:
        if len(points)!=4:
            cv2.circle(img,(x,y),4,(255,0,0),-1)
            cv2.imshow('Image',img)
            points.append([int(x),int(y)])
        else:
            cv2.destroyAllWindows()

def callback():
    global points
    cv2.imshow('Image',imgWarp)
    cv2.waitKey(0)
    if mb.askyesno('Verify', 'Want to edit?'):
        cv2.imshow('Image',imgEdit)
        cv2.setMouseCallback('Image',click_event)
        cv2.waitKey(0)

        points = np.array(points)
        imgEdited = getWarp(img,points)
        cv2.imshow('Image',imgEdited)
        cv2.waitKey(0)
    else:
        pass    

img = cv2.imread('Resources/Document.jpg')
imgEdit = img.copy()
imgContour = img.copy()
imgFinal = findCanny(img)
biggest = getContours(imgFinal)
imgWarp = getWarp(img,biggest)
callback()
