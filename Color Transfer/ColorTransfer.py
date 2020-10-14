import cv2
import numpy as np 

def image_stats(image):
    (l,a,b) = cv2.split(image)
    (lMean,lStd) = (l.mean(),l.std())
    (aMean, aStd) = (a.mean(), a.std())
    (bMean, bStd) = (b.mean(), b.std())
    
    return (lMean, lStd, aMean, aStd, bMean, bStd)

def color_transfer(source,target):
    ''' Convert BGR to LAB'''
    source = cv2.cvtColor(source,cv2.COLOR_BGR2LAB).astype('float32')
    target = cv2.cvtColor(target,cv2.COLOR_BGR2LAB).astype('float32')

    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)
    # subtract the means from the target image
    (l, a, b) = cv2.split(target)
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    l = (lStdTar / lStdSrc) * l
    a = (aStdTar / aStdSrc) * a
    b = (bStdTar / bStdSrc) * b

    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)
    
    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
	
    return transfer

source = cv2.imread('Resources/1.jpg')
target = cv2.imread('Resources/target.jpg')
transfer = color_transfer(source,target)

cv2.imshow('Source',source)
cv2.imshow('Target',target)
cv2.imshow('Transfer',transfer)

cv2.waitKey(0)
