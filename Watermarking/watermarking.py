import cv2 
import numpy as np 
path_watermark = 'Resources/Watermark1.png'
logo = cv2.imread(path_watermark)
h_logo,w_logo,_ = logo.shape

path_img = 'Resources/Face2.jpg'
img = cv2.imread(path_img)
h_img,w_img,_ = img.shape

# Coordinates for water mark
if h_img>h_logo and w_img>w_logo:
    gap_x,gap_y = 25,20
else:
    logo = cv2.resize(logo,(int(h_img/3),int(w_img/3)))
    h_logo,w_logo,_ = logo.shape
    gap_x,gap_y = 5,2

top_y = h_img - gap_y - h_logo
left_x = gap_x
bottom_y = h_img - gap_y
right_x = gap_x + w_logo



roi = img[top_y:bottom_y,left_x:right_x]
result = cv2.addWeighted(roi,1,logo,0.5,0)
img[top_y:bottom_y,left_x:right_x] = result
cv2.imshow('Image',img)
cv2.imwrite(path_img.split('/')[1],img)
cv2.waitKey(0)