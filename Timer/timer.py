import cv2
from datetime import datetime

# the duration (in seconds)
duration = 5
cap = cv2.VideoCapture(0)
while True:
    
    ret, frame = cap.read()
    start_time = datetime.now()
    diff = (datetime.now() - start_time).seconds # converting into seconds
    while( diff <= duration ):
        ret, frame = cap.read()
        cv2.putText(frame, str(diff), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text
        cv2.imshow('frame',frame)
        diff = (datetime.now() - start_time).seconds
        k = cv2.waitKey(10)
        if k & 0xFF == ord("r"): # reset the timer
            break
        if k & 0xFF == ord("q"): # quit all
            break
        
    break

cap.release()
cv2.destroyAllWindows()