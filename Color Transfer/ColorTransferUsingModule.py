import color_transfer
import cv2 

source = cv2.imread('Resources/1.jpg')
target = cv2.imread('Resources/target.jpg')
transfer = color_transfer.color_transfer(source,target)

cv2.imshow('Source',source)
cv2.imshow('Target',target)
cv2.imshow('Transfer',transfer)

cv2.waitKey(0)