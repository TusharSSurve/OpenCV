import cv2 

img = cv2.imread('Resources/noisy_1.jpg')

imgMedian = cv2.medianBlur(img,5)

# For Proper edge detection
imgBilateral = cv2.bilateralFilter(img,9,350,350)

cv2.imshow('Image',img)
cv2.imshow('median',imgMedian)
cv2.imshow('Bilateral',imgBilateral)
cv2.waitKey(0)