import cv2

cap = cv2.VideoCapture('Resources/sample.mp4')

count = 0
save_dir = 'Output Frames/'
import os
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    if count%2:
        print(f'{count:04d}')
        cv2.imwrite(save_dir + f"frame{count:04d}.jpg", frame)
    count += 1

cap.release()
cv2.destroyAllWindows()