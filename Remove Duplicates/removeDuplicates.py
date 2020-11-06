from imutils import paths
import cv2 
import os 
import numpy as np 

def dhash(image,hashsize=8):

    imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(imgGray,(hashsize+1,hashsize))

    diff = resized[:,1:] > resized[:,:-1]

    return sum([2**i for (i,v) in enumerate(diff.flatten()) if v])

imagePaths = list(paths.list_images('New folder'))
hashes = {}

for imagePath in imagePaths:
    img = cv2.imread(imagePath)
    h = dhash(img)

    p = hashes.get(h,[])
    p.append(imagePath)
    hashes[h] = p 

rem = 0 # 0, To check else,1 to remove

for (h,hashedPaths) in hashes.items():
    if len(hashedPaths)>1:
        if rem == 0:
            montage = None
            for p in hashedPaths:
                image = cv2.imread(p)
                image = cv2.resize(image, (150, 150))
                if montage is None:
                    montage = image
                else:
                    montage = np.hstack([montage, image])
            cv2.imshow("Montage", montage)
            cv2.waitKey(0)
        else:
            for p in hashedPaths[1:]:
                print(p)
                os.remove(p) 