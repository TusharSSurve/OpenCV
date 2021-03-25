import cv2 

cap = cv2.VideoCapture(0)

#*Tracker Types. More Info:- https://ehsangazar.com/object-tracking-with-opencv-fd18ccdd7369
tracker_types = {
    'BOOSTING':cv2.TrackerBoosting_create,
    'MIL':cv2.TrackerMIL_create,
    'TLD':cv2.TrackerTLD_create,
    'MEDIANFLOW':cv2.TrackerMedianFlow_create,
    'CSRT':cv2.TrackerCSRT_create,      #* Slower but more accurate
    'MOSSE':cv2.TrackerMOSSE_create
}

trackers = cv2.MultiTracker_create()

while True:
    timer = cv2.getTickCount()
    success,img = cap.read()

    success,bbox = trackers.update(img)
    if success:
        for box in bbox:
            x,y,w,h = [int(v) for v in box]
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
    else:
        cv2.putText(img,'Object Lost',(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)    
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)
    cv2.imshow('Tracking',img)
    key = cv2.waitKey(1) & 0xff
    if key==ord('s'):
        box = cv2.selectROI("Tracking", img,False)
        #*To run below code please install:- pip install opencv-contrib-python==4.2.0.34
        tracker = tracker_types['MOSSE']()
        trackers.add(tracker, img, box)
    if key==ord('q'):
        break