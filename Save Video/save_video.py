import cv2

cap = cv2.VideoCapture(0)
   
result = cv2.VideoWriter('Save Video/Output Video/filename.avi', cv2.VideoWriter_fourcc(*'MJPG'),30.0, (int(cap.get(3)),int(cap.get(4))))
res = ''

while True:
    success,img = cap.read()
  
    if success == True: 
        if res=='START':
            result.write(img)

        cv2.imshow('Frame', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('p'):
            print('Pause')
            res = 'PAUSE'
        if key == ord('s'):
            print('Start')
            res = 'START'
    else:
        break
  
cap.release()
result.release()
cv2.destroyAllWindows()